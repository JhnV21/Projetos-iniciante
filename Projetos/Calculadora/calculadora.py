# ======================= DEFS =======================
from utils import *
# ======================= DEFS =======================

from time import sleep

while True:
    texto("CALCULADORA")
    
    print("""
    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
    [5] - Exponenciação
    """)

    escolha = int(input("Escolha uma das opções acima: "))
    while escolha not in [1, 2, 3, 4, 5]:
        escolha = int(input("Escolha uma opção valida: "))
    print("========================================")

    if escolha == 1:
        limpar()
        soma()
    
    if escolha == 2:
        limpar()
        subtracao()

    if escolha == 3:
        limpar()
        multiplicacao()

    if escolha == 4:
        limpar()
        divisao()

    if escolha == 5:
        limpar()
        exponenciacao()

    r = []
    while r not in [1, 2]:
        r = int(input("Deseja fazer outra operação? 1 - SIM, 2 - NÃO "))
    if r == 1:
        limpar()
        continue
    elif r == 2:
        limpar()
        print("Fechando Calculadora...")
        sleep(1)
        break