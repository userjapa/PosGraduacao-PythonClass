list = [5,7,2,9,4,1,3]
print(f'Length: {len(list)}')
list.sort(reverse=True)
print(f'Max: {max(list)}')
print(f'Min: {min(list)}')
print(f'Sum: {sum(list)}')
list.sort()
print(f'Asc: {list}')
list.sort(reverse=True)
print(f'Desc: {list}')