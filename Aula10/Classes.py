# classe - espaço onde vou descrever um objeto
# atributos- caracteristicas do objeto
# metodos - ações deese objeto

#nome e vida- atacar
#self quanod quero acessar algum atributo
#cinstrutor - quando quero criar um novo objeto, chamo o construtor para acessar pros atributos
'''
class Personagem:
    # construtor
    def __init__(self, nome, vida):
      # encapsulamento
      self.__nome = nome
      self.__vida = vida
    #definindo GET 
    @property
    def nome(self):
       return self.__nome
    #definindo o SET
    @nome.setter
    def nome(self,novo_nome):
       self.__nome = novo_nome
    
    @property
    def vida(self):
       return self.__vida
    #definindo o SET
    @vida.setter
    def vida(self,vida):
       self.__vida = vida

    def atacar(self, personagem):
       personagem.vida -= 20
       print (f'{self.nome} atacou o {personagem.nome} e tirou 20 pontos de vida')
       print(f'Agora esta com {personagem.vida} ')

class Guerreiro (Personagem):
    def __init__(self, nome, vida, escudo=False):
      super().__init__(nome, vida)
      self.__escudo = escudo

    @property
    def escudo(self):
     return self.__escudo
   
    @escudo.setter
    def escudo(self, escudo):
     self.__escudo = escudo 
#sobrescrevendo p metodo da class pai
    def atacar(self,Personagem):
        Personagem.vida -= 40
        print (f'{self.nome} atacou o {Personagem.nome} e tirou 20 pontos de vida')
        print(f'Agora esta com {Personagem.vida} ')   

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome,vida)
    def curar(self,personagem):
              (Personagem.vida) += 15
              print(f'{self.__nome} usou poder de cura em {personagem.nome}')
              print(f'A vida de {personagem.nome} agora é {personagem.vida}')
frodo = Personagem('Frodo', 100)
Gandof = Mago('Gandof', 200)
lindolf = Guerreiro ('lindolf',150)

lindolf.atacar(Gandof)
'''

'''
class Favorito:
      # construtor
    def __init__(self, nome, vida):
      # encapsulamento
      self.__nome = nome
      self.__vida = vida
    #definindo GET 
    @property
    def nome(self):
       return self.__nome
    #definindo o SET
    @nome.setter
    def nome(self,novo_nome):
       self.__nome = novo_nome
    
    @property
    def vida(self):
       return self.__vida
    #definindo o SET
    @vida.setter
    def vida(self,vida):
       self.__vida = vida

    def atacar(self,Favorito):
       Favorito.vida -= 20
       print (f'{self.nome} atacou o {Favorito.nome} e tirou 20 pontos de vida')
       print(f'Agora esta com {Favorito.vida} ')     
Favorito1 = Favorito('Neo', 103 )
print(f'Personagem: {Favorito1.nome}')
print(f'Personagem: {Favorito1.vida}')

Favorito2 = Favorito('Thanos', 10000 )
print(f'Personagem: {Favorito2.nome}')
print(f'Personagem: {Favorito2.vida}')
Favorito1.atacar(Favorito2)
Favorito2.atacar(Favorito1)
'''

class Personagem:
    # construtor
    def __init__(self, nome, vida):
      # encapsulamento
      self.__nome = nome
      self.__vida = vida
    #definindo GET 
    @property
    def nome(self):
       return self.__nome
    #definindo o SET
    @nome.setter
    def nome(self,novo_nome):
       self.__nome = novo_nome
    
    @property
    def vida(self):
       return self.__vida
    #definindo o SET
    @vida.setter
    def vida(self,vida):
       self.__vida = vida

    def atacar(self, personagem):
       personagem.vida -= 40
       print (f'{self.nome} atacou o {personagem.nome} e tirou 20 pontos de vida')
       print(f'Agora esta com {personagem.vida} ')
    def caixa(self, Mago):
       Mago.vida -= 200
       print (f'{self.nome} atacou o {Mago.nome} e tirou 200 pontos de vida')
       print(f' O {Mago.nome} morreu ')

class Guerreiro (Personagem):
    def __init__(self, nome, vida, escudo=False):
      super().__init__(nome, vida)
      self.__escudo = escudo

    @property
    def escudo(self):
     return self.__escudo
   
    @escudo.setter
    def escudo(self, escudo):
     self.__escudo = escudo 
#sobrescrevendo p metodo da class pai
    def atacar(self,Personagem):
        Personagem.vida -= 40
        print (f'{self.nome} atacou o {Personagem.nome} e tirou 20 pontos de vida')
        print(f'Agora esta com {Personagem.vida} ')
    def batrang(self, Personagem):
       Personagem.vida -=100
       if Personagem.vida<=0:
          print(f'Agora esta com {Personagem.vida}')
       else:
            print(f'{self.nome} atacou o {Personagem.nome} e tirou 100 pontos de vida e morreu')
       
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome,vida)
    def curar(self,personagem):
              (personagem.vida) += 15
              print(f'{self.nome} usou poder de cura em {personagem.nome}')
              print(f'A vida de {personagem.nome} agora é {personagem.vida}')

    def atacar(self, personagem):
        personagem.vida -= 40
        print (f'{self.nome} atacou o {personagem.nome} e tirou 20 pontos de vida')
        print(f'Agora esta com {personagem.vida} ')
    
Coringa = Personagem('Coringa', 100)
Doutor = Mago('Doutor', 200)
Batman = Guerreiro('Batman',150)

Coringa.atacar(Batman)
Doutor.curar(Batman)
Coringa.caixa(Doutor)
Batman.atacar(Coringa)