from random import randint
numero = randint(0,5)
print('O Computador pensou em um número entre 0 e 5!\n Tente advinhar qual o número escolhido.')
choose = int(input('Dê seu palpite '))
if choose == numero:
    print('PARABÉNS, você VENCEU!')
else:
    print('O Computador VENCEU!')

print('O número escolhido pelo computador foi {}'.format(numero))


