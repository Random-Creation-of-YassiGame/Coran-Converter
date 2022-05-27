import json

with open("../data/files/dictionnary.json", 'r') as outfile:  # open the file
    encoder = json.load(outfile)