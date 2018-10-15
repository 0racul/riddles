import urllib.request
from bs4 import BeautifulSoup
import re


url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read()
soup = BeautifulSoup(url)

line1 = soup.find_all('a')

needed_line = 'http://www.pythonchallenge.com/pc/def/' + line1[0].get('href')

tushka = re.findall(r'\D+', needed_line)

count = 0
current_number = ''
while True:

    current_url = str(urllib.request.urlopen(needed_line).read())
    temp_number = re.search(r'the next nothing is \d+', current_url).group()
    if temp_number is not None:
        current_number = re.search(r'\d+', temp_number).group()
        current_url1 = str(tushka[0] + current_number)
        needed_line = current_url1

    elif temp_number is None:

        current_number = re.search(r'\d+', needed_line).group()
        current_url1 = str(tushka[0] + str(int(current_number)/2))
        needed_line = current_url1

    count = count + 1
    print(count)
    print(current_number)
    print(current_url)

print(current_url1)



