from bs4 import BeautifulSoup
import requests

cards = {}
card_images = []
card_alt_text = []

url = "http://www.metmuseum.org/collection/the-collection-online/search/413556?pos=3&rpp=90&pg=1&ao=on&ft=baseball+cards"

baseballcard = requests.get(url)

if baseballcard.status_code != 200:
    print("Uh-Oh, the page is messed up")

page_html = (baseballcard.text)

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

player_image = soup.find_all("div", attrs = {"id" : "inner-image-container"})

for a_image in player_image:

    cardimg = a_image.find("img")

    # for card in cardimg:
    #
    #     print(card["alt"])
    #     print(card["src"])

    Alt_text = cardimg["alt"]
    Image_file = cardimg["src"]

    if Alt_text not  in card_alt_text:
        card_alt_text.append("alt")

    if Image_file not in card_images:
        card_images.append("src")

print(Alt_text)
print(Image_file)

def cardlist(listo):
    totalcards = len(listo)

    answer = ("you have " + str(totalcards) + " items in your " + str(listo) + " list")
    return answer

number_of_cards = cardlist(card_images)
numbers_of_descriptions = cardlist(card_alt_text)
print(number_of_cards)
print(numbers_of_descriptions)
