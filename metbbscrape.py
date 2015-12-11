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

url = ("http://www.metmuseum.org/collection/the-collection-online/search?rpp=90&pg=1&ao=on&ft=baseball+cards")

result_page = requests.get(url)
result_html = result_page.text

soup = BeautifulSoup(result_html, "html.parser")
