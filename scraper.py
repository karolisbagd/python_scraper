import requests
from bs4 import BeautifulSoup

# Utilize Requests to obtain the HTML.
url = 'https://oxylabs.io/blog'
response = requests.get(url)

# Locate the element
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)
