a = str(input('Digite uma frase: ')).lower().strip()
letra = a.count('a')
print('A letra A aparece {} vezes'.format(letra))
print('A primeira letra A aparece na {}° posição'.format(a.find('a')+1))
print('A última letra A apreceu na {}° posição'.format(a.rfind('a')+1))


