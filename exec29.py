v = float(input('Digite a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado. Pague R${:.2f} na unidade do DETRAM mais próxima'.format(m))
else:
    print('Você está dentro do limite de velocidade! Dirija com cuidado')


