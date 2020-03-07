import json
import csv

### [open] will open a *.csv file that will be broken down in this function to be written as a JSON encoded file
with open('**/*.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='')
    #TODO (rpaglinawan): Add table delimeter when parsing csv files
    for row in reader:
        print(', '.join(row))
    #TODO (rpaglinawan): Add data delimeter to fill in table