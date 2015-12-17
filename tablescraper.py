import brscraper
import csv
from bs4 import BeautifulSoup
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

with open("playerpages_cleanedup.csv", "r") as m:

    reader = csv.reader(m)

    for row in reader:

        url = ("http://baseball-reference.com"+str(row[1]))

        result_page = requests.get(url)
        if result_page.status_code != 200:
            uprint("oops, this one's no good: ", url)

        result_html = result_page.text

        soup = BeautifulSoup(result_html, "html.parser")

        player_position = soup.find_all("span", attrs = {"itemprop" : "role"})

        for position in player_position:

            postest = position.text

            if "Pitcher" in postest:



# with open("playerpages_cleanedup.csv", "r") as bbrlinks:
#
#     reader = csv.reader(bbrlinks)
#
#     for row in reader:

                scraper = brscraper.BRScraper()
                data = scraper.parse_tables(str(row[1]))


                pitching = (data["pitching_standard"])


            else:

                scraper = brscraper.BRScraper()
                data = scraper.parse_tables(str(row[1]))

                batting = (data["batting_standard"])

            elif:
                continue
