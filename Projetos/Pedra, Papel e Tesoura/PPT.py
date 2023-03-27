from utils import *
from random import randint
from time import sleep

pc = 0
eu = 0
lance = ["PEDRA", "PAPEL", "TESOURA"]

texto("Bem vindo ao jogo de Pedra, Papel ou Tesoura")

while True:
    placar(eu, pc)
    for i, l in enumerate(lance):
        print(f"[{i}] - {l}")
    escolha_eu = int(input("Escolha seu lance: "))
    try:
        escolha_eu = lance[escolha_eu]
    except IndexError:
        print("Índice inválido.")
        sleep(1)
    escolha_pc = lance[randint(0, 2)]

    print()
    
    #PEDRA ======================================================
    if escolha_eu == lance[0] and escolha_pc == lance[0]:
        empate(escolha_eu, escolha_pc)

    elif escolha_eu == lance[0] and escolha_pc == lance[1]:
        compV(escolha_eu, escolha_pc)
        pc += 1
    
    elif escolha_eu == lance[0] and escolha_pc == lance[2]:
        pessoV(escolha_eu, escolha_pc)
        eu += 1
    
    #PAPEL ======================================================
    if escolha_eu == lance[1] and escolha_pc == lance[0]:
        pessoV(escolha_eu, escolha_pc)
        eu += 1

    elif escolha_eu == lance[1] and escolha_pc == lance[1]:
        empate(escolha_eu, escolha_pc)
        
    elif escolha_eu == lance[1] and escolha_pc == lance[2]:
        compV(escolha_eu, escolha_pc)
        pc += 1
    
    # #TESOURA ===================================================
    if escolha_eu == lance[2] and escolha_pc == lance[0]:
        compV(escolha_eu, escolha_pc)
        pc += 1

    elif escolha_eu == lance[2] and escolha_pc == lance[1]:
        pessoV(escolha_eu, escolha_pc)
        eu += 1
        
    elif escolha_eu == lance[2] and escolha_pc == lance[2]:
        empate(escolha_eu, escolha_pc)

    r = ""
    while r != "S" and r != "N":
        r = input("Quer continuar? [S/N] ").upper()
    if r == "N":
        if eu > pc:
            mFinalV(eu, pc)
        elif pc > eu:
            mFinalP(eu, pc)
        else:
            mFinalE(eu, pc)
        break
