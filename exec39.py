from datetime import date
def principal():
    ano = int(input("Digite o ano de nascimento seu: "))
    ano_atual = date.today().year
    print("Quem nasceu em {} tem {} anos em {}".format(ano, date.today().year - ano, date.today().year))
    alista = ano_atual - ano
    if alista < 18:
        tempo = 18 - alista
        if tempo == 1:
            print("Você ainda vai se alistar no serviço militar. Ainda falta 1 ano para você se alistar.".format(tempo))
            print("Seu alistamento será em {}.".format(ano_atual+tempo))
        else:
            print("Você ainda vai se alistar no serviço militar. Ainda falta {} anos para você se alistar.".format(tempo))
            print("Seu alistamento será em {}.".format(ano_atual + tempo))
    elif alista == 18:
        print("Está na hora de se alistar. Vá a unidade mais próxima com uma foto 3x4 e CPF")
    elif alista > 18:
        tempo = alista - 18
        if tempo == 1:
            print("Seu tempo de alistamento já excedeu. A data foi a {} ano".format(tempo))
            print("Seu alistamento foi em {}".format(ano_atual-tempo))
        else:
            print("Seu tempo de alistamento já excedeu. A data foi a {} anos.".format(tempo))
            print("Seu alistamento foi em {}".format(ano_atual - tempo))
sexo = str(input("Sexo [M/F] >> ")).upper()
if sexo == 'F':
    sim = input("O alistamento militar feminino não é obrigatório. Deseja se alistar ? [S/N] >> ").upper()
    if sim == 'S':
        principal()
    elif sim == 'N':
        print("\033[1;33mBRASIL\033[1;32m ACIMA DE TUDO, DEUS ACIMA DE TODOS")
        exit()
    else:
        print("Erro. Saindo")
        exit()
elif sexo == "M":
    print("O alistamento militar masculino é obrigatório.")
    principal()
else:
    print('\033[1;31mErro. Saindo')
    exit()


