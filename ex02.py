nota1 = float (input('Informe a primeira nota: '))
nota2 = float (input('Informe a segunda nota: '))

media = (nota1 + nota2)/2
if media < 4:
	print('Reprovado')
elif media < 6:
	print('Exame')
else:
	print('Aprovado')
