#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dados = {'nome' : 'Moisés', 'idade' : '19', 'cidade' : 'Porto Alegre'}  

#2 - Utilizando o dicionário criado no item 1:

#   - Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#   - Adicione um campo de profissão para essa pessoa;
#   - Remova um item do dicionário.

print(dados)
dados.update({'idade' : '20'})
print(dados)
dados.update({'profição' : 'dev'})
print(dados)
dados.pop('profição')
print(dados)

#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {1 : 1**2, 2 : 2**2, 3 : 3**2, 4 : 4**2, 5 : 5**2}
print(quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
if 'nome' in dados:
    print('A key existe')
else:
    print('A key não existe')

if 'profição' in dados:
    print('A key existe')
else:
    print('A key não existe')

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
