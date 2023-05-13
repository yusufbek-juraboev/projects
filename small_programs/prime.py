from math import sqrt


def isprime(num):
  n = sqrt(num)
  if num == 2 or num == 3:
    return True
  for i in range(2, int(n)+1):
    if num%i==0:
      return False
    else:
      return True


with open("input.txt", "r") as file_i:
  with open('output.txt', 'w') as file_o:
    for number in file_i:
      file_o.write(str(isprime(int(number))))

print("Done!")