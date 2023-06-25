from collections import deque 

class Pilha:
    def __init__(self):
        self.lista = deque()

    def insere(self, valor):
        # insere no final da lista
        self.lista.append(valor)

    def remove(self):
        # remove o ultimo, guarda o valor
        return self.lista.pop()
    
    def __repr__(self) -> str:
        return 'Fila [{}]'.format(', '.join(str(x) for x in self.lista))
    
lista = Pilha()
lista.insere(666)
lista.insere(999)
lista.insere("Mimi")
print(lista)
removido = lista.remove()
print(f'Removido {removido}')
print(lista)