from collections import deque 

# posso definir o tamanho máximo da minha deque
cache_values = deque(maxlen=5)

def cache(func):
    def inner(*args):
        cache_values.append(args)
        return  func(*args)
    return inner

@cache
def soma(x, y):
    return x + y


somar_1 = soma(2,2)
somar_2 = soma(3,4)
somar_3 = soma(5,1)
somar_4 = soma(7,7)

# insere no incio
cache_values.appendleft((1,1))
print(cache_values)

# reverte a ordem
cache_values.reverse()
print(cache_values)

# pegou os 3 ultimos e colocou no primeiro
cache_values.rotate(3)
print(cache_values)

cache_values.rotate(-3)
print(cache_values)

