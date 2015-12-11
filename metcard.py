from bs4 import BeautifulSoup
import requests
from pfchfunctions import cardlist
from time import sleep
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

MET = {}
METcardimg = []
METcardnext = []
METcardtext = []

cardpages = ["/collection/the-collection-online/search/413556?pos=1&rpp=90&pg=1&ao=on&ft=baseball+cards"]
counter = 0

while (counter < 2):

    for y in cardpages:

        url = ("http://www.metmuseum.org"+str(y))

# url = ('http://www.metmuseum.org/collection/the-collection-online/search/413556?pos=1&rpp=90&pg=1&ao=on&ft=baseball+cards')

        MET_page = requests.get(url)

        if MET_page.status_code != 200:
            print ("there was an error with", url)


        met_html = MET_page.text

        soup = BeautifulSoup(met_html, "html.parser")

        METtitle = soup.find_all("div", attrs = {"class" : "tombstone-container"})

        for container in METtitle:
            card_info = container.find_all("h2")
            next_link = container.find_all("a", attrs = {"class" : "next"})

        for title in card_info:
            if title not in METcardtext:
                METcardtext.append(title.text)

        for link in next_link:
            if link not in METcardnext:
                METcardnext.append(link["href"])



uprint(METcardtext)
uprint(METcardnext)
