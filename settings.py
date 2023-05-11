"""
1. Define the folder that will hold the files
2. Define skroutz product detail page urls for the items you want to track
3. Define the filename that will hold the latest prices
"""
STORE_DIR = 'storage/'
LATEST_FILE = 'latest_price.json'
LOG_DIR = STORE_DIR + LATEST_FILE 

URLS = [
    'https://www.skroutz.gr/s/34990039/Lenovo-IdeaPad-3-15ITL6-15-6-IPS-FHD-i3-1115G4-8GB-512GB-SSD-W11-Home-Arctic-Grey-US-Keyboard.html?product_id=116277144&sponsored=true',
    'https://www.skroutz.gr/s/27001920/HP-255-G8-15-6-FHD-Athlon-3020e-8GB-256GB-SSD-No-OS-GR-Keyboard.html?product_id=139302418&sponsored=true',
    'https://www.skroutz.gr/s/29606721/Apple-MacBook-Air-13-3-2020-IPS-Retina-Display-M1-16GB-256GB-SSD-Space-Gray-International-English-Keyboard.html?product_id=148442164&sponsored=true',
    'https://www.skroutz.gr/s/37725758/Lenovo-IdeaPad-3-15ALC6-15-6-IPS-FHD-Ryzen-5-5500U-8GB-512GB-SSD-W11-Home-Arctic-Grey-US-Keyboard.html?product_id=126315681&sponsored=true'
]
