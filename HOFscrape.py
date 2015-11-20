from bs4 import BeautifulSoup
import requests
#from pfchfunctions import cardlist
from time import sleep
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

HOFplayernames = []
HOFplayerpages = []

url = ('http://www.baseball-reference.com/awards/hof.shtml')

HOF_page = requests.get(url)

if HOF_page.status_code != 200:
    print ("there was an error with", url)


page_html = HOF_page.text

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

player_names = soup.find_all("tr", attrs = {"class" : "0"})

#for a_player in player_names:
uprint(player_names)
