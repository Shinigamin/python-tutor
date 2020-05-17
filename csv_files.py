import csv


fieldnames = ['card_type', 'name', 'effect']

with open('monster_cards.csv') as fp:
    reader = csv.DictReader(fp, fieldnames=fieldnames)
    for row in reader:
        print(row)
