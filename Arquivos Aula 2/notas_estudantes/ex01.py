file_ref = open('../notas_estudantes.dat', 'r')

students = dict()

for line in file_ref:
    arr = line.split()
    name = arr[0]
    arr.pop(0)
    if len(arr) > 6:
        print(name)

file_ref.close()
