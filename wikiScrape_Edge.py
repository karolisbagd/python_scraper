import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver import Edge

driver = Edge(executable_path=r'C:\Users\KarolisBagdonas\Downloads\edgedriver\msedgedriver.exe')

driver.get('https://en.wikipedia.org/wiki/Solar_System')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

for header_element in soup.findAll(['h2', 'h4']):
    results.append(header_element.text)

df = pd.DataFrame({'Text': results})
df.to_csv('wikipedia_text.csv', index=False)

driver.quit()