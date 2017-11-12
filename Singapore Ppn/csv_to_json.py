import csv
import json

try:
	csvfile = open('singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv')
except csv.Error as e:
	print e

data = {
	"age_structure": [
	]
}

def addRowToCSV(row):
	data["age_structure"].append({})
	data["age_structure"][-1]["year"] = int(row[0])
	data["age_structure"][-1]["resident_type"] = row[1]
	if 'Years & Over' in row[2]:
		row[2] = row[2].replace(' Years & Over', '+')
	else:
		row[2] = row[2].replace(' Years', '')
	data["age_structure"][-1]["age_group"] = row[2]
	data["age_structure"][-1]["cnt"] = int(row[3])

agesToIgnore = ['65 Years & Over', '70 Years & Over', '75 Years & Over', '80 Years & Over']
content = csv.reader(csvfile)
next(content)
for row in content:
	if int(row[0])>=1990 and row[2] not in agesToIgnore:
		addRowToCSV(row)
csvfile.close()

jsonfile = open('sgData.js', 'w')
jsonfile.write('var data=\n')
json.dump(data, jsonfile, indent=4)
jsonfile.close()

# sample = {
# 	"age_structure": [
# 		{
# 			"year": 1990,
# 			"person_group": [
# 				{
# 					"group": "all",
# 					"age_group": [
# 						{
# 							"age": "0 - 4 Years",
# 							"cnt": 1000
# 						},
# 						{
# 							"age": "5 - 8 Years",
# 							"cnt": 1200
# 						}
# 					]
# 				}
# 			]
# 		},
# 		{
# 			"year": 1980,
# 			"person_group": [
# 				{
# 					"group": "all",
# 					"age_group": [
# 						{
# 							"age": "0 - 4 Years",
# 							"cnt": 200
# 						},
# 						{
# 							"age": "5 - 8 Years",
# 							"cnt": 300
# 						}
# 					]
# 				}
# 			]
# 		}
# 	]
# }