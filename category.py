class Category:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        
category1 = Category("111\n", "Alimento\n", "Barra de Chocolate\n")
category2 = Category("222\n", "Cosmético\n", "Shampoo\n")
category3 = Category("333\n", "Limpeza\n", "Detergente\n")
category4 = Category("444\n", "Bebida\n", "Refrigerante\n")

print("\nCategoria 1: \n", "ID:", category1.id, "Nome:", category1.nome, "Descrição:", category1.descricao)
print("Categoria 2: \n", "ID:", category2.id, "Nome:", category2.nome, "Descrição:", category2.descricao)
print("Categoria 3: \n", "ID:", category3.id, "Nome:", category3.nome, "Descrição:", category3.descricao)
print("Categoria 4: \n", "ID:", category4.id, "Nome:", category4.nome, "Descrição:", category4.descricao)
