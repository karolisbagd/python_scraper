# import the necessary libraries
from bs4 import BeautifulSoup  # for parsing HTML and XML documents
import requests  # for sending HTTP requests

# send a GET request to the specified URL and get the HTML content as text
html_text = requests.get('https://www.cv-library.co.uk/cloud-jobs?us=1').text

# create a BeautifulSoup object by parsing the HTML content using the lxml parser
soup = BeautifulSoup(html_text, 'lxml')

# find all the articles with the class "job search-card"
jobs = soup.find_all('article', attrs={'class': 'job search-card'})

# loop through each job article and extract the company name
for job in jobs:
    # find the company name link
    company_name = job.find('a', attrs={'class': 'job__company-link'})
    if company_name:  # if a company name link is found
        # print the company name text with spaces removed
        print(company_name.text.replace(' ', ''))
    else:
        # print an error message if no company name link is found
        print("Company name not found")


