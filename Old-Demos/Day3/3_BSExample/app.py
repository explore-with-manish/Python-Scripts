import requests
from bs4 import BeautifulSoup

headers = {}
headers['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"

url = "https://www.google.com/search?q=Synechron"
req = requests.get(url, headers)

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())

all_links = soup.findAll('a')

for link in all_links:
    # print(link)
    print(link.get('href'))