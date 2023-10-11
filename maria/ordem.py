class Ordem:
    from cliente import Cliente 
    def __init__(self, preco_total, status):
        self._preco_total = preco_total 
        self._status = status 
    pass

ordem1 = Ordem ('\n\n 240', 'Pendente') 
ordem2 = Ordem ('\n\n 3000', 'Pago') 

print(ordem1._preco_total, ordem1._status)  
print(ordem2._preco_total, ordem2._status)


    