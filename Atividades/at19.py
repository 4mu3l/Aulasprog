# 19 Peça três números e verifique se o primeiro é maior que o segundo e menor que o terceiro.


#NOTE - importação 
import os
#variaveis
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
num1= input("Digite o primeiro número: ")
num2= input("Digite o segundo número: ")
num3= input("Digite o terceiro número: ")
limpar()
#condição
if num1 > num2 and num1 < num3:
    print(f"O número {num1} é maior que {num2} e menor que {num3}.")
else:
    print(f"O número {num1} não é maior que {num2} e menor que {num3}. Desculpe.")