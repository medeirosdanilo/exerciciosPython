from random import shuffle
a1 = str(input('1° Aluno '))
a2 = str(input('2° Aluno '))
a3 = str(input('3° Aluno '))
a4 = str(input('4° Aluno '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem de apresentação será \n {}'.format(lista))