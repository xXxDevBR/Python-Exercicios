n = int(input("Digite um número inteiro: "))
print("""[1] Binário
[2] Octal
[3] Hexadecimal""")
c = int(input("Qual base deseja utilizar ? "))
if c == 1:
    print("O número {} em Binário é {}".format(n, bin(n)[2:]))
elif c == 3:
    print("O número {} em Hexadecimal é {}".format(n, hex(n)[2:]))
elif c == 2:
    print("O número {} em Octal é {}".format(n, oct(n)[2:]))
else:
    print("ERRO! Entre com um número que esteja listado acima")


