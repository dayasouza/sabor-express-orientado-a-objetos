#Importando a classe para o programa principal
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebiba
from modelos.cardapio.prato import Prato


#Criando e instanciando os restaurantes
restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebiba('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
bebida_suco.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

#criando o método main
def main():
    restaurante_praca.exibir_cardapio

#informando que esse é o programa principal
if __name__ == '__main__':
    main()