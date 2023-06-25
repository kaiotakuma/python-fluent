from collections import ChainMap

# incapsulates many dictionaries into one unit

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"e": 5, "f": 6}

# Defining the chainmap
# tem ordem deprecedencia 
c = ChainMap(d1, d2, d3)

# saída - tupla de dicionários
print(c)
