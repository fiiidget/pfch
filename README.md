# pfch
This repository of scripts and corresponding JSON dictionary was created as a part of Matt Miller's Programming for Cultural Heritage class at Pratt School of Information, Fall 2015. It utlizes the Metropolitan Museum of Art's online collections and the statistics site baseball-reference.com.

Major League Baseball has inducted 310 people into the National Baseball Hall of Fame, dating back to the Hall’s first class of inductees in 1936. The members of the Hall of Fame (HOF) include iconic American figures, such as Babe Ruth and Joe DiMaggio, familiar even to non-baseball fans. Additionally the Metropolitan Museum of Art has an online collection of over 410,000 items. More than 10,000 of those items have the “Object Type: baseball cards.” Of those 10,313 records, 6,680 of them have an image as a part of their online collection record. What this project aims to do is to connect those images, often artistic renderings of baseball’s earliest stars, with the official player statistics for the 310 people in the Hall of Fame, essentially filling in the “back of the baseball card” for these items that fill an interesting niche in the area between sport, art and Americana. 

Visualization available at: (place)

JSON last updated 12/17/15

Next HOF inductee announcement: (date)

The hofmet.py script creates a csv file of the major league players and managers that are both in the Baseball Hall of Fame, and have their cards in the Met's online collection. The csv file, playerpages.csv contains the player's name, and links to their baseball-reference.com site, and their item page at the Met. Scripts going forward use a cleaned up versions of this csv, playerpages_cleanedup.csv

The metmetadata.py script then takes those links and extracts metadata about each player and turns it into JSON, using the statscraper function in bbtables.py to get the career player stats from baseball-reference.com, and Beautiful Soup to scrape the metadata from the Met's online collection. 
