from bs4 import BeautifulSoup
import requests
from pfchfunctions import cardlist
from time import sleep

cardpages = ["/collection/the-collection-online/search/413556?pos=1&rpp=90&pg=1&ao=on&ft=baseball+cards"]
cards = {}
card_images = ["images"]
card_alt_text = ["alt text"]

# ---collecting the pages----
counter = 0

while (counter < 11):

    for y in cardpages:

        url = "http://www.metmuseum.org"+str(y)

        baseballcard = requests.get(url)
        sleep(10)
        if baseballcard.status_code != 200:
            print("Uh-Oh, the page is messed up")


        page_html = (baseballcard.text)

        page_html = page_html.encode('ascii', 'ignore').decode('ascii')

        soup = BeautifulSoup(page_html, "html.parser")

        next_link = soup.find("a", attrs = {"class" : "next"})

        if next_link["href"] not in cardpages:
            cardpages.append(next_link["href"])
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
