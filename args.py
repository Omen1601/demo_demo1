# *args =       parameter that will pack all arguments in tuple.
#               Useful so that a function can accept a varying amount of arguments.

def add(*args):                  # you can also use diff name like (args , num, value)  but before that * is compulsory
    sum = 0
    args = list(args)            # |        used to convert tuple into list
    args[0] = 0                  # |        list can be modified but not a tuple (so the first number is 0)
    for i in args:
        sum += i
    return sum

print(add(1,2,3))           # 1+2+3 = 6         but index[0] is 0           so 0+2+3 = 5