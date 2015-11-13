from bs4 import BeautifulSoup
import requests
import sys
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

playerdata = {}

url = "http://www.baseball-reference.com/players/w/wagneho01.shtml"

statistics = requests.get(url)

if statistics.status_code != 200:
    print("BROKEN")

stat_html = (statistics.text)

# stat_html = stat_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(stat_html, "html.parser")

player_stats = soup.find("table", attrs = {"class" : "sortable stats_table row_summable"})

uprint(player_stats.text)
