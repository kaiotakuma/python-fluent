from itertools import chain


def chain(*iterables):

    """
    Função que combina várias sequências em uma única sequência, retornando um valor de cada sequência por vez
    """

    for iterable in iterables:
        for value in iterable:
            # retorna uma particula da sula interação por vez
            yield value


r = chain([1, 2, 3, 4], [3, 6, 3, 8])

print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
# print(next(r))

t = list(chain([1, 2, 3, 4], [3, 6, 3, 3]))
print(t)
print(set(t))