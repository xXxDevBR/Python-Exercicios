d = int(input('Por quantos dias utilizou o carro ? '))
km = float(input('Quantos KM rodou com o carro ? '))
total = (d * 60) + (km * 0.15)
print('O total a pagar será de R${}'.format(total))
