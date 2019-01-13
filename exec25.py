nome = str(input('Digite um nome completo: ')).lower()
silva = 'silva' in nome
if silva == True:
    print('Existe Silva nesse nome')
else:
    print('Não há Silva nesse nome')