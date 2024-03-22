#importando a classe avaliação
from modelos.avaliacao import Avaliacao
class Restaurante:
    """Representa um restaurante e suas caracteristicas"""
    restaurantes = []

    #construtor
    def __init__(self, nome, categoria):
        """Inicializa uma instância de restaurante

            Parametros: 
            - nome (str): O nome do restaurante
            - categoria (str): A categoria do restaurante
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma apresentação em string do restaurante"""
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes"""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')

    @property
    def ativo(self):
        """REcebe o nome do estado de ativo ou inativo"""
        return 'ativo' if self._ativo else 'inativo'

    def alternar_estado(self):
        """Alterna o status do restaurante"""
        self._ativo = not self._ativo 

    def receber_avaliacao(self, cliente, nota):
        """REgistra uma avaliação para o restaurante

            Parametros: 
            - cliente (str): O nome do cliente que fez a avaliação
            - nota (float): A nota atribuida ao restaurante (entre 0 e 5)
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        """Calcula a média das avaliações do restaurante"""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media