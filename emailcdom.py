import csv
from unidecode import unidecode
open("toascii", 'a').close()
def toascii():
    with open(r'departments_regions_france_2016.csv', 'r', encoding='utf8') as origfile, open(r'toascii', 'w', encoding='ascii') as convertfile:
        for line in origfile:
            line = unidecode(line)
            convertfile.write(line)
toascii()
with open('toascii', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        email=row[1].lower().replace (" ", "-")+'@'+row[0]+'.medecin.fr;'
        emails+=email
emailsfile = open("mailcdom.txt", "w")
emailsfile.write(emails)
emailsfile.close()
