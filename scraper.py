import requests
from bs4 import BeautifulSoup

# Utilize Requests to obtain the HTML.
url = 'https://oxylabs.io/blog'
response = requests.get(url)

# Locate the element
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

# Find all titles in H2 elements
blog_titles = soup.find_all('h2', attrs={"class":"blog-card__content-title"})
for title in blog_titles:
    print(title.text)
# Output:
# Prints all blog tiles on the page