var = input('Digite algo: ')

print('Só tem espaços ? {}'.format(var.isspace()))
print('É alfabético ? {}'.format(var.isalpha()))
print('É numérico ? {}'.format(var.isnumeric()))
print('É alfanumérico ? {}'.format(var.isalnum()))
print('Está apenas em maiúsculas ? {}'.format(var.isupper()))
print('Está apenas em minúsculas ? {}'.format(var.islower()))
print('Está capitalizada ? {}'.format(var.istitle()))