class Ordem_item:
    from ordem import Ordem
    from produto import Produto
    
    def __init__(self, quantidade, preco_unitario):
        self._quantidade = quantidade
        self._preco_unitario = preco_unitario
    pass

ordem_item1 = Ordem_item ('\n\n 25', '15,99')
ordem_item2 = Ordem_item ('\n\n 100', '23,55')

print(ordem_item1._quantidade, ordem_item1._preco_unitario)
print(ordem_item2._quantidade, ordem_item2._preco_unitario)