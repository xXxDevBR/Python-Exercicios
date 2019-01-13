nome = str(input("Digite seu nome: "))

mai = nome.upper()
min = nome.lower()
letras = len(nome.replace(" ", ""))
conta = nome.find(' ')
print("""
Maiúsculas > {}
Minúsculas > {}
Quantas letras sem espaços > {}
Quantas letras primeiro nome > {}
""".format(mai, min, letras, conta))

