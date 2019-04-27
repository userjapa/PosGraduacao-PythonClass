multiples = list()

for num in range(50):
	num+=1
	if num % 3 == 0:
		multiples.insert(0, num)

multiples.sort()
print(multiples)