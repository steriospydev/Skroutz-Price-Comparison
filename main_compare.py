import utils
from run_init import store_dir, filename, urls, file_path

new_info = utils.extract_multiple_info(urls=urls)

old_data = utils.fetch_old_values(file_path)

utils.compare_prices(filename=filename,
                store_dir=store_dir,
                new_data=new_info,
                old_data=old_data)