# Import the BeautifulSoup library
from bs4 import BeautifulSoup

# Open the HTML file in read-only mode
with open("Ver1/beverages.html", "r") as html_file:
    # Read the contents of the file
    content = html_file.read()

# Create a BeautifulSoup object with the contents of the file and lxml parser
soup = BeautifulSoup(content, 'lxml')

# Find all span elements with class 'caret'
beverage_items = soup.find_all('span', class_='caret')

# Iterate over the course cards and extract the course name
for beverage in beverage_items:
    # Find the parent li element of the current span element and extract its text
    beverage_name = beverage.find_parent('li').text
    
    # Print the course name
    print(f'{beverage_name}')

