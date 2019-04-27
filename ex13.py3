words = ['abc', 'defg', 'hijkl', 'lmnopq']

def most_char(list):
	bigger = ''
	for item in list:
		if len(bigger) < len(item):
			bigger = item
	return bigger

print(most_char(words))

def char_avg(list):
	letters = 0
	for item in list:
		for letter in item:
			if letter not in ['a', 'b', 'c', 'd', 'e']:
				letters+=1
	return letters/len(list)

print(char_avg(words))

def count_first(list):
	return list.count(list[0])

print(count_first(words))

def count_compost(list):
	count = 0
	for item in list:
		if '-' in item:
			count+=1
	return count

print(count_compost(words))

def count_same_neighborhood(list):
	same_count = 0
	for item in list:
		same_count+=(list.count(item) - 1)
	return same_count

print(count_same_neighborhood(words))