import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
driver.get('https://www.gumtree.com/computers-software/w5')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for element in soup.findAll('h2'):
    results.append(element.text)

df = pd.DataFrame({'Text': results})
df.to_excel('wikipedia_text.xlsx', index=False)

driver.quit()
