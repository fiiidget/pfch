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

with open(bbrlinks.csv, "r") as bbrlinks:

    reader = csv.reader(bbrlinks)

    for row in reader:


        scraper = brscraper.BRScraper()
        data = scraper.parse_tables(row[1])

        print(float(data["batting_standard"][23]["HR"]))
