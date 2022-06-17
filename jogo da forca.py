# jogo da forca
palavra = 'abcd'
tentativa = ''

while tentativa != palavra:
    letra = input('Digite uma letra p/ a forca: ').strip().lower()
    if letra.isalpha() == True:
        if len(letra) == 1:
            if letra in tentativa:
                print('Você já chutou essa letra.')
            else:
                if letra in palavra:
                    print('Temos essa letra')
                    tentativa += letra
                else:
                    print('Errou! Não temos essa letra.')
        else:
            print('Erro! Apenas uma letra.')
    else:
        print('Erro! Apenas letras.')
print("PARABÉNS! Você completou a FORCA! Fim do jogo!")
