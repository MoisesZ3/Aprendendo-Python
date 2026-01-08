#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
venda_macas = input('Quantas maças foram vendidas hoje: ')
venda_bananas = input('Quantas bananas foram vendidas hoje: ')

if venda_macas > venda_bananas:
    print('As maças tiveram mais vendas hoje.')
elif venda_bananas > venda_macas:
    print('As bananas tiveram mais vendas hoje.')
else:
    print('As vendas de maça e banana foram iguais hoje.')

#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
atividade_A = int(input('\nInforme os dias para a atividade A: '))
atividade_B = int(input('Informe os dias para a atividade B: '))
atividade_C = int(input('Informe os dias para a atividade C: '))

if atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0:
    calculo = atividade_A + atividade_B + atividade_C
    print(f'Ira demorar {calculo} dias para terminar todas as atividades')
else:
    print('Erro, os dias não podem ser negativos.')

#programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura_sala = int(input('\nDigite a temperatura atual: '))

if temperatura_sala > 25:
    print('Alerta, temperatura acima do limite permitido.')
else:
    print('A temperatura da sala se mantem no limite permitido.')

#O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

peso = int(input('\nDigite seu peso em kilos: '))
altura = float(input('Digite sua altura em metros:'))
IMC = peso / (altura ** 2)

if IMC < 18.5: 
    print('Você está abaixo do peso.')
elif 18.5 <= IMC < 25: 
    print('Você está com peso normal.')
elif IMC >= 25: 
    print('Você está acima do peso.')

#O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
gastos_mes = float(input('\nDigite o total de despesas do mês(R$): '))

if gastos_mes >= 3000.00:
    print('Atenção, você ultrapassou o limete do orçamento.')
elif gastos_mes < 3000.00:
    print('Você esta dentro do orçamento.')