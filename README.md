# Skroutz Price Comparison Tool


## Brief Summary
 The purpose of this project is to provide a tool that can fetch URLs from
 a content aggregator, save the prices and some information in JSON format,
 and compare the prices fetched during the next run of the program. 
 This will help users keep track of changes in prices over time and make informed
 decisions about purchasing products.

## Why is this app created?

# Structure


# Installation and Usage



# Next steps in the project
Project Title: Price Comparison Tool

Purpose:
Features:

    Fetch URLs from a content aggregator
    Save prices and some information in JSON format
    Compare prices with previous data
    Update JSON file with latest prices if the prices are different
    Run on schedule or manually

Documentation:
This project requires some basic knowledge of Python and JSON. The code is structured into three main components:

    Fetching URLs: The fetch_urls() function takes a list of URLs from a content aggregator and retrieves the HTML content from each URL. It then uses BeautifulSoup to parse the HTML content and extract relevant information, such as the name and price of the product.

    Saving data: The save_data() function takes the extracted data and saves it in JSON format. It saves the data in a file named data_time.json where time is the current date and time in the format YYYY-MM-DD_HH:MM:SS.

    Comparing prices: The compare_prices() function compares the prices fetched during the current run of the program with the prices saved in the data_time.json file. If the prices are different, it updates the file with the latest prices and saves them in a new file named latest_price.json.

## User Manual:
To use this program, follow these steps:
- Install Python 3.10 or later.
- Clone the repository from GitHub.
- Open the command prompt and navigate to the project directory.
- Run install_gecko.sh to download geckodriver
- Install the required dependencies by running pip install -r requirements.txt.
- Edit the settings.py file to include the list of URLs you want to fetch data from,
<directory name> to store json files and <filename> that is used to save the new prices every
time a price has changed
- Execute run_init.py to create directory and make the first fetch
- Run the program by executing the command python main.py.
- Wait for the program to finish running.
- Each time the main.py is running creates a <datetime>.json with the daily prices
- The new prices are also replaced in the <filename>.json 

## Developer Guide:
If you want to modify the code, here are some guidelines:
- The main program is in the main.py file.
- The fetch_urls(), save_data(), and compare_prices() functions are defined in the utils.py file.
- The settings.py file contains the URLs to fetch data from.
- The requirements.txt file contains the required dependencies.
- Use virtualenv to create a virtual environment and install the dependencies.
