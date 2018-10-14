import requests
from bs4 import BeautifulSoup

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
all_href = soup.findall(r"<a href=\"(.+)\">")
print(all_href)
