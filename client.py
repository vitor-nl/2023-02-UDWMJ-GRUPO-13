class Client:
    def __init__(self, nome, sobrenome, endereço, telefone, email, genero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereço = endereço
        self.telefone = telefone
        self.email = email
        self.genero = genero

client1 = Client("Henrique", "Fossi\n", "Rua 1\n", "12345678\n", "henrique@gmail.com\n" , "Masculino\n")
client2 = Client("William", "Luz\n", "Rua 2\n", "87654321\n", "william@gmail.com\n" , "Masculino\n")
client3 = Client("Mariana", "Pires\n", "Rua 3\n", "12348765\n", "mariana@gmail.com\n" , "Feminino\n")
client4 = Client("Maria", "Camoretto\n", "Rua 4\n", "43215678\n", "maria@gmail.com\n" , "Feminino\n")

print("\nCliente 1:\n", "Nome:", client1.nome, client1.sobrenome, "Endereço:", client1.endereço, "Telefone:", client1.telefone, "E-mail:", client1.email, "Gênero:", client1.genero)
print("Cliente 2:\n", "Nome:", client2.nome, client2.sobrenome, "Endereço:", client2.endereço, "Telefone:", client2.telefone, "E-mail:", client2.email, "Gênero:", client2.genero)
print("Cliente 3:\n", "Nome:", client3.nome, client3.sobrenome, "Endereço:", client3.endereço, "Telefone:", client3.telefone, "E-mail:", client3.email, "Gênero:", client3.genero)
print("Cliente 4:\n", "Nome:", client4.nome, client4.sobrenome, "Endereço:", client4.endereço, "Telefone:", client4.telefone, "E-mail:", client4.email, "Gênero:", client4.genero)
