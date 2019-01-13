print("""
[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]
 |   ANALISADOR DE TRIANGULOS 3.0  |
[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]

""")

a = int(input("Digite o comprimento da primeira reta: "))
b = int(input("Digite o comprimento da segunda reta: "))
c = int(input("Digite o comprimento da terceira reta: "))

if a + b > c:
    print("Pode formar um triângulo")
    exit()
else:
    print("Não pode formar um triângulo")
    exit()
if a + c > b:
    print("Pode formar um triângulo")
    exit()
else:
    print("Não pode formar um triângulo")
    exit()
if b + c > a:
    print("Pode formar um triângulo")
    exit()
else:
    print("Não pode formar um triângulo")
    exit()