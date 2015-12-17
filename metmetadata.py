from bs4 import BeautifulSoup
import requests
import json
import time
import csv
import sys
import brscraper

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

all_cards = []
careerstats = []

with open("playerpages_cleanedup.csv", "r") as m:

    reader = csv.reader(m)

    for row in reader:

        url = ("http://baseball-reference.com"+(row[1]))

        result_page = requests.get(url)
        if result_page.status_code != 200:
            uprint("oops, this one's no good: ", url)
            time.sleep(0.01)

        result_html = result_page.text

        soup = BeautifulSoup(result_html, "html.parser")

        player_position = soup.find_all("span", attrs = {"itemprop" : "role"})

        for position in player_position:

            postest = position.text


            if "Pitcher" in postest:

                scraper = brscraper.BRScraper()
                data = scraper.parse_tables(str(row[1]))


                pitching = (data)
                # total_pitching = (pitching["stat_total"])

                careerstats.append(pitching)


            if "Pitcher" not in postest:

                scraper = brscraper.BRScraper()
                data = scraper.parse_tables(str(row[1]))


                batting = (data)
                # total_batting = (batting["stat_total"])



                careerstats.append(batting)

        secondurl = ("http://www.metmuseum.org"+(row[2]))

        result_page = requests.get(secondurl)
        if result_page.status_code != 200:
            uprint("oops, this one's no good: ", url)
            time.sleep(0.01)

        result_html = result_page.text

        soup = BeautifulSoup(result_html, "html.parser")

        title_container = soup.find_all("div", attrs = {"class" : "tombstone-container"})

        for card_title in title_container:

            heading = card_title.find_all("h2")

            for words in heading:

                titled = words.text

        card_container = soup.find_all("div", attrs = {"id" : "inner-image-container"})

        for card_image in card_container:

            card = card_image.find_all("img")

            for picture in card:

                cardpic = picture["src"]

        all_meta = soup.find_all("div", attrs = {"class": "tombstone"})

        for a_meta in all_meta:

            meta_div = a_meta.find_all("div")

            player_name = str(row[0])
            career_stats = careerstats
            bbr_page = "http://baseball-reference.com"+str(row[1])
            #name, year stats and bbr page will be added from elsewhere.
            title = "no title"
            publisher = "no publisher"
            date = "no date"
            medium = "no_medium"
            dimensions = "no dimensions"
            classifications = "no classification"
            credit_line = "no credit_line"
            accession_number = "no accession_number"



            if len(meta_div) > 0:
                #loop through for text inside the div
                for a_div in meta_div:
                    all_text = a_div.text

                    #keyword check to identify data field
                    if 'Publisher:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        publisher = all_text.replace('Publisher:' , '').strip()


                    #keyword check to identify data field
                    if 'Date:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        date = all_text.replace('Date:' , '').strip()

                    #keyword check to identify data field
                    if 'Medium:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        medium = all_text.replace('Medium:' , '').strip()

                    #keyword check to identify data field
                    if 'Dimensions:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        dimensions = all_text.replace('Dimensions:' , '').strip()

                    #keyword check to identify data field
                    if 'Classifications:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        classifications = all_text.replace('Classifications:' , '').strip()

                    #keyword check to identify data field
                    if 'Credit Line:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        credit_line = all_text.replace('Credit Line:' , '').strip()


                    #keyword check to identify data field
                    if 'Accession Number:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        accession_number = all_text.replace('Accession Number:' , '').strip()


                this_card = {}

                #all the fields as dictionary keys, with the variables from above

                this_card['player_name'] = player_name
                this_card['career_stats'] = career_stats
                this_card['bbr_page'] = bbr_page
                this_card['title'] = titled
                this_card['publisher'] = publisher
                this_card['date'] = date
                this_card['medium'] = medium
                this_card['dimensions'] = dimensions
                this_card['classifications'] = classifications
                this_card['credit_line'] = credit_line
                this_card['accession_number'] = accession_number
                this_card['img_url'] = cardpic




                #add it to the list created above or return message
                all_cards.append(this_card)

                with open('scraped_metcards.json', 'w') as f:
                    f.write(json.dumps(all_cards, indent=4))


            else:
                uprint ("this one is no good")
                continue
