from random import randint
from time import sleep


def sortearSenha(tamanho, quant):
    for c in range(0, quant):
        if tamanho == 1:
            n = randint(1000, 9999)
        elif tamanho == 2:
            n = randint(100000, 999999)
        else:
            n = randint(10000000, 99999999)
        print(f'- a sua {c+1}º senha será: {n}')
        sleep(0.58)


while True:
    #VALIDAÇÃO DA OPÇÃO REFERNTE AO TAMANHO DA SENHA
    while True:
        ds = input('  -Qual o tamanho da senha desejada \n  (1) 4 digitos\n  (2) 6 digitos\n  (3) 8 digitos     escolha: ')
        if ds.isalpha() or ds.strip(" ") == "":
            print(f"\n\033[31m  -ERRO!! ESCOLHA AS OPÇÕES ENTRE 1 A 3!!\033[m\n")
            continue
        elif ds.isnumeric():
            ds = int(ds)
            if 0 < ds < 4:
                break
            else:
                print(f"\n\033[31m  -ERRO!! ESCOLHA AS OPÇÕES ENTRE 1 A 3!!\033[m\n")
    #VALIDAÇÃO DA QUANTIDAE DE SENHAS
    while True:
        quanti = input("  -Quantas senhas diferentes deseja gerar?\n   (maximo 80)      escolha: ")
        if quanti.isalpha() or quanti.strip(" ") == "":
            print("\n\033[31m   -ERRO!! ESCOLHA UMA QUANTIDADE DE SENHAS ENTRE 1 E 80!!\033[m\n")
            continue
        elif quanti.isnumeric():
            quanti = int(quanti)
            if 0 < quanti < 81:
                break
            else:
                print("\n\033[31m   -ERRO!! ESCOLHA UMA QUANTIDADE DE SENHAS ENTRE 1 E 80!!\033[m\n")

    #GERANDO AS SENHAS
    if ds == 1:
        sortearSenha(1, quanti)
    elif ds == 2:
        sortearSenha(2, quanti)
    elif ds == 3:
        sortearSenha(3, quanti)

    else:
        print (f' ERROR - tente novamente - ERROR\n\n\n\n')

    #VERIFICAÇÃO SE O USER DESEJA CONTINUAR
    continuar = ''
    while True:
        continuar = str(input("Quer continuar?[S/N]    - ")).upper().strip()
        if continuar == "S":
            break
        if continuar == "N":
            break
    if continuar == "N":
        break
    print("\n\n\n")
