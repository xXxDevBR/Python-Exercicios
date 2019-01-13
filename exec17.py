import math

co = int(input("Digite o valor do cateto oposto: "))
ca = int(input("Digite o valor do cateto adjacente: "))
hip = math.hypot(co, ca)
print("A hipotenusa vale {}".format(hip))
