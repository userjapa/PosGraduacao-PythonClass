def convert_mb(value):
    return round(value / 1000000, 2)

def get_percent(value, total):
    return round((value * 100) / total, 2)

def generate_file(file_path):
    users = dict()
    file_ref = open(file_path, 'r')
    for line in file_ref:
        arr = line.split()
        users[arr[0]] = int(arr[1])

    file_ref.close()

    result_ref = open('fab-result.txt', 'w')
    result_ref.write('ACME Inc.   Uso do espaco em disco pelos usuarios\n')
    result_ref.write('-------------------------------------------------\n')
    result_ref.write('Nr.     Name         Espaço utilizado      % do uso\n')
    for k,v in users.items():
        result_ref.write(f'{(list(users.keys()).index(k) + 3):<7} {k:<15} {convert_mb(v):>10} MB {get_percent(v, sum(users.values())):>12}%\n')
    result_ref.close()

generate_file('usuarios.txt')
