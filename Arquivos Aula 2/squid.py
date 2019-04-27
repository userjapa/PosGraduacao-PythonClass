file_ref, denied = open('squid/access.log.6/data'), dict()

for line in file_ref:
    infos       = line.split()
    status_code = int(infos[3].split('/')[1])
    if status_code == 400:
        ip = infos[2]
        if ip in denied.keys(): denied[ip] += 1
        else: denied[ip] = 1

file_ref.close()
for k,v in denied.items():
    print(f'{k} denied {v} times')
