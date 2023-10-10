class Social_Network:
  def __init__(self, nome, descricao):
    self.nome = nome
    self.descricao = descricao
  pass

social_network1 = Social_Network('\n\nInstagram', '\nDescrição de algo')
social_network2 = Social_Network('\n\nFacebook', '\nDescrição de algo\n\n')
print(social_network1.nome,social_network1.descricao)
print(social_network2.nome,social_network2.descricao)

    