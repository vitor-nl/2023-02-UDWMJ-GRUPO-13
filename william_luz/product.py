class Product:
  from category import Category
  def __init__(self, nome, descricao, data_fabricacao, esta_ativo):
    self.nome = nome
    self.descricao = descricao
    self.data_fabricacao = data_fabricacao
    self.esta_ativo = esta_ativo
  pass

produto1 = Product('\n\nNome:Arroz','\nDescrição:Integral','\nData Fab:23/10/2024','\nEstá ativo: Sim')
produto2 = Product('\n\nNome:Feijão','\nDescrição:Integral','\nData Fab:29/11/2024','\nEstá ativo: Sim')
produto3 = Product('\n\nNome:Oleo','\nDescrição:Soja','\nData Fab:10/08/2024','\nEstá ativo: Sim')
produto4 = Product('\n\nNome:Ovo','\nDescrição:Integral','\nData Fab:06/10/2024','\nEstá ativo: Sim')
print(produto1.nome,produto1.descricao,produto1.data_fabricacao,produto1.esta_ativo)
print(produto2.nome,produto2.descricao,produto2.data_fabricacao,produto2.esta_ativo)
print(produto3.nome,produto3.descricao,produto3.data_fabricacao,produto3.esta_ativo)
print(produto4.nome,produto4.descricao,produto4.data_fabricacao,produto4.esta_ativo)
