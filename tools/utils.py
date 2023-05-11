import os
from typing import List, Dict
import datetime
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def fetch_url(url: str) -> str:
    """Fetch html content using Selenium Firefox webdriver and return the page"""
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    # print(driver.execute_script("return document.readyState"))
    return driver.page_source

def create_soup(page: str) -> BeautifulSoup:
    """Convert page to soup object"""
    return BeautifulSoup(page, 'html.parser')

def get_info(obj: BeautifulSoup, tag: str, attr: Dict) -> str:
    return obj.find(tag, attrs=attr).text

def construct_values(url: str, title: str, price: str,
                     values: Dict = {}) -> Dict:
    values['url'] = url
    values['title'] = title
    values['price'] = price if price else 'Product temporary unavailable.'
    return values


def extract_info(url: str) -> Dict:
    """Takes url and returns a dictionary from selected tags."""
    page = fetch_url(url)
    obj = create_soup(page)

    print(f'Process URL:\n{url}')
    title = get_info(obj, tag='h1', attr={'class', 'page-title'})
    price = get_info(obj, tag='strong', attr={'class', 'dominant-price'})
    data = construct_values(url=url, price=price, title=title)
    print("\nDone.\n")
    return data

def extract_multiple_info(multiple_urls: List) -> List:
    multiple = []
    for url in multiple_urls:
        url_data = extract_info(url=url)
        # create a new dictionary object
        multiple.append(dict(url_data))
    return multiple

# FileModel
def create_dir(dir_name: str) -> None:
    """ Create folder to store output"""
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
        print(f"Store dict: {dir_name} created successfully.")

def new_file() -> str:
    now = datetime.datetime.now().date()
    return f'{now}.json'

def save_items(data: List, dir_name: str = '',
               jsonfile: str = '') -> None:
    # Save items   
    if dir_name != '':
        create_dir(dir_name)
    if jsonfile == '':        
        jsonfile = new_file()
    full_path = dir_name + jsonfile
    with open(full_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
        print(f'{jsonfile} saved.')

def fetch_old_values(file_archive: str) -> json:
    # Load info from basic file. Create it if it does not exist
    with open(file_archive) as f:
        past_data = json.load(f)
        return past_data

#
def compare_prices(jsonfile: str, dir_name: str,
                   past_data: List, new_data: List):
    """Compare scraped prices with the last ones."""
    for i in range(len(new_data)):
        title = new_data[i]['title']
        price_new = new_data[i]['price']
        price_old = past_data[i]['price']
        print(f'{i}:\t{title}')
        print('-'*100)
        print(f'New price:\t{price_new}')
        print(f'Old price:\t{price_old}')
        print('\n')
        if price_old == price_new:
            print('Price has not changed yet.\n')
        else:
            print('Price has changed.') 
        print('-'*100)    
        past_data[i]['previous_price'] = price_old
        past_data[i]['price'] = price_new

    save_items(data=new_data, dir_name=dir_name)
    save_items(data=past_data, dir_name=dir_name, jsonfile=jsonfile)
    print('latest_json updated!!')


if __name__ == "__main__":
    store_dir = '../storage/'
    filename = 'last_price.json'
    urls = [
   'https://www.skroutz.gr/s/34990039/Lenovo-IdeaPad-3-15ITL6-15-6-IPS-FHD-i3-1115G4-8GB-512GB-SSD-W11-Home-Arctic-Grey-US-Keyboard.html?product_id=116277144&sponsored=true'
   'https://www.skroutz.gr/s/27001920/HP-255-G8-15-6-FHD-Athlon-3020e-8GB-256GB-SSD-No-OS-GR-Keyboard.html?product_id=139302418&sponsored=true',
   'https://www.skroutz.gr/s/29606721/Apple-MacBook-Air-13-3-2020-IPS-Retina-Display-M1-16GB-256GB-SSD-Space-Gray-International-English-Keyboard.html?product_id=148442164&sponsored=true',
   'https://www.skroutz.gr/s/37725758/Lenovo-IdeaPad-3-15ALC6-15-6-IPS-FHD-Ryzen-5-5500U-8GB-512GB-SSD-W11-Home-Arctic-Grey-US-Keyboard.html?product_id=126315681&sponsored=true'
    ]
    file_path = store_dir + filename 

    info = extract_multiple_info(multiple_urls=urls)
    # save_items(store_dir=store_dir, data=info, filename=filename)

    old_data = fetch_old_values(file_path)
    compare_prices(jsonfile=filename,
                   dir_name=store_dir,
                   new_data=info,
                   past_data=old_data)
