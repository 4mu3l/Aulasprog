# 23 Solicite um número e exiba o valor absoluto

#variaveis
num = float(input("Digite um número: ").replace(',','.'))
#mostrando o valor absoluto
valor_absoluto = abs(num)

print(f"O valor absoluto de {num} é: {valor_absoluto}")