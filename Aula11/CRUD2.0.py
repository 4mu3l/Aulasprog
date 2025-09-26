#Importação para arquivo json
#Importação para limpar tela
import json
import os
#Lambda para limpar tela
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#CRUD de uma biblioteca com json e com POO 
#bibli é um dicionario, que puxa todos "livro"
#livro é uma lista, o que vai ser adicionado no dicionário
bibli =[]
livro={}

class Livro:
    # construtor
    def __init__( self,nome, autor, ano):
      # encapsulamento
      self.__nome = nome
      self.__autor = autor
      self.__ano = ano
    #definindo GET 
    @property
    def nome(self):
       return self._nome
    #definindo o SET
    @nome.setter
    def nome(self,novo_nome):
       self.__nome = novo_nome
    
    @property
    def autor(self):
       return self.__autor
    #definindo o SET
    @autor.setter
    def autor(self,autor):
       self.__autor = autor

    def atacar(self, personagem):
       personagem.vida -= 40
       print (f'{self.nome} atacou o {personagem.nome} e tirou 20 pontos de vida')
       print(f'Agora esta com {personagem.vida} ')
    def caixa(self, Mago):
       Mago.vida -= 200
       print (f'{self.nome} atacou o {Mago.nome} e tirou 200 pontos de vida')
       print(f' O {Mago.nome} morreu ')
'''
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        """Converte objeto Livro em dicionário (para salvar em JSON)."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Livro a partir de um dicionário (quando carrega do JSON)."""
        return Livro(data["titulo"], data["autor"], data["ano"])
'''
# Menu para o CRUD de uma biblioteca para livros
while True:
  try:
      # Menu para o CRUD de uma biblioteca para livros
      def menu():
         print('1 - Cadastrar um livro')
         print('2 - Listar um livro')
         print('3 - Atualizar um livro')
         print('4 - Excluir um livro')
         print('5 - Sair da biblioteca')
      menu()
      opcao = int(input('Escolha uma opção: '))
      limpar()
    # função cadastrar livro 

     
    
  except:
     ...

