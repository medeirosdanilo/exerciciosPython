from math import pow, sqrt
print('A respeito de um Triângulo Retângulo, informe...')
compCatOp = int(input('Qual o comprimento do cateto oposto? '))
compCatAdj = int(input('Qual o comprimento do cateto adjacente?'))

potCatOp = pow(compCatOp, 2)
potCatAdj = pow(compCatAdj, 2)

som = potCatOp + potCatAdj

hip = sqrt(som)


print('O comprimento da hipotenusa é {:.0f}'.format(hip))

