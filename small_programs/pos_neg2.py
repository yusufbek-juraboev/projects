pos = []
neg = []

with open("input.txt", "r") as file_i:
  with open('output1.txt', 'w') as file_o1:
    with open('output2.txt', 'w') as file_o2:
      
      for numbers in file_i:
        numbers = numbers.split(',')
        
        for num in numbers:
          
          if int(num) > 0:
            pos.append(num)
           
          if int(num) < 0:
            neg.append(num)
            
      file_o1.write(','.join(pos))
      file_o2.write(','.join(neg))


print("Done!")