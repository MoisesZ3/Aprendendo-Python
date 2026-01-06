#1 - Crie uma lista para cada informação a seguir:
#    - Lista de números de 1 a 10;
#    - Lista com quatro nomes;
#    - Lista com o ano que você nasceu e o ano atual.
numeros = [1,2,3,4,5,6,7,8,9,10] 
nomes = ['Moisés','Danilo','Arthur','Gabriel']
ano = [2005,2026]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos
#da lista.
for nome in nomes:
    print(f'Nomes: {nome}\n')

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
numeros_impares = []
for numero in numeros:
    calculo = numero % 2

    if calculo != 0:
        numeros_impares.append(numero)

soma = sum(numeros_impares)
print(soma)
        

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.



#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para
#imprimir a tabuada desse número, indo de 1 a 10.

#6 - Crie uma lista de números e utilize um loop for para calcular a soma
#de todos os elementos. Utilize um bloco try-except para lidar com possíveis
#exceções.

#7 - Construa um código que calcule a média dos valores em uma lista.
#Utilize um bloco try-except para lidar com a divisão por zero,
#caso a lista esteja vazia.
