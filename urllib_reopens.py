import urllib.request
from bs4 import BeautifulSoup
import re


url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read()
soup = BeautifulSoup(url)

line1 = soup.find_all('a')

needed_line = 'http://www.pythonchallenge.com/pc/def/' + line1[0].get('href')

#needed_line = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682'

tushka = re.findall(r'\D+', needed_line)

count = 0
current_number = ''
while True:

    current_url = str(urllib.request.urlopen(needed_line).read())

    if len(re.findall(r'\d+', current_url)) == 1:

        temp_number = re.findall(r'\d+', current_url)
        current_url1 = str(tushka[0] + temp_number[0])
        needed_line = current_url1

    elif re.search(r'\d+', current_url) is None:

        temp_number = re.search(r'\d+', needed_line).group()
        current_url1 = str(tushka[0] + str(int(temp_number)/2))
        needed_line = current_url1

    elif len(re.findall(r'\d+', current_url)) > 1:

        temp_temp = re.findall(r'the next nothing is \d+', current_url)
        temp_number = re.findall(r'\d+', temp_temp[0])
        current_url1 = str(tushka[0] + temp_number[0])
        needed_line = current_url1

    count = count + 1
    print(count)
    print(current_url1)
    print(current_url)

print(current_url1)



