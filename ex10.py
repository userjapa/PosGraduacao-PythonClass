def compare_lists(list1, list2):
	list1.sort()
	list2.sort()
	return list1 == list2

print(compare_lists([1,2], [2,1]))