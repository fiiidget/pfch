from bs4 import BeautifulSoup
import requests

card_images = []

url = "http://www.metmuseum.org/collection/the-collection-online/search/413556?pos=3&rpp=90&pg=1&ao=on&ft=baseball+cards"

baseballcard = requests.get(url)

if baseballcard.status_code != 200:
    print("Uh-Oh, the page is messed up")

page_html = (baseballcard.text)

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

player_image = soup.find_all("div", attrs = {"id" : "inner-image-container"})

for a_image in player_image:

    cardimg = soup.find_all("img")

    for card in cardimg:

        print(card["alt"])
        print(card["src"])
