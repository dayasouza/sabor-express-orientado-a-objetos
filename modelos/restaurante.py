class Restaurante:
    #construtor
    def __init__(self, nome, categoria):
        #Atributos 
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

#Objetos
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))