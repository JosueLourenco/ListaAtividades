class pet:
    def __init__(self,nome,especie,idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

pet1 = pet("Orion","rato",1)
pet2 = pet("Tales","tartaruga",10)
pet3 = pet("Artemis","gato",2)

pets = [pet1, pet2, pet3]

def especie(pet):
    print(f"A espécie do seu pet é: {pet.especie}")
    return pet.especie

def idade(pet):
    print(f"Seu pet tem {pet.idade} anos")
    return pet.idade

def nome(pet):
    print(f"O nome do seu pet é {pet.nome}")
    return pet.nome

nome(pet1)