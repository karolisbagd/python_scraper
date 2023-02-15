import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome(
    executable_path=r'C:\Users\Admin\Documents\UWL\Year3\Project\chromedriver.exe')
driver.get('https://en.wikipedia.org/wiki/Solar_System')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

driver.quit()

for element in soup.findAll(attrs='mw-body'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
