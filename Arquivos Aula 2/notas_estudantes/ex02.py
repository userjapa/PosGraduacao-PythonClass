file_ref = open('../notas_estudantes.dat', 'r')

students = dict()

for line in file_ref:
    arr = line.split()
    name = arr[0]
    arr.pop(0)
    arr_int = list(map(int, arr))
    print(f'{name} - MAX: {max(arr_int)} | MIN: {min(arr_int)}')

file_ref.close()
