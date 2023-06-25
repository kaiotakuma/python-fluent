from collections import ChainMap

# initializing dictionaries
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
dic3 = {"f": 5}

# initializing ChainMap
chain = ChainMap(dic1, dic2)

# printing chainMap using map
print("All the ChainMap contents are : ")
print(chain.maps)

# imprimindo só o primeiro dicionário
print(chain.maps[0])

# imprimindo as chaver do primeiro dicionário
print(chain.maps[0].keys())


# # using new_child() to add new dictionary
# chain1 = chain.new_child(dic3)

# # printing chainMap using map
# print("Displaying new ChainMap : ")
# # nova lista de dicionários com dic3 adicionado na posição 0
# print(chain1.maps)

# # displaying value associated with b before reversing
# print("Value associated with b before reversing is : ", end="")
# print(chain1["b"])

# # reversing the ChainMap
# # para converter o objeto retornado pela função reversed() em uma lista
# chain1.maps = list(reversed(chain1.maps))

# # printing reversed ChainMap using maps
# print("Reversed ChainMap contents are:")
# print(chain1.maps)


# # displaying value associated with b after reversing
# print("Value associated with b after reversing is : ", end="")
# print(chain1["b"])
