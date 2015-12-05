from bs4 import BeautifulSoup
import requests
#from pfchfunctions import cardlist
import sys
import csv

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

HOF = {}
HOFplayernames = []
HOFplayerpages = []

url = ('http://www.baseball-reference.com/awards/hof.shtml')

HOF_page = requests.get(url)

if HOF_page.status_code != 200:
    print ("there was an error with", url)


page_html = HOF_page.text

#page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

HOFtable = soup.find_all("table", attrs = {"id" : "hof"})

for arow in HOFtable:

    a_player = arow.find_all("a")

for player_link in a_player:

#Should I bother to extract just the player inductees? There might be matches for managers?

    HOFplayernames.append(player_link.text)

    HOFplayerpages.append(player_link["href"])

#put the things in the dictionary, make the dictionary xml? #actually do you really need to write it to anything?

HOF = dict(zip(HOFplayernames, HOFplayerpages))

writer = csv.writer(open('HOFdict.csv', 'w'))

for key, value in HOF.items():
    writer.writerow([key, value])

# uprint(HOF)
