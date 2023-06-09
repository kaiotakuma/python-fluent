from collections import namedtuple

binary_ops = { 
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "div",
    "%": "mod",
    "||": "or",
    "&&": "and",
    "<": "lt",
    "<=": "le",
    ">": "gt",
    ">=": "ge",
    "==": "eq",
    "!=": "ne"
}

BinaryOp = namedtuple("BinaryOp", ["symbol", "operation"])

binary_ops = [
    BinaryOp("+", "add"),
    BinaryOp("-", "sub"),
    BinaryOp("*", "mul"),
    BinaryOp("/", "div"),
    BinaryOp("%", "mod"),
    BinaryOp("||", "or"),
    BinaryOp("&&", "and"),
    BinaryOp("<", "lt"),
    BinaryOp("<=", "le"),
    BinaryOp(">", "gt"),
    BinaryOp(">=", "ge"),
    BinaryOp("==", "eq"),
    BinaryOp("!=", "ne")
]


def print_named_tuple(BinaryOp,target_key:str,target_value:str=None):
    # for binary_op in binary_ops:
    #     if binary_op.symbol == target_key:
    #         return binary_op.operation
    return [binary_op.operation for binary_op in BinaryOp if binary_op.symbol == target_key][0]
                   
#print(print_named_tuple(target_key = '-'))
print(binary_ops)
new_dict  = binary_ops._asdict()



print(new_dict)



