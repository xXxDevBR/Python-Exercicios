km = int(input("Digite a distância da viagem em KM: "))
if km <= 200:
    preco = km * 0.50
    print("O valor da passagem será de R${}".format(preco))
else:
    preco = km * 0.45
    print("O valor da passagem será de R${}".format(preco))



