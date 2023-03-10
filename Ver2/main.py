from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.totaljobs.com/jobs/cloud?radius=10').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('div', class_='ResultsSectionContainer-sc-gdhf14-0 kteggz')
company_name = jobs.find('h2', class_='sc-fzqMAW krdChg')
