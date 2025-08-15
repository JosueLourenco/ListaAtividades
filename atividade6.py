numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def buscar(lista):
    listado = []
    numero = int(input("Digite o número desejado: "))
    try:
        for num in lista:
           if num == numero:
            listado.append(num)
        if listado[0] == numero:
           return True
        else:
           return False
    except:
        return False
        
    
print(buscar(numeros))