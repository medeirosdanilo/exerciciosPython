prod = float(input('Qual o preço do produto sem descontos? '))
desc = (prod * 5) / 100
print('O novo preço do produto com 5% de desconto é R${:.2f}'.format(prod - desc))
