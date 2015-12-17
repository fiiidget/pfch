from bs4 import BeautifulSoup
import requests
from time import sleep
import sys
import csv

all_players = []
tracked_stats = []
this_player = {}
indiv_stats = []

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

url = ("http://baseball-reference.com/players/v/vanceda01.shtml")

result_page = requests.get(url)
if result_page.status_code != 200:
    uprint("oops, this one's no good: ", url)

result_html = result_page.text

soup = BeautifulSoup(result_html, "html.parser")

batting_table = soup.find_all("table", attrs = {"id" : "batting_standard"})

for career_table in batting_table:

    career_stats = career_table.find_all("tfoot")

    for stat_names in career_stats:

        names = stat_names.find_all("tr", attrs = {"class" : "thead"})

        for a_name in names:

            onestat = a_name.find_all("th")

            for a_stat in onestat:

                stat_item = a_stat.text

                tracked_stats.append(stat_item)

with open("playerpages_cleanedup.csv", "r") as m:

    reader = csv.reader(m)

    for row in reader:

        url = ("http://baseball-reference.com"+str(row[1]))

        result_page = requests.get(url)
        if result_page.status_code != 200:
            uprint("oops, this one's no good: ", url)

        result_html = result_page.text

        soup = BeautifulSoup(result_html, "html.parser")

        batting_table = soup.find_all("table", attrs = {"id" : "batting_standard"})

        for career_table in batting_table:

            career_stats = career_table.find_all("tfoot")

            for stats in career_stats:

                statnumbers = stats.find_all("tr", attrs = {"class" : "stat_total"})

                for number in statnumbers:

                    a_number = number.find_all("td")

                    for num in a_number:

                        stat_num = num.text

                        indiv_stats.append(stat_num)

        this_player = {}

        this_player = dict(zip(tracked_stats, indiv_stats))

        all_players.append(this_player) #this does it, but it prints the same stats to each one.

uprint(all_players)
