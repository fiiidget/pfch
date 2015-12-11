from bs4 import BeautifulSoup
import requests
from pfchfunctions import cardlist
import time
import sys
import csv

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

MET = {}
card_titles = []
card_links = []

pages = range (0, 76, 1)
for x in pages:

    url = ("http://www.metmuseum.org/collection/the-collection-online/search?rpp=90&ao=on&ft=baseball+cards&pg="+str(x))

    result_page = requests.get(url)
    if result_page.status_code != 200:
        uprint("oops, this one's no good: ", url)
        time.sleep(0.2)

    result_html = result_page.text

    soup = BeautifulSoup(result_html, "html.parser")

    item_container = soup.find_all("div", attrs = {"class" : "list-view-object-info"})

    for list_item in item_container:

        item_name = list_item.find_all("div", attrs = {"class" : "objtitle"})

        for name in item_name:

            card_titles.append(name.text)

        item_link = list_item.find_all("a")

        for link in item_link:

            card_links.append(link["href"])

MET = dict(zip(card_titles, card_links))

writer = csv.writer(open('METdict.csv', 'w'))

for key, value in MET.items():
     writer.writerow([key, value])
