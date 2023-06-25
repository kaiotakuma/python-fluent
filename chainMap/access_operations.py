from collections import ChainMap
  
# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
  
# initializing ChainMap
chain = ChainMap(dic1, dic2)
  
# printing chainMap using maps
print ("All the ChainMap contents are : ")
# saída - lista de dicionários
print (chain.maps)
  
# printing keys using keys()
print ("All keys of ChainMap are : ")
# listas de chaves, não repete 
print (list(chain.keys()))
  
# printing keys using keys()
print ("All values of ChainMap are : ")
# lista de valores, não pega todos os valores de b(chave repetida)
print (list(chain.values()))