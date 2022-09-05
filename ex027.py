nomeCompl = str(input('Informe um nome ')).strip()
nome = nomeCompl.split()
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu último nome é {} '.format(nome[len(nome)-1]))


