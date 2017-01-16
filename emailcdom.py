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
    emails=""
    for row in spamreader:
        print(','.join(row))
        email=row[1].lower().replace (" ", "-")+'@'+row[0]+'.medecin.fr;'
        print(email)
        emails+=email
print(emails)
emailsfile = open("mailcdom.txt", "w")
emailsfile.write(emails)
emailsfile.close()
