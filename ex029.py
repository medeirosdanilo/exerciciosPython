vel = int(input('Informe a velocidade atual do veículo '))
perm = 80
cont = vel - perm
if cont >= 1:
    print('Você foi multado em R${}'.format(cont * 7))
else:
    print('Parabéns, você está dentro do limite permitido!')