# biblioteca
import os

# loop do menu
while True:

    # limpa o sistema
    os.system("cls")

    # menu e titulo
    print(30*"-","MENU",30*"-")
    print("1 - Gerenciar nomes")
    print("2 - Ordenar números")
    print("3 - Calcular média de notas")
    print("4 - Sair")
    print()

    # usuário escolhe
    escolha = str(input("Escolha uma opção: "))

    # 1-gerenciar nomes
    if escolha == "1":
        # lista de nomes
        lista = []

        #loop
        while True:
            # limpa o sistema
            os.system("cls")

            # menu do 1
            print("\n--- MENU NOMES ---")
            print("1 - Incluir nome")
            print("2 - Pesquisar nome")
            print("3 - Alterar nome")
            print("4 - Excluir nome")
            print("5 - Listar nomes")
            print("6 - Voltar ao menu principal")

            # usuario escolhe
            opcao = str(input("Escolha uma opção: "))

            #se incluir
            if opcao == "1":
                # usuario digita o nome
                nome = input("Digite o nome para incluir: ")

                # adiciona o nome no inicio da lista
                lista.append(nome)
                print("Nome incluído com sucesso!")
                input("Pressione ENTER para continuar...")

            # se pesquisar
            elif opcao == "2":
                # usuario digita o nome
                nome = input("Digite o nome para pesquisar: ")

                # verificando se o nome digitado esta na lista
                if nome in lista:
                    print("Nome encontrado!")
                # se nao encontrar
                else:
                    print("Nome não encontrado.")
                input("Pressione ENTER para continuar...")

            # se alterar
            elif opcao == "3":
                # usuario digita o nome que quer alterar
                nome = input("Digite o nome que deseja alterar: ")

                # verifica se o nome esta na lista
                if nome in lista:
                    # usuario digita o novo nome
                    novo_nome = input("Digite o novo nome: ")

                    # codigo para selecionar o nome antigo
                    troca = lista.index(nome)

                    # substitui o nome antigo pelo escolhido
                    lista[troca] = novo_nome
                    print("Nome alterado com sucesso!")

                # se nao estiver o nome na lista
                else:
                    print("Nome não encontrado.")
                input("Pressione ENTER para continuar...")

            # se excluir
            elif opcao == "4":
                # usuario digita o nome que quer excluir
                nome = input("Digite o nome que deseja excluir: ")

                # se o nome estiver na lista
                if nome in lista:
                    # remove o nome da lista
                    lista.remove(nome)
                    print("Nome excluído com sucesso!")

                # se o nome nao estiver na lista
                else:
                    print("Nome não encontrado.")
                input("Pressione ENTER para continuar...")

            # se quer mostra todos
            elif opcao == "5":
                # mostra os nomes da lista
                print("Lista de nomes:", lista)
                input("Pressione ENTER para continuar...")

            # se quiser sair
            elif opcao == "6":
                break

            # se digitar algo invalido
            else:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")

    # 2-ordenar numeros
    elif escolha == "2":
        # lista de numeros digitados
        numeros = []

        # loop
        while True:
            # limpar sistema
            os.system("cls")

            #usuario digita um numero ou deixa em branco para encerrar
            valor = input("Digite um número (ou aperte ENTER para encerrar): ")

            # se usuario escolher encerrar
            if valor == "":
                break

            # tenta adicionar o numero na lista
            try:
                # apenas numero inteiros sao adicionados
                numeros.append(int(valor))

            # se oque for digitado nao for um numero
            except ValueError:
                print("Digite apenas números!")
                input("Pressione ENTER para continuar...")

        # codigo para colocar os numeros em ordem crescente
        numeros.sort()

        # mostra os numeros
        print("Números em ordem crescente:", numeros)
        input("Pressione ENTER para voltar ao menu principal...")

    # 3-lista de notas
    elif escolha == "3":

        # lista de notas
        notas = []

        # contagem de bimestre
        contagem = 4

        # loop
        while contagem > 0:
            # limpar o sistema
            os.system("cls")

            # usuario digita a nota
            valor = input("Digite uma nota (0 a 10): ")

            # tenta adicionar a nota na lista de nota
            try:
                # transforma o numero inserido em um numero real
                nota = float(valor)

                # a nota inserida so pode ser entre 0 e 10
                if 0 <= nota <= 10:
                    # adiciona a nota na lista
                    notas.append(nota)

                    # diminui a contegem em 1
                    contagem -= 1

                # se a nota nao for um numero entre 0 e 10
                else:
                    print("A nota deve estar entre 0 e 10.")
                    input("Pressione ENTER para continuar...")

            # se a nota nao for um numero
            except ValueError:
                print("Digite apenas números.")
                input("Pressione ENTER para continuar...")

        # tira a media das notas
        # SUM soma a lista de notas
        # LEN e a quantidade de notas que tem na lista99
        media = sum(notas)/len(notas)

        # mostra a media com apenas dois numeros depois da virgula
        print(f"Média do aluno: {media:.2f}")
        input("Pressione ENTER para continuar")

        # se o aluno tirou acima ou igual a 7
        if media >= 7:
            print("Aluno APROVADO")

        # se nao
        else:
            print("Aluno REPROVADO")

    # 4-sair
    elif escolha == "4":
        print("Encerrando programa...")

        # sai do loop do programa
        break

    # numero invalido
    else:
        print("Opção inválida!")
        input("Pressione ENTER para continuar...")