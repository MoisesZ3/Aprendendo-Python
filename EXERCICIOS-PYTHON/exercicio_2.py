#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura
#if else para determinar se o número é par ou ímpar.

print('Vamos ver se seu número escolhido e par ou impar\n')
numero = int(input('Escolha um numero: '))

if numero < 0:
    print(f'O numero {numero} é impar')
elif numero > 0:
    print(f'O numero {numero} é par')
else:
    print('Seu número é zero(0)')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura
#if elif else para classificar a idade em categorias de acordo com as seguintes
#condições:
# - Criança: 0 a 12 anos;
# - Adolescente: 13 a 18 anos;
# - Adulto: acima de 18 anos.

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print(f'Com a idade {idade} você é considerado criança')
elif idade >= 13 and idade <= 18:
    print(f'Com a idade {idade} você é considerado adolescente')
elif idade > 18:
    print(f'Com a idade {idade} você é considerado adulto')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para
#verificar se o nome de usuário e a senha fornecidos correspondem aos valores
#esperados determinados por você.
print('vamos nos cadastrar')

nome_cadastro = input('Digite um nome de sua escolha')
senha_cadastro = input('Digite uma senha de sua escolha')

print('vamos nos logar agora')

nome_login = input('Digite seu nome')
senha_login = input('Digite sua senha')

if nome_login == nome_cadastro and senha_login == senha_login:
    print('Acesso liberado, bem vindo!')
else:
    print('Acesso negado')    

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize
#uma estrutura if elif else para determinar em qual quadrante do plano
# - cartesiano o ponto se encontra de acordo com as seguintes condições:
# - Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# - Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# - Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# - Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# - Caso contrário: o ponto está localizado no eixo ou origem.

print('''
      Digite uma coordenada para um plano cartesiano
      e te mostraremos em que quadrante ficou esse ponto
''')

numeroX = input('Digite o valor X')
numeroY = input('Digite o valor Y')

if numeroX > 0 and numeroY > 0:
    print('''
          Seu ponto esta nesse quadrante

                    |
                    |   o
                    |
             -------+-------
                    |
                    |
                    |
''')
elif numeroX < 0 and numeroY > 0:
    print('''
          Seu ponto esta nesse quadrante

                    |
                o   |
                    |
             -------+-------
                    |
                    |
                    |
''')
elif numeroX < 0 and numeroY < 0:
    print('''
          Seu ponto esta nesse quadrante

                    |
                    |
                    |
             -------+-------
                    |
                o   |
                    |
''')
elif numeroX < 0 and numeroY > 0:
    print('''
          Seu ponto esta nesse quadrante

                    |
                    |
                    |
             -------+-------
                    |
                    |   o
                    |
''')
else:
    print('''
          Seu ponto esta na origem

                    |
                    |
                    |
             -------o-------
                    |
                    |
                    |
''')