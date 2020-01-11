# linear search algorithm
# look through the array from the very first index until
# the specified value (X) is found, if the array ends and the
# value is not found return -1.
def find(x, l):
    index = 0
    for element in l:
        if element == x:
            return index
        index += 1
    return -1

print(find(9, [3,6,7,8,9,100,123]))
print(find(100, [1,1,2,3,5,8,13]))