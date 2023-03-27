from bs4 import BeautifulSoup
import requests
import time

print('Please type feature you dont like to see')
unfamiliar_description = input('>')
print(f'Filtering out {unfamiliar_description}')


def find_jobs():
    html_text = requests.get(
        'https://www.cv-library.co.uk/cloud-jobs?us=1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('article', class_='job search-card')
    # enumarete func allows us to itterate over the index of the jobs list & job content
    for index, job in enumerate(jobs):
        publish_date = job.find(
            'p', class_='job__posted-by').text.replace(' ', '')
        if 'yesterday' in publish_date:
           # company_name = job.find(
            #  'a', class_='job__company-link').text.replace(' ', '')
            description = job.find(
                'p', class_='job__description noscript-show').text
            # for span tags use span.text
            job_title = job.find('h2', class_='job__title').text
            more_info = job.div.h2.a['href']
            if unfamiliar_description not in description:
                # 'w' Writing inside the file
                with open(f'Ver2/posts/{index}.txt', 'w') as f:
                    f.write(f"{job_title.strip()} \n")
                    f.write(f"{publish_date.strip()} \n")
                    f.write(f"{description.strip()} \n")
                    f.write(f"{more_info}")
                print(f'File saved: {index}')


'''if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait * 1)'''
