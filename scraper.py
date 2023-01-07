# Utilize Requests to obtain the HTML.
import requests
url = 'https://en.wikipedia.org/wiki/List_of_heads_of_state_of_Lithuania/'
response = requests.get(url)