nomeComp = str(input('Insira um nome completo: ')).strip()

print('O Nome em letras maiúsculas: {}'.format(nomeComp.upper()))
print('O Nome em letras minúsculas: {}'.format(nomeComp.lower()))
print('O Nome possui {} letras.'.format(len(nomeComp) - nomeComp.count(' ')))
separado = nomeComp.split()
print('O Primeiro nome é {} e possui {} letras.'.format(separado[0], len(separado[0])))
