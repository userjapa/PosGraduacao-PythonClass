num = int(input('Informe um numero entre 1 e 10: '))
if (num < 1 or num > 10):
	print ('Valor invalido!')
else:
	for n in range(10):
		n += 1
		print(f'{num} x {n} = {num * n}')