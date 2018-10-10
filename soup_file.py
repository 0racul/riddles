from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import collections

page = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")


soup = BeautifulSoup(page, "html.parser")

comments = soup.findAll(text=lambda text: isinstance(text, Comment))

comments.remove("\nfind rare characters in the mess below:\n")


result = collections.Counter(comments[0])


result = dict((k, v) for k, v in result.items() if v == 1)


print(result)

