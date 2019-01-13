s = float(input("Digite seu salário: "))

if s > 1250:
    a = ((s * 10)/100) + s
    print("Seu salário passou a ser R${:.2f} com 10% de aumento".format(a))
else:
    a = ((s * 15)/100)+ s
    print("Seu salário passou a ser R${:.2f} com 15% de aumento".format(a))


