# 22 Peça a distância percorrida e o combustível gasto, e exiba o consumo médio do veículo.
while True:
    try:
        #variaveis
        dist = float(input("Digite a distância percorrida (em km): ").replace(',','.'))
        combs = float(input("Digite o combustível gasto (em l): ").replace(',','.'))
        #calculo
        consumo_medio = dist / combs

        print(f"O consumo médio do veículo é: {consumo_medio} km/l")
        break   

    except Exception as e:
        print("Erro na entrada de dados. Por favor, insira valores numéricos válidos.")
        print(f"Detalhes do erro: {e}")
        continue
