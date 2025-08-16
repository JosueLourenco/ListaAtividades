numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9, 13]
def somafun(lista):
    funsom = []
    num = int(input("Digite o número: "))
    for n in lista:
        if n == num:
            funsom.append(n)
    print(len(funsom))

somafun(numeros)