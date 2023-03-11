from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.totaljobs.com/jobs/cloud?radius=10').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('div', class_='Wrapper-sc-11673k2-0 eHVkAX')
company_name = job.find('div', class_='sc-fzoiQi kuzZTz')
