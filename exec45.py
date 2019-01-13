#-*- coding: utf-8 -*-
from random import choice
from subprocess import call
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print("""
[+]-=-=-=-=-=-=-=-[+]
 |    JO KÊN PO    |
[+]-=-=-=-=-=-=-=-[+]

""")

entrada = str(input("Digite seu nome >> "))
print("\033[1;32m##################################################")
print("Pois bem \033[1;31m{}, a seguir as regras básicas de jogo".format(entrada))
print("")
print("\033[1;31m>>>\033[m Papel cobre Pedra")
print("\033[1;31m>>>\033[m Pedra quebra Tesoura")
print("\033[1;31m>>>\033[m Tesoura corta Papel")
input("\033[1;32mAperte ENTER para continuar")
call('clear', shell=True)
pc = choice(lista)
print("""
{1} PEDRA
{2} PAPEL
{3} Tesoura
""")
escolha = int(input("Escolha um >> "))
sleep(0.5)
print("JO")
sleep(0.8)
print("KEN")
sleep(0.8)
print("PO!")
print("O computador escolheu {}".format(pc))
if escolha == 1 and pc == 'PAPEL':
    print("\033[1;31mPAPEL COBRE PEDRA! O computador ganhou. Mais sorte da próxima vez {}".format(entrada))
elif escolha == 2 and pc == 'PAPEL':
    print("\033[1;33mEMPATE! Ambos escolheram papel")
elif escolha == 3 and pc == 'PAPEL':
    print("\033[1;32mPARABÉNS, {}! Você ganhou. TESOURA CORTA PAPEL".format(entrada))
elif escolha == 1 and pc == 'PEDRA':
    print("\033[1;33mEMPATE! Ambos escolheram pedra")
elif escolha == 2 and pc == 'PEDRA':
    print("\033[1;32mPARABÉNS, {}! Você ganhou. PAPEL COBRE PEDRA".format(entrada))
elif escolha == 3 and pc == 'PEDRA':
    print("\033[1;31mPEDRA QUEBRA TESOURA! O computador ganhou. Mais sorte da próxima vez {}".format(entrada))
elif escolha == 1 and pc == 'TESOURA':
    print("\033[1;32mPARABÉNS, {}! Você ganhou. PEDRA QUEBRA TESOURA".format(entrada))
elif escolha == 2 and pc == 'TESOURA':
    print("\033[1;31mTESOURA CORTA PAPEL! O computador ganhou. Mais sorte da próxima vez {}".format(entrada))
elif escolha == 3 and pc == 'TESOURA':
    print("\033[1;33mEMPATE! Ambos escolheram tesoura")