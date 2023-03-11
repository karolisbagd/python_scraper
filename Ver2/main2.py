from bs4 import BeautifulSoup
import requests
import time

print('Please type feature you like to see')
unfamiliar_description = input('>')
print(f'Filtering out {unfamiliar_description}')

html_text = requests.get('https://www.cv-library.co.uk/cloud-jobs?us=1').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', class_='job search-card')


def find_jobs():
    for job in jobs:
        publish_date = job.find(
            'p', class_='job__posted-by').text.replace(' ', '')
        if 'yesterday' in publish_date:
            company_name = job.find(
                'a', class_='job__company-link').text.replace(' ', '')
            description = job.find(
                'p', class_='job__description noscript-show').text
            job_title = job.find('h2', class_='job__title').text.replace(
                ' ', '')  # for span tags use span.text
            more_info = job.div.h2.a['href']
            if unfamiliar_description not in description:
                print(f"{publish_date.strip()}")
                print(f"{description.strip()}")
                print(f"{more_info}")
                print(' ')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
