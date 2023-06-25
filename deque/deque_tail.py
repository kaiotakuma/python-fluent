from collections import deque


def tail(filename, n=2):
    with open(filename) as f:
        return deque(f, n)


letra_musica = tail("deque\music.txt")
print(letra_musica)
