#importações para limpar e usar json
import os 
import json
arquivo=' '
livros=[]
# Função da biblioteca
while True:
    #Try para corrigir os erros
    try:
        # Menu para o CRUD de uma biblioteca para livros
        def menu():
            print('1 - Cadastrar um livro')
            print('2 - salvar na biblioteca')
            print('3 - Listar um livro')
            print('4 - Atualizar um livro')
            print('5 - Excluir um livro')
            print('6 - Sair da biblioteca')
        menu()
        escolha = input('Escolha uma opção (1-6): ')
        limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        #função para adicionar no arquivo json os livros desejados e que não seja subtituído só adicionado
        def cadastrar():
            livro={}
            livro['nome']= input('Digite o nome do livro: ').strip()
            livro['Categoria']= input('Digite a categoria: ').strip()
            livros.append(livro)
            limpar()
            print('Seu livro foi cadastrado')   
        #salvar o livro em uma biliote
        def salvar():
            arquivo= input('Digite o nome da bilioteca: ').strip()
            with open(fr'{arquivo}.json', 'w', encoding='utf-8')as f:
             json.dump(livros, f, ensure_ascii= False, indent=4)
             print('Livro salvo na biblioteca!')
       
       #listar livros
        def listar():
            arquivo = str(input('Digite a bilioteca: ')).strip()
            with open(fr'{arquivo}.json','r', encoding='utf-8')as f:
                lisste =json.load(f)
                print (f'{lisste}')
        #função para atualizar o livro na biblioteca json, substituindo um livro por outro
        def atualizar():
        
            arquivo = str(input('Digite a biblioteca: ')).strip()
            with open(fr'{arquivo}.json', 'r', encoding='utf-8') as f:
                livros = json.load(f)

            listar()  # mostra a lista antes
            nome = input('Digite o nome do livro que deseja atualizar: ').strip()

            encontrado = False
            for livro in livros:
                if livro['nome'].lower() == nome.lower():  # compara ignorando maiúsculas/minúsculas
                    novo_nome = input('Digite o novo nome do livro: ').strip()
                    nova_categoria = input('Digite a nova categoria: ').strip()
                    livro['nome'] = novo_nome
                    livro['Categoria'] = nova_categoria
                    encontrado = True
                    break
                
            if encontrado:
                with open(fr'{arquivo}.json', 'w', encoding='utf-8') as f:
                    json.dump(livros, f, ensure_ascii=False, indent=4)
                print('Livro atualizado com sucesso.')
            else:
                print('Livro não encontrado.')


        #função para excluir algum livro
        def excluir():
            arquivo = str(input('Digite a biblioteca: ')).strip()
            with open(fr'{arquivo}.json', 'r', encoding='utf-8') as f:
             livros = json.load(f)
        
            listar()
            nome = input('Digite o nome do livro que deseja excluir: ').strip()
        
            encontrado = False
            for livro in livros:
             if livro['nome'].lower() == nome.lower():
                 livros.remove(livro)
                 encontrado = True
                 break


        match escolha:
            case '1':
                cadastrar()            
            case '2':
                salvar()          
            case '3':
                listar()            
            case '4':
                atualizar()             
            case '5':
                excluir()
            case '6':
                print('Saindo do programa...')
                break         
    except Exception as e:
        print('Não é possível realizar essa função!')
        print(e)