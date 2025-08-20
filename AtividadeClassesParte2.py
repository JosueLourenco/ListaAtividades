import AtividadeClasses as at

def petcriar():
    nome = (input("Digite o nome de seu pet:").capitalize())
    especie = (input("Digite a especie de seu pet:"))
    idade = (int(input("Digite a idade de seu pet:")))
    petnovo = at.pet(nome, especie, idade)
    at.pets.append(petnovo)

def removerpet():
    nome = input("Digite o nome do pet que deseja remover: ").capitalize()
    for pet in at.pets:
        if pet.nome == nome:
            at.pets.remove(pet)
            print(f"{nome} removido")
            return
    else: 
        print(f"Pet '{nome}' não encontrado.")

at.especie(at.pets[0])
at.idade(at.pets[0])
at.nome(at.pets[0])

petcriar()
removerpet()

print(at.pets)
    
     
