from bs4 import BeautifulSoup
import requests
from time import sleep
import sys
import csv

def statscraper(player):

    this_player = {}
    tracked_stats = []
    indiv_stats = []

    batting_table = player.find_all("table", attrs = {"id" : "batting_standard"})

    for career_table in batting_table:

        career_stats = career_table.find_all("tfoot")

        for stat_names in career_stats:

            names = stat_names.find_all("tr", attrs = {"class" : "thead"})

            for a_name in names:

                onestat = a_name.find_all("th")

                for a_stat in onestat:

                    stat_item = a_stat.text

                    tracked_stats.append(stat_item)

        for stats in career_stats:

            statnumbers = stats.find_all("tr", attrs = {"class" : "stat_total"})

            for number in statnumbers:

                a_number = number.find_all("td")

                for num in a_number:

                    stat_num = num.text

                    indiv_stats.append(stat_num)

                    this_player = dict(zip(tracked_stats, indiv_stats))

    return(this_player)

def pitchscraper(player):

    this_player = {}
    tracked_stats = []
    indiv_stats = []

    batting_table = player.find_all("table", attrs = {"id" : "pitching_standard"})

    for career_table in batting_table:

        career_stats = career_table.find_all("tfoot")

        for stat_names in career_stats:

            names = stat_names.find_all("tr", attrs = {"class" : "thead"})

            for a_name in names:

                onestat = a_name.find_all("th")

                for a_stat in onestat:

                    stat_item = a_stat.text

                    tracked_stats.append(stat_item)

        for stats in career_stats:

            statnumbers = stats.find_all("tr", attrs = {"class" : "stat_total"})

            for number in statnumbers:

                a_number = number.find_all("td")

                for num in a_number:

                    stat_num = num.text

                    indiv_stats.append(stat_num)

                    this_player = dict(zip(tracked_stats, indiv_stats))

    return(this_player)
