def texto(txt):   
    t = len(txt) + 14
    print('=' * t)
    print(f'{txt:^{t}}')
    print('=' * t)


def lista(lista):
    for n, v in enumerate(lista):
        print(f"[{n}] {v[0]} - R$ {v[1]} /dia")
    print()
    print()