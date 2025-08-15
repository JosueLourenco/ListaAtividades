numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def segundomaior(lista):
    maior = 0
    segundo = 0
    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
    print(segundo)
    return segundo

segundomaior(numeros)