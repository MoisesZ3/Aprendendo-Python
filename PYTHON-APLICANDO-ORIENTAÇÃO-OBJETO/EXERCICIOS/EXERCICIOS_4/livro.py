class Livro:
    livros = []

    def __init__(self,titulo,autor,ano_lancamento):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_lancamento = ano_lancamento
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.ano_de_lancamento}'
    
    def emprestar_livro(self):
        if self.disponivel == True:
            self.disponivel = not self.disponivel
            print('Você emprestou seu livro')
        else:
            print('Esse livro emprestado')

    def verificar_livro(self):
        if self.disponivel == True:
            print('Seu livro esta na prateleira')
        else:
            print('seu livro ja deve ser sido pego')

    def verificar_disponibilidade(ano):
        for livro in Livro.livros:
            if livro.ano_de_lançamento == ano and livro._disponivel == True:
                print(livro)
            