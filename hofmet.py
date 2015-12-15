from bs4 import BeautifulSoup
import requests
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

Players_List = []
HOF = {}
HOFplayernames = []
card_titles = []
HOFinMET = []
not_in_met = []

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

    player = player_link.text
    link = player_link["href"]

    if player not in HOF:

        HOF[player] = [link]

    HOFplayernames.append(player)

for x in HOFplayernames:

    url = ("http://www.metmuseum.org/collection/the-collection-online/search?&noqs=true&ao=on&what=Baseball+cards&pg=1&ft="+str(x))

    result_page = requests.get(url)
    if result_page.status_code != 200:
        uprint("oops, this one's no good: ", url)
        time.sleep(0.2)

    result_html = result_page.text

    soup = BeautifulSoup(result_html, "html.parser")

    no_results = soup.find_all("div", attrs = {"class" : "no-results"})

    for result in no_results:

        no_player = result.find_all("span", attrs = {"class" : "no-results-searchterm"})

        for player in no_player:

            not_in_met.append(player.text)

    # item_container = soup.find_all("div", attrs = {"class" : "list-view-object-info"})
    #
    # for list_item in item_container:
    #
    #     item_name = list_item.find_all("div", attrs = {"class" : "objtitle"})
    #
    #     for name in item_name:
    #
    #         card_titles.append(name.text)
            #uprint(name.text)

HOFcopy = HOF.copy()

for guy in HOFcopy:

    if guy in not_in_met:

        del HOF[guy]

    if guy not in not_in_met:

        HOFinMET.append(guy)


uprint(HOF)
uprint(len(HOF))
uprint(len(HOFinMET))
# uprint(HOF)
# uprint(HOFplayernames)
