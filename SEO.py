import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
URL = 'https://en.wikipedia.org/wiki/Recommerce'

# Send a GET request to the URL
response = requests.get(URL)

# Parse the HTML content of the page using BeautifulSoup
bs = BeautifulSoup(response.text, 'lxml')

# Find all anchor tags with href attribute starting with '/wiki/'
links = bs.find_all('a', href=True)

# Extract and print words that have links to other Wikipedia pages
linked_words = []
for link in links:
    href = link['href']
    if href.startswith('/wiki/'):
        linked_words.append(link.text.strip())

# Print the words with links
for word in linked_words:
    print(word)

