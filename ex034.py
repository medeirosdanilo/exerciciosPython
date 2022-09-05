sal = float(input('Informe o salário do funcionário '))

if sal > 1250:
    aumento = sal * 10 / 100
    porc = 10
else:
    aumento = sal * 15 / 100
    porc = 15

print('O salário atual do funcionário é R${:.2f} e com o aumento de {}% passará a ser de R${:.2f} '.format(sal, porc, sal + aumento))
