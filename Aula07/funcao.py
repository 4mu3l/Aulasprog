#Funções
# crie uma aplicação de bancom, onde o usuário se cadastra e cria 
# uma conta corrente que começa com saldo de R$ 0,00. O usuário terá as opções: 
# Criar conta, Exibir dados da conta, Depositar valor, Sacar valor, encerrar conta. Sair do programa.
import os
import json
saldo = 0
nome = ''
conta = 0
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#criando a conta
def criar_conta():
    global nome, conta
    nome = input('Digite seu nome: ')
    conta = int(input('Digite o número da conta: '))
    limpar()
    print(f'Conta criada com sucesso!\nNome: {nome}\nNúmero da conta: {conta}\nSaldo: R$ {saldo:.2f}')
    salvar_dados() 
#exibir dados da conta
def exibir_dados():
    print(f'Nome: {nome}\nNúmero da conta: {conta}\nSaldo: R$ {saldo:.2f}')
#depositar valor
def depositar_valor():
    global saldo
    valor = float(input('Digite o valor a ser depositado: R$ '))
    if valor > 0:
        saldo += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}')
        salvar_dados() 
    else:
        print('Valor inválido. O depósito deve ser maior que R$ 0,00.')
#sacar valor
def sacar_valor():
    global saldo
    valor = float(input('Digite o valor a ser sacado: R$ '))
    if 0 < valor <= saldo:
        saldo -= valor
        print(f'Saque de R$ {valor:.2f} realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}')
        salvar_dados() 
    elif valor > saldo:
        print('Saldo insuficiente para o saque.')
    else:
        print('Valor inválido. O saque deve ser maior que R$ 0,00.')
#encerrar conta
def encerrar_conta():
    global nome, conta, saldo
    confirmar = input('Tem certeza que deseja encerrar a conta? (s/n): ').lower()
    if confirmar == 's':
        nome = ''
        conta = 0
        saldo = 0
        print('Conta encerrada com sucesso.')
        salvar_dados() 
    else:
        print('Encerramento de conta cancelado.')
#salvar dados em um arquivo json
def salvar_dados():
    dados = {
        'nome': nome,
        'conta': conta,
        'saldo': saldo
    }
    with open('dados_banco.json', 'w') as arquivo:
        json.dump(dados, arquivo)
#ccarregar dados em uma pasta txt em json
def carregar_dados():
    global nome, conta, saldo
    if os.path.exists('dados_banco.json'):
        with open('dados_banco.json', 'r') as arquivo:
            dados = json.load(arquivo)
            nome = dados.get('nome', '')
            conta = dados.get('conta', 0)
            saldo = dados.get('saldo', 0)
#menu principal
def menu():

    print('\n--- Menu do Banco ---')
    print('1. Criar conta')
    print('2. Exibir dados da conta')
    print('3. Depositar valor')
    print('4. Sacar valor')
    print('5. Encerrar conta')
    print('6. Sair do programa')
    escolha = input('Escolha uma opção (1-6): ')
    return escolha

while True:
    limpar()
    escolha = menu()
    carregar_dados()
    match escolha:
        case '1':
            criar_conta()
        case '2':
            exibir_dados()
            input('Pressione Enter para continuar...')
        case '3':
            depositar_valor()
            input('Pressione Enter para continuar...')
        case '4':
            sacar_valor()
            input('Pressione Enter para continuar...')
        case '5': 
            encerrar_conta()
            input('Pressione Enter para continuar...')
        case '6':
            print('Saindo do programa...')
            break
        case _:
            print('Opção inválida. Tente novamente.')
            input('Pressione Enter para continuar...')