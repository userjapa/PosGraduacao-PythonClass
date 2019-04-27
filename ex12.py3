def calc_tree_grow(high, grow_year, years):
	for y in range(years):
		high+=grow_year
	print(f"It'll be {high} meters in {years} years")

calc_tree_grow(1, 1, 5)