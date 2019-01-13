city = str(input('Digite o nome de uma cidade: ')).lower()

t1 = city.split()
if t1[0] == 'santo':
    print('Essa cidade começa com Santo')
else:
    print('Essa cidade não começa com Santo')
