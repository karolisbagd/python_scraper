from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.totaljobs.com/jobs/cloud?radius=10').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('div', class_='Wrapper-sc-11673k2-0 eHVkAX')
company_name = jobs.find('h2', class_='sc-fzqMAW krdChg')
