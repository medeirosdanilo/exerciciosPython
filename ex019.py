from random import choice
print('+++++Quem apaga o quadro?+++++')
a1 = input('Nome do 1° Aluno? ')
a2 = input('Nome do 2° Aluno? ')
a3 = input('Nome do 3° Aluno? ')
a4 = input('Nome do 4° Aluno? ')
lista = [a1, a2, a3, a4]
sort = choice(lista)
print('O aluno escolhido foi {}'.format(sort))





