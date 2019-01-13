from datetime import date
a = int(input("Digite o ano de nascimento do atleta: "))
n = date.today().year - a
if n <= 9:
    print("CLASSE MIRIM")
elif n > 9 and n <= 14:
    print("CLASSE INFANTIL")
elif n > 14 and n <= 19:
    print("CLASSE JUNIOR")
elif n == 20:
    print("CLASSE SÊNIOR")
else:
    print("CLASSE MASTER")

