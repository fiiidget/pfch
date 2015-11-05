from bs4 import BeautifulSoup
import requests
import csv

playerdata = {}

url = "http://www.baseball-reference.com/players/w/wagneho01.shtml"

statistics = requests.get(url)

if statistics.status_code != 200:
    print("BROKEN")

stat_html = (statistics.text)

stat_html = stat_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(stat_html, "html.parser")

player_stats = soup.find("table", attrs = {"class" : "sortable stats_table row_summable"})

for a_stats in player_stats:

    career = a_stats.find("tfoot"

    print(career.text)

    # for career_stats in career:
    #
    #     numbs = career_stats.find("tr", attrs = {"data-row" : "24"})
    #
    #     print(numbs)
