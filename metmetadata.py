from bs4 import BeautifulSoup
import requests
import json
import time
import csv
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

all_cards = []


with open("HOFinMET.csv", "r") as m:

    reader = csv.reader(m)

    for row in reader:

        url = ("http://www.metmuseum.org"+(row[1]))

        result_page = requests.get(url)
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

            player_name = "no name"
            year_stats = "no stats"
            title = "no title"
            publisher = "no publisher"
            date = "no date"
            medium = "no_medium"
            dimensions = "no dimensions"
            classifications = "no classification"
            credit_line = "no credit_line"
            accession_number = "no accession_number"


            #check if it has the 10 metadata fields
            if len(meta_div) > 0:
                #loop through for text inside the div
                for a_div in meta_div:
                    all_text = a_div.text

                    #keyword check to identify data field
                    if 'Publisher:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        maker = all_text.replace('Maker:' , '')


                    #keyword check to identify data field
                    if 'Date:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        date = all_text.replace('Date:' , '')

                    #keyword check to identify data field
                    if 'Medium:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        medium = all_text.replace('Medium:' , '')

                    #keyword check to identify data field
                    if 'Dimensions:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        dimensions = all_text.replace('Dimensions:' , '')

                    #keyword check to identify data field
                    if 'Classifications:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        classifications = all_text.replace('Classifications:' , '')

                    #keyword check to identify data field
                    if 'Credit Line:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        credit_line = all_text.replace('Credit Line:' , '')


                    #keyword check to identify data field
                    if 'Accession Number:' in all_text:
                        #create the variable for that field
                        #find/replace for the 'label' span, then trim white space
                        accession_number = all_text.replace('Accession Number:' , '')


                #create / define a dictionary
                this_card = {}

                #all the fields as dictionary keys, with the variables from above

                this_card['player_name'] = player_name
                this_card['year_stats'] = year_stats
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
