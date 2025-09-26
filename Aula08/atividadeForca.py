import random
import os
def escolher_palavras(escolha):
    palavras=['python', 'developer', 'programação','inteligencia artificial', 'java', 'algoritmo',
         'computador','linguagens de programação','software', 'mouse', 'teclado', 'memoria', 'notebook',
         'garoto de programa', 'programador', 'cooler', 'disco', 'gabinete']
    return random.choice(palavras)
def menu():
    print('1 - Animais')
    print('2 - Comida')
    print('3 - objetos da cozinha')
    escolha=input('Escolha uma das opções ')

def jogar_forca():
    palavra =escolher_palavras()
    letras_corretas=[]
    letras_erradas=[]
    tentativas= 6

    while True:
        palavra_escondida= ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida+= letra
            else:
                palavra_escondida += '_'
        print('Palavra escondida', palavra_escondida)
        print('Letras erradas', letras_erradas)
        print('tentativas', tentativas)

        if palavra_escondida==palavra:
            print('Você ganhou ')
            break
        elif tentativas==0:
            print('Você perdeu, a palara era, ',palavra)
            break
        letra_usuario = input('Digite uma letra ').lower()
       
        if letra_usuario in palavra:
            print('Letra correta ')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra errada')
            letras_erradas.append(letra_usuario)
            tentativas -= 1 
if __name__=='__main__':
    os.system('cls')
    print('Bem vindo')
    jogar_forca()