import json, os
from time import *

try:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/items.json") as file:
        items = json.load(file)

        input = input("Insert skin name: ").lower()
        found = False
        results = []

        for item in items['items']:
            if input in item['name'].lower(): 
                results.append([item['sku'],item['id']])
                found = True

        if found == False:
            print('Item not found!')
        elif found == True:
            results.sort()
            if len(results) == 1:
                print('<<<',len(results), 'RESULT FOUND >>>')
            else:
                print('<<<',len(results), 'RESULTS FOUND >>>')
            for result in results:
                print(result[1], ':', result[0])
except FileNotFoundError:
    print("items.json file does not exist! Run update.py!")
sleep(120)
