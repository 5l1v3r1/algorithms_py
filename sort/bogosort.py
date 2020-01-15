# implementation of the bogosort algorithm
# extremely inefficient
# Performance: O(n!)
from random import shuffle

def isSorted(l):
    previous = l[0]
    for i in range(1, len(l)):
        if l[i] < previous:
            return False
        previous = l[i]
    return True

def sort(l):
    while not isSorted(l):
        shuffle(l)
    return l

print(sort([2,3,1,8,4,6,5,9]))