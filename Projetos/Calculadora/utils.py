from time import sleep

def soma():
    print("Soma Escolhido")
    n1 = int(input("1° Valor: "))
    n2 = int(input("2° Valor: "))
    print("Calculando...")
    sleep(1)
    print(f"{n1} + {n2} = {n1 + n2}")


def subtracao():
    print("Subtração Escolhido")
    n1 = int(input("1° Valor: "))
    n2 = int(input("2° Valor: "))
    print("Calculando...")
    sleep(1)
    print(f"{n1} - {n2} = {n1 - n2}")

    
def multiplicacao():
    print("Multiplicação Escolhido")
    n1 = int(input("1° Valor: "))
    n2 = int(input("2° Valor: "))
    print("Calculando...")
    sleep(1)
    print(f"{n1} x {n2} = {n1 * n2}")

    
def divisao():
    print("Divisão Escolhido")
    n1 = int(input("1° Valor: "))
    n2 = int(input("2° Valor: "))
    print("Calculando...")
    sleep(1)
    print(f"{n1} ÷ {n2} = {n1 / n2}")
    

def exponenciacao():
    print("Exponenciação Escolhido")
    n1 = int(input("1° Valor: "))
    n2 = int(input("2° Valor: "))
    print("Calculando...")
    sleep(1)
    print(f"{n1} ** {n2} = {n1 ** n2}")
    
def texto(txt):   
    t = len(txt) + 14
    print('=' * t)
    print(f'{txt:^{t}}')
    print('=' * t)

def limpar():
    import os
    os.system('cls') or None