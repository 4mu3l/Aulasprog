import os
while True:
    try:
        os.system('cls')
        #Entrada de dados
        etanol= float(input('Digite o valor da etanol: ')).replace(',', '.')
        gasolina= float(input('Digite o valor da gasolina: ')).replace(',', '.')
        calculo= (etanol/gasolina)*100
        resultado= 'Gasolina' if calculo > 70 else 'etanol'
        print(f'Resultado = {calculo: 2f}%. Compensa abastecer com {resultado}.')
        opcao= input('Deseja refazer o calculo? (S/N): ').lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print(f'Opção inválida')
                continue
    except Exception as e:
        print(f'Não foi possível executar a operação. {e}')