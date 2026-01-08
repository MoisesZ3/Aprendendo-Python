#1 - Crie uma lista para cada informação a seguir:
#    - Lista de números de 1 a 10;
#    - Lista com quatro nomes;
#    - Lista com o ano que você nasceu e o ano atual.
numeros = [1,2,3,4,5,6,7,8,9,10] 
nomes = ['Moisés','Danilo','Arthur','Gabriel']
ano = [2005,2026]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for nome in nomes:
    print(f'Nomes: {nome}\n')

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
numeros_impares = []
for numero in numeros:
    calculo = numero % 2

    if calculo != 0:
        numeros_impares.append(numero)

soma_impares = sum(numeros_impares)
print(soma_impares)

        
#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for numero in range(10, 0, -1):
    print(numero)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_escolha = int (input('Escolha um número para calcularmos a tabuada: '))

for numero in range(1, 11):
    calculo_tabuada = numero * numero_escolha
    resultado = f'{numero_escolha} x {numero} = {calculo_tabuada}'
    print(resultado)

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [80, 189, 5, 160, 08, 45, 91, 1]
soma = 0
try:
    for numero in lista_numeros:
        soma += numero
    
    print(soma)

except TypeError:
    print('A lista contém um valor que não é um número')


#7 - Construa um código que calcule a média dos valores em uma lista.
#Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
try:
    for numero in lista_numeros:
        numero += numero
    quantidade = len(lista_numeros)
    
    media = soma / quantidade
    print(media)

except ZeroDivisionError:
    print("Erro: A lista está vazia, não é possível calcular a média (divisão por zero).")