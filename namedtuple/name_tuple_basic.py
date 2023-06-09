from collections import namedtuple


"""
python 2.6 

Uma função de fábrica para criar subclasses que 
fornece campos nomeados que permitem acessar itens por nome,
 mantendo a capacidade de acessar itens por índicetuple

1- typename é o nome da classe que você está criando. Deve ser uma cadeia de 
caracteres com um identificador Python válido.
2 - field_names é a lista de nomes de campos que você usará para acessar os itens na tupla resultante. Pode ser:
    *Uma iteração de cadeias de caracteres, como ["field1", "field2", ..., "fieldN"]
    *Uma cadeia de caracteres com nomes de campo separados por espaço em branco, como "field1 field2 ... fieldN"
    *Uma cadeia de caracteres com nomes de campos separados por vírgula, como "field1, field2, ..., fieldN"

"""


BinaryOp = namedtuple('BinaryOp',['plus','minus'])

binary_op = BinaryOp(plus = 'add',minus = 'sub')

print(binary_op)