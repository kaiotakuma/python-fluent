from collections import deque 

class List:
    def __init__(self):
        self.lista = deque()

    def insert(self, valor, posicao = None):
        # se tiver posição, inserir na posição que defini
        if posicao:
            self.lista.insert(valor, posicao)
        # se não, insere no final da lista
        else:
            self.lista.append(valor)

    def remove(self, valor):
        return self.lista.remove(valor)
    
    def __repr__(self) -> str:
        return 'Lista [{}]'.format(', '.join(str(x) for x in self.lista))
    
list_a = List()
list_a.insert('popo')
list_a.insert(0,'pipi')
list_a.remove('popo')
print(type(list_a))
print(list_a)

list_b = list()
list_b.append(666)
list_b.extend([list_a])
print(list_b)

