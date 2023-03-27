import os
from time import sleep

def texto(msg):
    t = len(msg) + 4
    print('=' * t)
    print(f'{msg:^{t}}')
    print('=' * t)

def placar(pessoa=0, comp=0):
    os.system("cls") or None
    print()
    print("PLACAR:")
    print(f"Você: {pessoa}")
    print(f"Computador: {comp}")
    print("=" * 15)
    print()
    print()


def empate(pessoa, comp):
    print(f"Sua Jogada: {pessoa}")
    print(f"Jogada do computador: {comp}")
    print("\033[33mEmpate!!\033[m")
    

def compV(pessoa, comp):
    print(f"Sua Jogada: {pessoa}")
    print(f"Jogada do computador: {comp}")
    print("\033[31mComputador venceu!!\033[m!!")
    

def pessoV(pessoa, comp):
    print(f"Sua Jogada: {pessoa}")
    print(f"Jogada do computador: {comp}")
    print("\033[32mVocê venceu!!\033[m")


def mFinalV(pessoa=0, comp=0):
    os.system("cls") or None
    print("EZ")
    print("\033[32mPLACAR FINAL:\033[m")
    print(f"\033[32mVocê: {pessoa}\033[m")
    print(f"\033[31mComputador: {comp}\033[m")
    sleep(1)


def mFinalP(pessoa=0, comp=0):
    os.system("cls") or None
    print("VOCE PERDEU PRA UM COMPUTADOR ")
    print("\033[31mPLACAR FINAL:\033[m")
    print(f"\033[31mVocê: {pessoa}\033[m")
    print(f"\033[32mComputador: {comp}\033[m")
    sleep(1)


def mFinalE(pessoa=0, comp=0):
    os.system("cls") or None
    print("EMPATE")
    print("\033[33mPLACAR FINAL:\033[m")
    print(f"\033[33mVocê: {pessoa}\033[m")
    print(f"\033[33mComputador: {comp}\033[m")
    sleep(1)