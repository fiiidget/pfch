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

cardpages = ["/collection/the-collection-online/search/413556?pos=1&rpp=90&pg=1&ao=on&ft=baseball+cards"]
cards = {}
card_images = ["images"]
card_alt_text = ["alt text"]

# ---collecting the pages----
counter = 0

while (counter < 2):

    for y in cardpages:

        url = ("http://www.metmuseum.org"+str(y))

        baseballcard = requests.get(url)
        sleep(1)
        if baseballcard.status_code != 200:
            print("Uh-Oh, the page is messed up")


        page_html = (baseballcard.text)

        soup = BeautifulSoup(page_html, "html.parser")

        next_link = soup.find("div", attrs = {"class" : "tombstone-container"})

        for link in next_link:

            # a_link = link["href"]

            if link not in cardpages:
                cardpages.append(link["href"])
        counter = counter + 1
#
print(cardpages)

#         # # ----getting the info out of the pages----
#         # for x in cardpages:
#         #     url = "http://www.metmuseum.org"+str(x)
#         player_image = soup.find_all("div", attrs = {"id" : "inner-image-container"})
#
#         for a_image in player_image:
#
#             cardimg = a_image.find("img")
#
#             Alt_text = cardimg["alt"]
#             Image_file = cardimg["src"]
#
#             if Alt_text not in card_alt_text:
#                 card_alt_text.append(Alt_text)
#
#             if Image_file not in card_images:
#                 card_images.append(Image_file)
#
#
#
#
#
#
# # print(Alt_text)
# # print(Image_file)
# print(cardlist(card_images))
# print(cardlist(card_alt_text))
# # print(cardpages)
# print(cardlist(cardpages))
# # print(card_images)
