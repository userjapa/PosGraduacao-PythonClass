arq = open('test.txt', 'r')
for line in arq:
    print(line.split())
arq.close()

with open('test.txt', 'r+') as text_file:
    text = text_file.read()
    # pointer back to start
    text_file.write('QUERO CAFEEEEEE\n')
    text_file.seek(0)
    text = text_file.read()
    print(text)
