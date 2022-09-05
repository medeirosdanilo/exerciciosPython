frase = str(input('Escreva uma frase qualquer ')).upper().strip()
print('A letra "A" aparece {} vezes '.format(frase.count('A')))
print('"A" aparece pela primeita vez na posição {}'.format(frase.find('A')))
print('A ultima vez que a letra "A" aparece é na posição {}'.format(frase.rfind('A')))