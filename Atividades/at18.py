# 18 Peça dois números e verifique se são diferentes.
#FIXME - impotação
import os
#variaveis
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#se o numero for diferente
if num1 != num2:
    limpar()
    print('Os números não são iguais.')
#se o numero for igual
else:
    limpar()
    print('ERRO! NÚMEROS iguais.')