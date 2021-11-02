import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    json_array = []
    
    # read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:

        # load csv file data
        csv_reader = csv.DictReader(csvf, delimiter=';')

        # convert each row into python dict
        for row in csv_reader:
            json_array.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)


csv_file_path = r'%file_path%'
json_file_path = r'%file_path%'

csv_to_json(csv_file_path, json_file_path)