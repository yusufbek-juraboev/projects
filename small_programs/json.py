import json


output = []
with open("input.txt", "r") as file_i:
  with open('output.txt', 'w') as file_o:
    
    data = json.load(file_i)
    
    for k in data.keys():
      output.append(type(data[k]).__name__)
      
    file_o.write(','.join(output))

print("Done!")