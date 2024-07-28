# Skroutz Price Comparison Tool


## Brief Summary
Track prices on an online marketplace
## Features:
 - Retrieve info from a product's detail page given as a list of URLs 
 - Save prices in JSON format
 - Compare prices with previous data
 - Update JSON file with latest prices if the prices are different
 - Run on schedule or manually

## Installation and Usage|:

To use this program, follow these steps:
- Install Python 3.10 or later.
- Clone the repository from GitHub.
- Open the command prompt and navigate to the project directory.
- Run tools/install_gecko.sh to download geckodriver
- Install the required dependencies by running pip install -r requirements.txt.
- Edit the settings.py file to include the list of URLs you want to fetch data from,
<directory name> to store json files and <filename> that is used to save the new prices every
time a price has changed
- Run the program by executing the command python main.py.
- Wait for the program to finish running.
- Each time the main.py is running creates a <datetime>.json with the daily prices
- The new prices are also replaced in the <filename>.json 

## Developer Guide:
If you want to modify the code, here are some guidelines:
- The main program is in the main.py file.
- All functions are defined in the tools/utils.py file.
- The settings.py file contains the URLs to fetch data from.
- The requirements.txt file contains the required dependencies.
- Use virtualenv to create a virtual environment and install the dependencies.

## Libraries
- selenium
- bs4
