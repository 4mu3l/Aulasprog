#importações de json e limpar
import json
import os
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#classe livro, para poder adicionar, excluir e atualizar 
class Livro:
    def __init__(self, id, titulo,autor, ano):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
    @property
    def id(self):
        return self.__id
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo
    
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self,autor):
        self.__autor = autor
    
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
    
    def to_dict(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano
        }
# classe biblioteca para armazenar o(s) livro(s)
class Biblioteca:
    def __init__(self, arquivo_json='biblioteca.json'):
        self.__arquivo = arquivo_json
        self.__livros = []
        self.__carregar_dados()

    def __carregar_dados(self):
        if os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
                for d in dados:
                    livro = Livro(
                        d.get('id', self.gerar_id()),  # se não tiver id, gera um
                        d['titulo'],
                        d['autor'],
                        d['ano']
                    )
                    self.__livros.append(livro)
    #dentro de biblioteca temos o salvar que é o que faz o livro permanecer na bilioteca
    def salvar_dados(self):
        dados = []

        for livro in self.__livros:
            dados.append(livro.to_dict())
        with open(self.__arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f,indent=4, ensure_ascii=False)
        
    def gerar_id(self):
        if not self.__livros:
            return 1
        return max(l.id for l in self.__livros) + 1
    
    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro= Livro(self.gerar_id(), titulo, autor, ano)
        self.__livros.append(novo_livro)
        self.salvar_dados()
        print(f'Livro "{titulo}" cadastrado com sucesso!')

    def listar_livros(self):
        if not self.__livros:
            print("Nenhum livro cadastrado.")
        else:
            print('\nLista de Livros:')
            for livro in self.__livros:
                print(f'ID: {livro.id}|Título: {livro.titulo}| Autor: {livro.autor}| Ano: {livro.ano}')

    def atualizar_livros(self):
        id = int(input('Digite o ID do livro que deseja atualizar: '))
        for livro in self.__livros:
            if livro.id == id:
                novo_titulo = input(f'Novo título (atual: {livro.titulo}): ')
                novo_autor = input(f'Novo autor (atual: {livro.autor}): ')
                try:
                    novo_ano = int(input(f'Novo ano (atual: {livro.ano}): '))
                    livro.titulo = novo_titulo if novo_titulo else livro.titulo
                    livro.autor = novo_autor if novo_autor else livro.autor
                    livro.ano = novo_ano if novo_ano else livro.ano
                    self.salvar_dados()
                    print(f'Livro com ID {id} atualizado com sucesso!')
                except ValueError:
                    print('Ano inválido. Digite um número.')
                return
        print(f'Livro com ID {id} não encontrado.')
#antes de excluir, possa mostrar os livros cadastrados
    def excluir_livros(self):
        self.listar_livros()
        id = int(input('Digite o ID do livro que deseja excluir: '))
        for livro in self.__livros:
            if livro.id == id:
                self.__livros.remove(livro)
                self.salvar_dados()
                print(f'Livro com ID {id} excluído com sucesso!')
                return
        print(f'Livro com ID {id} não encontrado.')
def main():
    while True:
        biblioteca = Biblioteca(arquivo_json='biblioteca.json')
        print(f'\n=========== Sistema de Biblioteca ===========')
        print('1 - Cadastrar livro')
        print('2 - Listar livros')
        print('3 - Atualizar livro')
        print('4 - Excluir livro')
        print('5 - Sair')
        opcao = input('Escolha uma opção: ')
        limpar()
        if opcao == '1':
            titulo = input('Título: ')
            autor = input('Autor: ')
            try:
                ano = int(input('Ano: '))
                biblioteca.cadastrar_livro(titulo, autor, ano)
            except ValueError:
                print('Ano inválido. Digite um número.')
        elif opcao == '2':
            biblioteca.listar_livros()
        elif opcao == '3':
            biblioteca.atualizar_livros()
        elif opcao == '4':
            biblioteca.excluir_livros()
        elif opcao == '5':
            print('Saindo do sistema...')
            break
if __name__ == "__main__":
 main()