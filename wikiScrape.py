import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
driver.get('https://en.wikipedia.org/wiki/Solar_System')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for header_element in soup.findAll(['h2', 'h3']):
    results.append(header_element.text)

df = pd.DataFrame({'Text': results})
df.to_csv('wikipedia_text.csv', index=False)

driver.quit()
