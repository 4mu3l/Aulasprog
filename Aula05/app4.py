# biblioteca
import os

# loop
while True:
    try:
        # titulo
        print(30*"-","Manipulação de arquivo",30*"-")

        # usuario digita o texto e cira um arquivo
        novo_texto = input("Digite o texto: ")
        novo_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip().lower()

        # abre o aarquivo
        with open(fr"C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula05/{novo_arquivo}.txt","w",encoding="utf-8") as f:
            # escreve o texto no arquivo
            f.write(novo_texto)

        os.system("cls" if os.name == "nt" else "clear")
        print(f"{novo_arquivo}.txt foi gravado com sucesso!!")

        #novo texto
        novo_texto_adicionar= input('Digite o novo texto: \n')
        with open(fr"C:\Users\SamueldosSantosRodri\logicaprogramaçãoaulas\Aula05/{novo_arquivo}.txt","a",encoding="utf-8") as f:
            f.write(f'\n{novo_texto_adicionar}')
        print('Gravado com sucesso.')
        #ler os daddos atualizados
        
        with open(f'{novo_arquivo}.txt', 'r', encoding= 'utf-8') as f:
            texto_final=f.read()
        print(f'Texto final: {texto_final}')

        # loop 2
        while True:
            prosseguir = input("Deseja abrir outro arquivo? (s/n): ").lower()
            
            # se prosseguir for sim
            if prosseguir == "s" or "n":
                break
            else:
                print("Opção invalida!")
                continue
        
        match prosseguir:
            case "s":
                continue
            case "n":
                print("Saindo...")
                break
    except Exception as e:
        print(f"ERROR!!\nErro: {e}")