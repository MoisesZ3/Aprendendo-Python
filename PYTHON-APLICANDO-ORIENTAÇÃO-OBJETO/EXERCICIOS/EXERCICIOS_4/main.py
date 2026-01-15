from livro import Livro

livro_1 = Livro('Harry Potter e a Pedra Filosofal','J.K. Rowling',1997)
livro_2 = Livro('Harry Potter e a Câmara Secreta','J.K. Rowling',1998)

def main():
    Livro.verificar_disponibilidade(1997)

if __name__ == '__main__':
    main()