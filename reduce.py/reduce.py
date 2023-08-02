from functools import reduce
l = [2, 4, 5, 6]

def func(accumultor, currentvalue):
    print(accumultor, "accumulator")
    print(currentvalue, "currentvalue\n")
    return accumultor - currentvalue


sum = reduce(func, l, 5 )
print(sum)


