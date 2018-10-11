from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import re
import collections

page = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")


soup = BeautifulSoup(page, "html.parser")

comments = soup.findAll(text=lambda text: isinstance(text, Comment))

result_mid = re.findall("[A-Z]{3}[a-z][A-Z]{3}", comments[0])

#n = 0

#list_dohuya = []

#for abvgd in result_mid:

#    abvgd_temp = abvgd[3]

#    list_dohuya.append(abvgd_temp)


#comments.remove("\nfind rare characters in the mess below:\n")


#result = collections.Counter(comments[0])


#result = dict((k, v) for k, v in result.items() if v == 1)


print(result_mid)

