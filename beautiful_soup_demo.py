
#we want to load the beautiful soup module that we installed so we can use it in our script
#the module is named bs4 and it has multiple parts, but we just want to use the BeautifulSoup part
from bs4 import BeautifulSoup

#we also want to have a way to talk to the internet so we need the request module too
import requests

#here is the URL to the browse painting pages
url = "http://collections.frick.org/view/objects/asimages/152"

#lets ask requests to get that page
painting_page = requests.get(url)

#just let us know if that failed
if painting_page.status_code != 200:
	print ("There was an error with", url)

#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
page_html = painting_page.text

#now we are going to ask BS to parse the page
soup = BeautifulSoup(page_html, "html.parser")

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

#now we can "query" the soup variable for the paterns we are looking for
all_links = soup.find_all("a", attrs = {"class": "titleLink"})

for a_link in all_links:

	#print out the url of each link and the text
	print(a_link.text)
	print(a_link['href'])



#find all the spans with class titleCell
all_title_cells = soup.find_all("span", attrs = {"class": "titleCell"})

for a_title_cell in all_title_cells:

	artist = a_title_cell.find("span", attrs = {"class": "imageArtist"})

	#now we have the arist span, we just want the text of the link so do another find
	print (artist.find("a").text)

	#lets get the title of the work
	title = a_title_cell.find("a", attrs = {"class": "titleLink"})

	#if it is not found None is returned so lets make sure we found something
	if title != None:
		print (title.text)

#lets find the "Next" link
next_link = soup.find("a",text="Next")

print ("The next page is:")
print (next_link)
