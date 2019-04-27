def validate_ip (ip):
    arr = ip.split('.')
    for n in arr:
        if (int(n) > 255) || int(n) < 0: return False
    return True

file_ref = open('listaips.txt', 'r')
ips = dict()
for line in file_ref:
    ips[line] = validate_ip(line)

file_ref.close()

result_ref = open('ip-result.txt', 'w')
result_ref.write('[Enderecos validos:]\n')
result_ref.writelines(filter(lambda n: ips[n], ips.keys()))
result_ref.write('\n')
result_ref.write('[Enderecos invalidos:]\n')
result_ref.writelines(filter(lambda n: not ips[n], ips.keys()))

result_ref.close()
