'''
digite seu nome 
digite sua idade 
escolha o filme
escolha o horario
legendado ou dublado
qualidade da sala
pode entrar ou não
se não pode entrar repete a escolha do filme
'''

while True:
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))
    #escolher um filme 
    print(40*"-", "Próxima página", 40* "-")
    print("Escolha um filme:")
    print('1 - Quarteto fantástico (12)')
    print('2 - Piece by piece (14)')
    print('3 - Premonição 6 (18)')
    print('4 - Os caras malvados 2 (L)')
    print('5 - Como treinar seu dragão (10)')
    print('6 - Deadpool 2 (16) ')
    print('Cancelar')
    opcao=str(input("Digite uma opção "))
    if opcao== '1':
        FT4 = 12
        if idade >= FT4:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '2':
        PYP = 14
        if idade >= PYP:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '3':
        P6 = 18
        if idade >= P6:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '4':
        CM = 0
        if idade >= CM:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '5':
        CD = 10
        if idade >= CM:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '6':
        DP = 16
        if idade >= DP:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== 'cancelar':
        print('Operação cancelada')
        break

'''
while True:
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))
    ft4= 12 
    pyp= 14
    P6= 18
    cm= 0
    D= 10
    dp= 16
    #escolher um filme 
    print(40*"-", "Próxima página", 40* "-")
    print("Escolha um filme:")
    print('1 - Quarteto fantástico (12)')
    print('2 - Piece by piece (14)')
    print('3 - Premonição 6 (18)')
    print('4 - Os caras malvados 2 (L)')
    print('5 - Como treinar seu dragão (10)')
    print('6 - Deadpool 2 (16) ')
    print('Cancelar')
    opcao=str(input("Digite uma opção "))
    if opcao== '1':
        print('escolha um filme:')
        print ('1 - Quarteto fantástico (12)| 6 -Deadpool 2 (16)')
        if idade>= 16:
            if opcao== '1':
                if idade >= ft4:
                 print('Sua sessão foi comprada')
            elif opcao == "6": 
                if idade >= dp:

                  FT4 = 12
        if idade >= FT4:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '2':
        PYP = 14
        if idade >= PYP:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '3':
        P6 = 18
        if idade >= P6:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '4':
        CM = 0
        if idade >= CM:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '5':
        CD = 10
        if idade >= CM:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== '6':
        DP = 16
        if idade >= DP:
            print(f"Senhor(a) {nome} seu ingreso foi comprado")
            break
        else:
            print(f'Senhor(a) {nome} você não pode assistir a esse filme')
    elif opcao== 'cancelar':
        print('Operação cancelada')
        break
'''