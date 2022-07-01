
import json



with open('./example.json', 'r', encoding='utf8') as f: 
 string = f.read()

data = json.loads(string)

with open('example-extraction.txt', 'w') as d:
 for element in data:  # iterate on each element of the list
   
    d.write('Name: \n' + element['name'])  # print it
    d.write('\n')
    d.write('\n')
    description = ""
    if(element['description'] != ""):
     description = element['description'].replace('\u200b', '')
    d.write('Description: \n' + description)
    d.write('\n')
    d.write('_' * 120)
    d.write('\n')
    
  
print(len(data))