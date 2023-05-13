with open("input.txt", "r") as file_i:
  with open('output.txt', 'w') as file_o:
    for word in file_i:
      a = word.lower().count('a')
      o = word.lower().count('o')
      x = a * o
      file_o.write(str(x))


print("Done!")