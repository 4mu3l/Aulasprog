#importando a biblioteca json e os para manipulação de arquivos e sistema operacional
import json
import os
#variaveis
usuarios = []
novo_arquivo = ''
#variavel para limpar a tela
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#laço para salvar os usuarios
while True:
    #opcões do sistema
    usuario = {}
    print('1 - Cadastrar novo usuario.')
    print('2 - Salvar arquivo JSON.')
    print('3 - Fazer leitura do JSON.')
    print('4 - deletar arquivo JSON')
    print('5 - Sair do sistema.')
# usuario escolhe a opcão
    opcao = input('Informe a opção desejada: ')
    limpar()
#match case para as opções
    match opcao:
    #o usuario informa seu nome, idade e email
        case '1':
            usuario['nome'] = input('Informe o nome: ').strip().title()
            usuario['idade'] = input('Informe a idade: ')
            usuario['email'] = input('Informe o email: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso')
            continue
    #o usuario informa o nome do arquivo que deseja salvar
        case '2':
            novo_arquivo = input('Informe o nome do arquvio: ').strip().lower()
          
            if novo_arquivo:
                with open(fr'C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula06/{novo_arquivo}.json','w', encoding= 'utf-8') as f:
                 dados_existentes = json.load(f)
            dados_existentes.append(usuarios)
            
            with open(fr'C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula06/{novo_arquivo}.json','w', encoding= 'utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            limpar()
            print('Arquivo salvo com sucesso!')
            continue
        case'3':
    #o usuario informa o nome do arquivo que deseja ler
            if not novo_arquivo:
                novo_arquivo= input('Digite o nome do arquivo: ').strip().lower()
                with open(fr'C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula06/{novo_arquivo}.json','r', encoding= 'utf-8') as f:
                    dados = json.load(f)
                print(f'{"-"*20} USUARIOS {"-"*20}')
                for usuario in dados:
                    for chave in usuario:
                        print(f'{chave.capitalize()}: {usuario.get(chave)}')
                    print('-'*40)
                continue
        case '4':
        #o usuario informa o nome do arquivo que deseja deletar
            if not novo_arquivo:
                novo_arquivo= input('Digite o nome do arquivo: ').strip().lower()
            os.remove(fr'C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula06/{novo_arquivo}.json')
            print('Arquivo deletado com sucesso!')
            continue
        case '5':
         # o sistema é encerrado
            print('Saindo do sistema...')
            break