#-*- coding: utf-8 -*-
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2
if media < 5:
    print("A média foi {}. Você foi \033[1;31mREPROVADO".format(media))
elif media > 5 and media < 6.9:
    print("A média foi {}. Você está de \033[1;33mRECUPERAÇÃO")
elif media > 7:
    print("A média foi {}. Você foi \033[1;32mAPROVADO".format(media))


