from tools import utils
from settings import STORE_DIR, LATEST_FILE, URLS

data = utils.extract_multiple_info(multiple_urls=URLS)

utils.save_items(dir_name=STORE_DIR, data=data, jsonfile=LATEST_FILE)
