import csv
import json

naughty = 0;
nice = 0;
just_the_naughty = []
just_the_nice = []

# Parsing naughty and nice list as csv
# saving all the naugties in memory
naughty_file = open("Naughty and Nice List.csv", 'r')
naughty_csv = csv.reader(naughty_file)

for line in naughty_csv:
	if line[1] == "Naughty":
		just_the_naughty.append(line[0])
	else:
		just_the_nice.append(line[0])

# Parsing JSON file
json_file = open("infractions.json", 'r')
json_data = json.load(json_file)
json_file.close()

for person in json_data["infractions"]:
	if person["name"] in just_the_naughty:
		print("Naughty: {}\t\t Coal: {}".format(person["name"], len(person["coals"])))
	elif person["name"] in just_the_nice:
		print("Nice: {}\t\t Coal: {}".format(person["name"], len(person["coals"])))
