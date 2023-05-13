import time
import itertools

start_time = time.time()

a = ["A", "B", "C", "D", "E"]

# Product
comb = itertools.product(a, repeat=5)
combinations = set()
for data in comb:
	combinations.add("".join(data))

lst = list(combinations)
for data in lst:
	for i in a:
		if data.count(i) > 3:
			combinations.discard(data)
print(combinations)



print("Well done!")
print("--- %s seconds ---" % (time.time() - start_time))