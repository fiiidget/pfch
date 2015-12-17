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

card_pictures = []

with open("HOFinMET.csv", "r") as m:

    reader = csv.reader(m)

    # readercopy = reader.copy()

    # for row in reader:
    #
    #     try:
    #         page_url = str(row[1])
    #
    #     except:
    #         reader.remove(row)

    for row in reader:

        url = ("http://www.metmuseum.org"+(row[1]))

        result_page = requests.get(url)
        if result_page.status_code != 200:
            uprint("oops, this one's no good: ", url)
            time.sleep(0.01)

        result_html = result_page.text

        soup = BeautifulSoup(result_html, "html.parser")

        card_container = soup.find_all("div", attrs = {"id" : "inner-image-container"})


        for card_image in card_container:

            card = card_image.find_all("img")

            for pic in card:

                card_pictures.append(pic["src"])

for arow in card_pictures:

    with open("metimages2.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(str(arow))
# uprint(card_pictures)
