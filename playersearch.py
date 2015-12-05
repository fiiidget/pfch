import csv

players_in_the_hall = []

with open("HOFplayers.csv", "r") as bb:
    reader = csv.reader(bb)

    for row in reader:

        if "Player" in row[4]:
            players_in_the_hall.append(row[1])

print(players_in_the_hall)
