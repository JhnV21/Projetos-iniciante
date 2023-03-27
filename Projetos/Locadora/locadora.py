from utils import *
import os
from time import sleep

cars = [("Chevrolet Tracker", 120), 
        ("Chevrolet Onix", 90), 
        ("Chevrolet Spin", 150), 
        ("Hyundai HB20", 85), 
        ("Hyundai Tucson", 120), 
        ("Fiat Uno", 60), 
        ("Fiat Mobi", 70), 
        ("Fiat Pulse", 130), 
        ]

carro_escolhido = []

while True:
    os.system("cls")
    texto("Bem vindo a locadora de Carros!")
    print()
    print("[1] - Mostrar portifólio\n[2] - Alugar um carro\n[3] - Devolver um carro")
    print()
    escolha = int(input("Escolha uma das opções acima: "))
    

    if escolha == 1:
        os.system("cls")
        lista(cars)
    
    elif escolha == 2:
        os.system("cls")
        print("[ ALUGAR ] Dê uma olhada em nosso portifólio")
        print()

        lista(cars)

        codigo = int(input("Escolha o código do carro: "))
        preco = cars[codigo][1]
        dias = int(input("Escolha quantos dias deseja alugar: "))
        valor = preco * dias

        os.system("cls")
        print(f"Você escolheu {cars[codigo][0]} por {dias} dias.")
        print(f"O aluguel totalizaria R${valor:.2f}. Deseja alugar? ")
        alugou = int(input("[1] - SIM | [2] - NÃO "))
        if alugou == 1:
            carro_escolhido.append(cars.pop(codigo))
            print(f"Parabéns voce Alugou o {carro_escolhido[0][0]} por {dias} dias.")
        elif alugou == 2:
            continue
        else:
            print("\033[31mCódigo invalido\033[m")
            continue

    elif escolha == 3:
        os.system("cls")
        print("Segue a lista de carros alugados. Qual voce deseja devolver?")
        lista(carro_escolhido)
        
        devolver = int(input("Escolha o código do carro que deseja devolver: "))
        print(f"Obrigado por devolver o carro {carro_escolhido[devolver][0]}")
        cars.append(carro_escolhido[devolver])

    r = []
    while r not in [1, 2]:
        print("=========================")
        r = int(input("1 - CONTINUAR | 2 - SAIR "))
    if r == 2:
        break