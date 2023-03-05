# website-email-scraper
Web Scraper for Finding Email Addresses

This Python script uses the requests and BeautifulSoup libraries to scrape a website for email addresses that contain a specified search string. The script recursively searches all links on a page and writes any email addresses found to a file named scre.txt.
Usage

To use this script, run the following command in a terminal window:

python website-email-scraper.py

You will then be prompted to enter the base URL and search string for the email addresses you wish to find. The script will then begin scraping the website and output any email addresses found to the console and the scre.txt file.
Dependencies

This script requires the following libraries to be installed:

    requests
    beautifulsoup4

You can install them using pip:

pip install requests beautifulsoup4

Usage:

python website-email-scraper.py

Enter the Base URL: example.com <--- Your Base URL
Enter the search string for url: example <--- Your Text Included In Base URL
