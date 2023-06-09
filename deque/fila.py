from collections import deque
import queue

class Fila:

    def __init__(self):
        self.lista = deque()

    def insert(self, val):
        self.lista.append(val)

    def remove(self):
        return self.lista.popleft()

    def __repr__(self):
        lista_elementos = [str(elemento) for elemento in self.lista]
        elementos_str = ";-;".join(lista_elementos)
        return f'Fila [{elementos_str}]'

queue = Fila()
queue.insert('Godofredo - 1')
queue.insert('Godofreda - 2')
queue.insert('Godofre(lu) - 3')
print(queue)

a = queue.remove()
print('a = ',a)
print(queue)

# # Cria uma instância de uma fila (queue) FIFO (First-In-First-Out)
# fila = queue.Queue()

# # Adiciona elementos à fila
# fila.put("A")
# fila.put("B")
# fila.put("C")

# while (fila.empty() == False):
#     print(fila.queue[1])

# # # Verifica se a fila está vazia
# # vazia = fila.empty()
# # print("Fila vazia?", vazia)  # False

# # # Obtém o tamanho da fila
# # tamanho = fila.qsize()
# # print("Tamanho da fila:", tamanho)  # 3

# # # Obtém o próximo elemento da fila (sem removê-lo)
# # proximo_elemento = fila.queue[0]
# # print("Próximo elemento da fila:", proximo_elemento)  # "A"

# # # Remove e retorna o próximo elemento da fila
# # elemento_removido = fila.get()
# # print("Elemento removido:", elemento_removido)  # "A"

# # # Verifica se a fila está vazia novamente
# # vazia = fila.empty()
# # print("Fila vazia?", vazia)  # False

# # # Obtém o tamanho atualizado da fila
# # tamanho = fila.qsize()
# # print("Tamanho da fila:", tamanho)  # 2

# # # Limpa a fila
# # fila.queue.clear()

# # Verifica se a fila está vazia após limpar
# # vazia = fila.empty()
# # print("Fila vazia?", vazia)  # True
