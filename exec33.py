print("""Digite três números""")
n1 = int(input("[+]=>> "))
n2 = int(input("[+]=>> "))
n3 = int(input("[+]=>> "))


if n1 == n2 or n1 == n3 or n2 == n3:
    i = n1 == n2 or n1 == n3 or n2 == n3
    print("Há valores iguais")

# MAIOR NÚMERO
if n1 > n2 and n1 > n3:
    print("{} é o maior número".format(n1))
if n2 > n1 and n2 > n3:
    print("{} é o maior número".format(n2))
if n3 > n1 and n3 > n2:
    print("{} é o maior número ".format(n3))

# MENOR NÚMERO
if n1 < n2 and n1 < n3:
    print("{} é o menor número".format(n1))
if n2 < n1 and n2 < n3:
    print("{} é o menor número".format(n2))
if n3 < n1 and n3 < n2:
    print("{} é o menor número".format(n3))


