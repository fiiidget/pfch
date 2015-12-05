from bs4 import BeautifulSoup
import requests
#from pfchfunctions import cardlist
from time import sleep
import sys
import csv

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

HOFplayernames = []
HOFplayerpages = []

url = ('http://www.baseball-reference.com/awards/hof.shtml')

HOF_page = requests.get(url)

if HOF_page.status_code != 200:
    print ("there was an error with", url)


page_html = HOF_page.text

#page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

player_names = soup.find_all("div", attrs = {"id" : "div_hof"})

for item in player_names:
    # holder = soup.find("div", attrs = {"style" : "overflow:auto"})
    #
    # for thing in holder:
    playercsv = soup.find("pre", attrs = {"id" : "csv_hof"})


uprint(playercsv.text)

# for player in player_names:
#     hofname = player.text
#     if hofname not in HOFplayernames:
#         HOFplayernames.append(hofname)
#
# for player in player_names:
#     playerlink = soup.find_all("a")
#
#     for link in playerlink:
#         uprint(link.text)
#         uprint(link['href'])
#         # page = link.attrs["href"]
#         # if page not in HOFplayerpages:
#         #     HOFplayerpages.append(page)
#
# # uprint [tag.attrMap['href'] for tag in html.findall('a', {'href' : True})]
# #for a_player in player_names:
# # uprint(HOFplayernames)
# # uprint(HOFplayerpages)
