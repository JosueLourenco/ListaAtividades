lista = [
    {"nome": "Ana", "idade": 23},
    {"nome": "Bruno", "idade": 31},
    {"nome": "Carlos", "idade": 27},
    {"nome": "Diana", "idade": 19}
]

def buscarnome(lista):
    for nome in lista:
        print(nome["nome"])

buscarnome(lista)