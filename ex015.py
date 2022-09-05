km = int(input('Qual a kilometragem percorrida? '))
dias = int(input('Quantos dias de aluguel do veículo?'))

total = (dias * 60) + (km * 0.15)

print('Total a pagar: R${:.2f}'.format(total))



