data = [
	['brasil', 'italia', [10, 9]],
	['brasil', 'espanha', [5, 7]],
	['italia', 'espanha', [7, 8]]
]

time_falta = dict()

for jogo in data:
	if jogo[0] in time_falta:
		time_falta[jogo[0]] += jogo[2][0]
	else:
		time_falta[jogo[0]] = jogo[2][0]
	if jogo[1] in time_falta:
		time_falta[jogo[1]] += jogo[2][1]
	else:
		time_falta[jogo[1]] = jogo[2][1]

min_fault = 0
min_name = ''
max_fault = 0
max_name = ''

for k,v in time_falta.items():
	if min_fault == 0:
		min_fault = v
	if min_fault >= v:
		min_fault = v
		min_name = k
	if max_fault <= v:
		max_fault = v
		max_name = k

total_faltas = sum(time_falta.values())

print(f'{total_faltas} faltas')
print(f'Mais faltas: {max_name} {max_fault}')
print(f'Menos faltas: {min_name} {min_fault}')