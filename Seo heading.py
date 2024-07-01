import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
URL = 'https://www.feedough.com/recommerce-business-model/'

# Send a GET request to the URL
response = requests.get(URL)

# Parse the HTML content of the page using BeautifulSoup
bs = BeautifulSoup(response.text, 'lxml')

# Find all heading tags H1, H2, H3, H4, H5
headings = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])

# Extract and print the text of each heading
for heading in headings:
    print(heading.name + ': ' + heading.text.strip())
