# 20 Receba um valor em metros do usuário. Converta o valor para centímetros, milímetros e quilômetros. Exiba os resultados.
#variaveis
metros = float(input("Digite um valor em metros: ").replace(',', '.'))
#calculos para conversao
cm = metros * 100  
mm = metros * 1000
km = metros / 1000
#exibindo os resultados
print(f"{metros}m em cm é {cm}cm, em milímetros é {mm}mm e em quilômetros é {km}km.")