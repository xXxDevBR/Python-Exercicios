from random import randint

n = randint(0,5)

print('''[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]
         Jogo da Advinhação
[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]
            
  Pensei em um número de 0 a 5
         Tente acertar
''')
chute = int(input('Chute um número: '))
if chute == n:
    print('PARABÉNS! VOCÊ ACERTOU')
else:
    print('Você errou, tente novamente')

