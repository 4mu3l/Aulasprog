# 17 Solicite um valor principal, a taxa de juros e o tempo, e exiba o valor dos juros simples.
#NOTE - variaveis 
valor = float(input("Digite o valor principal: "))
taxa = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo (em anos): "))
#NOTE - calculo para encontar o valor do juros
juros_simples = valor * (taxa / 100) * tempo
print(f"O valor dos juros simples: {juros_simples}") 