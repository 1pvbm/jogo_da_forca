import random
from time import sleep

palavras = ['brasil', 'estados unidos', 'portugal', 'alemanha', 'grecia', 'japao', 'china','russia','australia','chile',
            'canada','italia']

def escolher_palavra(palavras):
    return random.choice(palavras)

print('<<<< Bem vindo ao jogo da forca >>>> ')
sleep(3)
print('Acerte a palavra e ganhe !!!')
print('Serão 6 tentativas, cada erro uma tentativa a menos!')
sleep(5)
print('Após as 6 tentativas >FALHAS< você estará...')
sleep(4)
print('ENFORCADO !!!! ')
sleep(2)
print('Vamos começar...')
sleep(1)
print('Carregando a palavra...')
sleep(2)

def jogar_forca(palavra):
    palavra_escondida = '_' * len(palavra)
    tentativas = 6
    letras_usadas = []

    while True:
        desenhar_forca(tentativas)
        print('Palavra: ', palavra_escondida)
        letra = input('Escolha sua letra : ').lower()

        if letra in letras_usadas:
            print(f'Você ja tentou a letra "{letra}", tente novamente!')
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            print('VOCÊ ACERTOU UMA LETRA !!!!')
            nova_palavra_escondida = ''
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    nova_palavra_escondida += letra
                else:
                    nova_palavra_escondida += palavra_escondida[i]
            palavra_escondida = nova_palavra_escondida
        else:
            print('Que pena, você errou a letra!')
            tentativas -= 1

        print('Letras usadas: ' + ', '.join(letras_usadas))
        print('Tentativas restantes: ' + str(tentativas))

        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra correta era: ' + palavra)
            break

def desenhar_forca(tentativas):
    etapas_forca = [
        '''
           --------
           |      |
           |
           |
           |
           |
        ====
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
        ====
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |
           |
        ====
        ''',
        '''
           --------
           |      |
           |      O
           |     /|
           |
           |
        ====
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\ 
           |
           |
        ====  
        '''
        ,
        '''
           --------
           |      |
           |      O
           |     /|\ 
           |     /
           |
        ====
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\ 
           |     / \ 
           |
        ==== 
        '''
    ]

    print(etapas_forca[6 - tentativas])

def main():
    palavra = escolher_palavra(palavras)
    jogar_forca(palavra)


