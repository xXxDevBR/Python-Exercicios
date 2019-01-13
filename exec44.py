from time import sleep
valor = float(input("Digite o valor do produto: "))
print("""
======================
 Forma de Pagamento
======================
[1] À vista // Dinheiro ou Cheque
[2] À vista // Cartão de Cŕedito
[3] 2x no Cartão de Crédito
[4] 3x ou mais no Cartão de Crédito
""")
pag = int(input("Selecione sua forma de pagamento: "))
if pag == 1:
    print("Você selecionou pagamento: Á vista // Dinheiro ou Cheque")
    print("Aguarde...")
    sleep(0.8)
    desconto10 = valor - (valor * 0.1)
    print("PARABÉNS! Você recebeu um desconto de 10%, equivalendo à R${:.2f}".format(desconto10))
elif pag == 2:
    print("Você selecionou pagamento: Á vista // Cartão de Crédito")
    print("Aguarde...")
    sleep(0.8)
    desconto5 = valor - (valor * 0.05)
    print("PARABÉNS! Você recebeu um desconto de 5%, equivalendo à R${:.2f}".format(desconto5))
elif pag == 3:
    print("Você selecionou pagamento: 2x no Cartão de Crédito")
    print("Aguarde...")
    sleep(0.8)
    print("Transação aprovada. Valor pago R${:.2f}".format(valor))
elif pag == 4:
    print("Você selecionou pagamento: 3x ou mais no Cartão de Crédito")
    print("Aguarde...")
    sleep(0.8)
    juros = (valor * 0.2) + valor
    print("Transação aprovada. Você recebeu juros de 20% pela forma de pagamento, equivalento à R${:.2f}".format(juros))