list_one = [1,2,3]
list_two = [3,4,5,6]
def join_lists(list1=[], list2=[]):
	return list1 + list2

print(join_lists(list_one, list_two))

def get_intersection(list1=[], list2=[]):
	intersection = []
	for item in list1:
		if item in list2:
			intersection.insert(0, item)
	print(intersection)
	
get_intersection(list_one, list_two)

def show_lists_items(list1=[], list2=[]):
	len1, len2 = len(list1), len(list2)
	length = len1 if len1 > len2 else len2
	index = 0
	while index < length:
		if (index < len1):
			print(f'List 1, item {index + 1}: {list1[index]}')
		if (index < len2):
			print(f'List 2, item {index + 1}: {list2[index]}')
		index+=1

show_lists_items(list_one, list_two)