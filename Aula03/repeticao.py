'''
Problema: crie um sistema que calcule o indice de masssa corporal(IMC) do usuario, 
mostre o valor do imc na tela, e retorne se o usuario esta no peso ideal ou se precisa 
emagrecer ou engordar mais. utilize a tabela do imc para definir os valores
'''
'''
print(40*"-", "CALCULADORA IMC",40*"-")
while True:
    nome= str(input('Digite seu nome '))
    altura= float(input(f"{nome} Digite sua altura ").replace(',','.'))
    peso= float(input("{nome} Digite o seu peso ").replace(',','.'))
    imc= peso/(altura * altura)
    print(f"{nome} IMC é: {imc:.2f}")
    if imc <= 18.5:
        print('{nome} esta com Abaixo do normal')
    elif imc <= 24.9:
        print(f"{nome} está normal")
    elif imc <= 29.9:
        print(f"{nome} está Sobrepeso")
    elif imc <= 34.9:
        print(f"{nome} está Obesidade grau 1")
    elif imc <= 39.9:
        print(f"{nome} está Obesidade grau 2")
    else:
        print(f"{nome} está com Obesidade grau 3, o ultimo sobrevivente")
    opcao= input("Deseja calcular novamente? S- sim|N- não): ").lower()
    if opcao=='s':
        continue
    elif opcao== "n":
        print("Saindo do sistema")
        break
'''
#ANCHOR - Problema 2: Um elevador de carga possui capacidade para 200kg. 
#Crie um programa que receba do usuario seu peso e o peso da carga e 
#verifca se a carga está aitorizada a usar o elevador.
#NOTE - loop
'''
limite= 200
peso= float(input("Informe seu peso ").replace(',','.'))
pcarga=float(input("Informe seu peso da carga ").replace(',','.'))
pesoT= peso + pcarga
if pesoT >= limite:
    print("Você não pode entrar no elvador, vá pelas escadas")
else:
    print("Você pode usar o elevador, parabéns")
'''
#ANCHOR - looop
#ANCHOR - NÃO USE 
'''
numero=10
while numero>= 0:
    print("KKKKKKK")
'''
#FIXME - Existe  o while cont
#FIXME - Break
'''
while True:
 # menu principal
  print(40*'-','sistema console 2° DS',40*'-')
  print('1 - calculadora de IMC')
  print('2 - Maioridade')
  print('3 - calculaddora')
  print('4 - Dados pessoais')
  print('5 - Feliz natal')
  print('6 - sair')
  opcao=str(input("Digite uma opção "))
  if opcao=='1':
        pass
  elif opcao=="2":
        ...
  elif opcao=="3":
        ...
  elif opcao=="4":
        ...
  elif opcao=="5":
        linha=15
        j=1
        while j<= linha:
            espacos=linha-j
            estrelas= 2 * j - 1
            print(" " * espacos+ "^" * estrelas)
            j+=1
  elif opcao=="6":
       ('saindo sistema')
       break
  else:
       ("Opção inválida")
'''
'''
while True:
  nome=input("Digite seu nome: ")
  cpf= input("Digite seu cpf: ")
  tel= input("Digite seu numero de telefone: ")
  nasc=int(input ("Digite o ano do seu nascmento: "))
  anoat= 2025
  idade = anoat - nasc
 # menu principal
  print(40*'-','sistema console 2° DS',40*'-')
  print('1 - calculadora de IMC')
  print('2 - Maioridade')
  print('3 - calculaddora')
  print('4 - Dados pessoais')
  print('5 - Feliz natal')
  print('6 - sair')
  opcao=str(input("Digite uma opção "))
  if opcao=='1':
    while True:
        altura= float(input(f"{nome} Digite sua altura ").replace(',','.'))
        peso= float(input("{nome} Digite o seu peso ").replace(',','.'))
        imc= peso/(altura * altura)
        print(f"{nome} IMC é: {imc:.2f}")
        if imc <= 18.5:
            print(f'{nome} esta com Abaixo do normal')
        elif imc <= 24.9:
            print(f"{nome} está normal")
        elif imc <= 29.9:
            print(f"{nome} está Sobrepeso")
        elif imc <= 34.9:
            print(f"{nome} está Obesidade grau 1")
        elif imc <= 39.9:
            print(f"{nome} está Obesidade grau 2")
        else:
            print(f"{nome} está com Obesidade grau 3, o ultimo sobrevivente")
        opcao= input("Deseja calcular novamente? S- sim|N- não): ").lower()
        if opcao=='s':
            continue
        elif opcao== "n":
            print("Saindo do sistema")
            break
  elif opcao=="2":
        if idade>=18:
         print (f"{nome},é maior de idade.")
        else:
            print("Você é menor de idade")
  elif opcao=="3":
        while True:
             print("Calculadora")
             print("1- soma")
             print("2- divisão")
             print("3- subtração")
             print("4- multiplicação")
             opcao_calculo= input("Escolha uma das operações: ")

             num1= float(input("Digite o primeiro número: "))
             num2= float(input("Digite o segundo número: "))
             if opcao_calculo=="1":
                  print(f"Resultado da soma é {num1 + num2}")
             elif opcao_calculo=="2":
                  print(f"O resultado da divisão é {num1/num2}")
             elif opcao_calculo== "3":
                  print(f"O resultado da subtração é {num1 - num2}")
             elif opcao_calculo=="4":
                  print(f"O resultado da multiplicação é {num1 * num2}")
             elif opcao_calculo== "5":
                  print("sair")
                  break
  elif opcao=="4":
        print(f"|Nome: {nome}|cpf: {cpf}")
        print(f"telefone: {tel}|nascmento: {nasc}")
  elif opcao=="5":
        linha=1
        j=1
        while j<= linha:
            espacos=linha-j
            estrelas= 2 * j - 1
            print(" " * espacos+ "^" * estrelas)
            j+=1
  elif opcao=="6":
       ('saindo sistema')
       break
  else:
       ("Opção inválida")
'''

nome='gomes'
for i in nome:
    print(i.replace(i, "*"))