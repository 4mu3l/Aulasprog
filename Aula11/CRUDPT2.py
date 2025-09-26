from CRUDprof import Biblioteca

def main():
    while True:
        biblioteca = Biblioteca(arquivo_json='biblioteca.json')
        print(f'\n=========== Sistema de Biblioteca ===========')
        print('1 - Cadastrar livro')
        print('2 - Listar livros')
        opcao = input('Escolha uma opção: ')

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

if __name__ == "__main__":
 main()