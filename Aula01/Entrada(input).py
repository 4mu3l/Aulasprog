print()
print (30*"-", "Entrada de Dados", 30*"-")

nome_usu = input ("Digite o seu nome:")
print("Seja Bem-Vindo", nome_usu)

print (30*"-", "Calculadora", 30*"-")
num1 = int(input("Digite algum numero:"))
num2 = int(input("Digite algum numero:"))
#Tipos de dados
#float = numeros reais, ou seja, tem ",", exemplo: 5.20
#int = numeros inteiros 
#str = texto, conjunto de caracteres 
#bool valores logicos como True e False 

soma = num1 + num2
divi = num1 / num2
mult = num1 * num2
sub = num1 - num2
divi_int = num1 // num2
expo = num1 ** num2

print ("Reusltado da soma ",num1,"+", num2, "é:",soma)
print ("Reusltado da divisão ",num1,"/", num2, "é:",divi)
print ("Reusltado da multiplicação ",num1,"*", num2, "é:",mult)
print ("Reusltado da subtração ",num1,"-", num2, "é:",sub)
print ("Reusltado da exponencial ",num1,"**", num2, "é:",expo)
print(50*"-")
print(nome_usu,"esses são os resultados, espero ter ajudado")