
import requests
from bs4 import BeautifulSoup

response = requests.get("https://scholar.google.com")

html = BeautifulSoup(response.text, "html.parser")

print(html.prettify())

   import random

random_number = random.randint(1, 10)
print(f"The random number is: {random_number}")


