# Pegar informações
casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário: R$"))
anos = int(input("Digite quantos anos você pretende pagar: "))

# calculos
meses = anos * 12
prestacao = casa / meses
ex = salario * 0.3
# condições
if prestacao > ex:
    print("Valor da Casa: R${}".format(casa))
    print("Seu salário: R${}".format(salario))
    if anos == 1:
        print("Tempo: 1 ano")
    else:
        print("Tempo: {} anos".format(anos))
    print("Valor de cada prestação: R${:.2f}".format(prestacao))
    print("Status: NEGADO")
else:
    print("Valor da Casa: R${}".format(casa))
    print("Seu salário: R${}".format(salario))
    if anos == 1:
        print("Tempo: 1 ano")
    else:
        print("Tempo: {} anos".format(anos))
    print("Valor de cada prestação: R${:.2f}".format(prestacao))
    print("Status: APROVADO")
