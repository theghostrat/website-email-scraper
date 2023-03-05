from urllib.parse import urljoin
import re
import requests
from bs4 import BeautifulSoup

def find_emails(url, search_string, visited_urls=set()):
    # check if the URL has already been visited or doesn't contain the search string
    if (url in visited_urls) or (search_string not in url):
        return
    visited_urls.add(url)
    try:
      # fetch the page content
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')
      text = soup.get_text()
  
      # find email addresses in the page text
      emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
  
      # print the email addresses found on this page
      print(f"Email addresses found on {url}:")
      for email in emails:
        with open("emails.txt", "a") as f:
          f.write(email)
          f.write('\n')
          print(email)
  
      # find any links on the page and recurse into them
      for link in soup.find_all('a'):
          href = link.get('href')
          href = str(href)
          if href.startswith('http'):
              find_emails(href, search_string, visited_urls)
          else:
              abs_url = urljoin(url, href)
              find_emails(abs_url, search_string, visited_urls)
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,requests.exceptions.InvalidSchema, requests.exceptions.Timeout):
      print(f"Skipping invalid URL: {url}")
        
  

url = input("Enter the Base URL: ")
search_str = input("Enter the search string for url: ")

# call the function with a starting URL and url search string
find_emails(url, search_str)
