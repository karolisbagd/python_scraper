from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.cv-library.co.uk/cloud-jobs?us=1').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', attrs={'class': 'job search-card'})
for job in jobs:
    company_name = job.find('a', attrs={'class': 'job__company-link'})
    if company_name:
        print(company_name.text)
    else:
        print("Company name not found")
