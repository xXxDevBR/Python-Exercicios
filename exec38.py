n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print("O primeiro valor ({}) é maior que o segundo valor ({})".format(n1, n2))
elif n1 < n2:
    print("O segundo valor é ({}) é maior que o primeiro valor ({})".format(n2, n1))
elif n1 == n2:
    print('Não existe valor maior, ambos são iguais')



