import csv
import json
import sys
if(len(sys.argv) != 3):
    print("Enter 2 arguments, first a csv file, second a json file")
csv_file_name = sys.argv[1]
json_file_name = sys.argv[2]
official_name_data = []
non_official_names = []
try:
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter = ',')
        for row in csv_reader:
            if (len(row[0].split(' ')) == 1) or (row[0] == row[0].lower()):
                non_official_names.append(row[0])
                continue
            names = row[0].split(' ')
            is_alpha = 1
            for name in names:
                if(name != '' and name.isalpha() == False):
                    is_alpha = 0
                    break
            if is_alpha == 0:
                non_official_names.append(row[0])
            else:
                official_name_data.append(row)
except:
    print('Enter correct csv file as first argument and json file as second argument')
    sys.exit()

json_data= []
try:
    with open(json_file_name) as json_file:
        data = json.load(json_file)
        for entry in data:
            json_data.append(entry)
except:
    print('Enter correct csv file as first argument and json file as second argument')
    sys.exit()

required_data = []
for single_entry in official_name_data:
    for entry in json_data:
        if(single_entry[0] == entry['n']):
            required_data.append([entry['n'],entry['i'],entry['d'],single_entry[1],single_entry[2]])

if len(non_official_names) == 0:
    print('No non official name found')
else:
    print('The non official names are: ')
    for name in non_official_names:
        print(name)

if len(required_data) == 0:
    print('\nNo common entries')
else: 
    print('\nThe common entries are: ')
    for entry in required_data:
        print(', '.join(entry))
