from collections import deque

cache_values = deque(maxlen=3)

def cache(func):
    def inner(*args):
        cache_values.append(args)
        return func(*args)
    return inner


@cache
def soma(x, y):
    return x + y

print(soma(1,2)) # 3 
print(soma(1,3)) # 4
print(soma(1,4)) # 5 
print(soma(1,5))  # 6
print(cache_values)

'''
3
4
5
6
deque([(1, 3), (1, 4), (1, 5)], maxlen=3)

'''