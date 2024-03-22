#Importando a classe para o programa principal
from modelos.restaurante import Restaurante

#Criando e instanciando os restaurantes
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'mexicano')
restaurante_japones = Restaurante('japa', 'japones')

#alterando o estado de um restaurante
restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao('Gui', 10)
restaurante_japones.receber_avaliacao('Lais', 8)
restaurante_japones.receber_avaliacao('Emy', 5)

#criando o método main
def main():
    Restaurante.listar_restaurantes()

#informando que esse é o programa principal
if __name__ == '__main__':
    main()