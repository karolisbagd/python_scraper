from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.cv-library.co.uk/cloud-jobs?us=1').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('article', class_='job search-card')
company_name = job.find('a', class_='job__company-link').text.replace(' ', '')
description = job.find(
    'p', class_='job__description noscript-show').text.replace(' ', '')
job_title = job.find('h2', class_='job__title').text.replace(
    ' ', '')  # for span tags use span.text

print(f'''
Company Name: {company_name}
Job Title: {job_title}
{description}
''')

# print(skills)
# print(company_name)
