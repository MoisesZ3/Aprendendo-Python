class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
nome_praca = restaurante_praca.nome = 'Bistrô'
categoria_praca = restaurante_praca.categoria = 'Italiana'
status_praca = restaurante_praca.ativo

restaurante_pizza = Restaurante()
nome_pizza = restaurante_pizza.nome = 'Pizza Place'
categoria_pizza = restaurante_pizza.categoria = 'Fast Food'
status_pizza = restaurante_pizza.ativo

restaurantes = [restaurante_praca, restaurante_pizza]
print(restaurante_praca.nome)

if status_praca == True:
    print('O restaurante praça esta ativo')
elif status_praca == False:
    print('O restaurante praça esta inativo')

print(categoria_pizza)
restaurante_pizza.ativo = True

print(f'Nome: {nome_praca}\nCategoria: {categoria_praca}')

