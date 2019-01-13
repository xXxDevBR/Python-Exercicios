print("""
[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]
 |   ANALISADOR DE TRIANGULOS 3.0  |
[+]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[+]
""")

a = int(input("Digite o comprimento da primeira reta: "))
b = int(input("Digite o comprimento da segunda reta: "))
c = int(input("Digite o comprimento da terceira reta: "))

if a + b > c and b + c > a and c + a > b:
    if a == b and a == c:
        forma = "EQUILÁTERO"
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        forma = "ISÓSCELES"
    elif a != b and a != c and b != c:
        forma = "ESCALENO"

    print("É possível formar um triângulo {} com esses seguimentos".format(forma))
else:
    print("Não é possível formar um triângulo")



