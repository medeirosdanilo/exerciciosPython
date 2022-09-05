dist = int(input('Qual a distância da viagem em km'))

if dist <= 200:
    print('O valor da sua viagem ficou em R$ {:.2f}'.format(dist * 0.5))
else:
    print('O valor da viagem ficou em R$ {:.2f}'.format(dist * 0.45))
