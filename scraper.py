import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome(
    executable_path=r'C:\Users\Admin\Documents\UWL\Year3\Project\chromedriver.exe')  # webdriver.Chrome()

# driver.get("HTML")
driver.get('https://en.wikipedia.org/wiki/List_of_heads_of_state_of_Lithuania')
results = []
other_results = []
# Add the page source to the variable `content`.
content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup
# class, which analyzes the HTML as a nested data structure and allows to select
# its elements by using various selectors.
soup = BeautifulSoup(content)
for element in soup.findAll(attrs={'class': 'mw-headline'}):
    name = element.find('a')
    if name not in results:
        # Add the object of “name” to the list “results” extracts the text in the element, omitting the HTML tags.
        results.append(name.text)

# Turns object into a two-dimensional data table.
df = pd.DataFrame({'Names': results})
# 'names.csv' = adding extendsion, index = specific starting point in column, encode = specific format
df.to_csv('names.xlsx', index=False, encoding='utf-8')
