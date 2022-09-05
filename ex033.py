n1 = int(input('Informe o 1° número '))
n2 = int(input('Informe o 2° número '))
n3 = int(input('Informe o 3° número '))
maior = 0
menor = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if menor > n3:
    menor = n3
print('O MAIOR número digitado é o {}'.format(maior))
print('O MENOR número digitado é o {}'.format(menor))
