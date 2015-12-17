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
HOFinMET = {}
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

        HOF[player] = (link)

    HOFplayernames.append(player)

for x in HOF:

    url = ("http://www.metmuseum.org/collection/the-collection-online/search?&noqs=true&ao=on&what=Baseball+cards&pg=1&ft="+str(x))

    result_page = requests.get(url)
    if result_page.status_code != 200:
        uprint("oops, this one's no good: ", url)
        time.sleep(0.01)

    result_html = result_page.text

    soup = BeautifulSoup(result_html, "html.parser")


    # item_container = soup.find_all("div", attrs = {"class" : "list-view-object-info"})
    #
    # for list_item in item_container:
    #
    #     item_name = list_item.find_all("a")
    #
    #     for name in item_name:
    #
    #         metlink = name["href"]
    #
    #         try:
    #             HOF[player].append(metlink)
    #
    #         except:

    no_results = soup.find_all("div", attrs = {"class" : "no-results"})

    for result in no_results:

        no_player = result.find_all("span", attrs = {"class" : "no-results-searchterm"})

        for player in no_player:

            not_in_met.append(player.text)


#This doesn't quite work. It appends all of the links to the first player that it finds, which
#is Honus Wagner. I think maybe trying to do this in one script is ambitious. Make another one
#that gets the names and Metlinks, and then merge them.
    # else:
    #

#
HOFcopy = HOF.copy()

for guy in HOFcopy:

    if guy in not_in_met:

        del HOF[guy]

    if guy not in not_in_met:

        HOFinMET[guy] =[]

# writer = csv.writer(open('bbrlinks.csv', 'w'))
#
# # for key, value in HOF.items():
#      writer.writerow([key, value])

HOFinMETcopy = HOFinMET.copy()

for guy in HOFinMETcopy:

    url = ("http://www.metmuseum.org/collection/the-collection-online/search?&noqs=true&ao=on&what=Baseball+cards&pg=1&ft="+str(guy))

    result_page = requests.get(url)
    if result_page.status_code != 200:
        uprint("oops, this one's no good: ", url)
        time.sleep(0.01)

    result_html = result_page.text

    soup = BeautifulSoup(result_html, "html.parser")


    item_container = soup.find_all("div", attrs = {"class" : "list-view-thumbnail"})

    for list_item in item_container:

        item_name = list_item.find_all("a")

        for name in item_name:

            # metlink = []
            #
            # metlink.append(name["href"])

            if name["href"] not in HOFinMET:

                HOFinMET[guy] = (name["href"])

playerpages = { k: [ HOF[k], HOFinMET[k] ] for k in HOF }

write = csv.writer(open('playerpages.csv', 'w'))

for key, value in playerpages.items():
     write.writerow([key, value])



#
#
# # uprint(HOF)
# # uprint(len(HOF))
#
#
#     # item_container = soup.find_all("div", attrs = {"class" : "list-view-object-info"})
#     #
#     # for list_item in item_container:
#     #
#     #     item_name = list_item.find_all("a")
#     #
#     #     for name in item_name:
#     #
#     #         metlink = name["href"]
