import os
from settings import STORE_DIR, LATEST_FILE, URLS, LOG_DIR
from tools.utils import (extract_multiple_info,
                         fetch_old_values,
                         compare_prices, save_items)

if not os.path.exists(LOG_DIR):
    print("Initialize app")
    data = extract_multiple_info(multiple_urls=URLS)
    save_items(dir_name=STORE_DIR, data=data, jsonfile=LATEST_FILE)
else:
    new_info = extract_multiple_info(multiple_urls=URLS)
    old_data = fetch_old_values(LOG_DIR)
    compare_prices(jsonfile=LATEST_FILE, dir_name=STORE_DIR,
                   new_data=new_info, past_data=old_data)
