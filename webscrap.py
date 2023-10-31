
import requests
from bs4 import BeautifulSoup

response = requests.get("https://scholar.google.com")

html = BeautifulSoup(response.text, "html.parser")

print(html.prettify())
    

