def find(x, l):
    index = 0
    for element in l:
        if element == x:
            return index
        index += 1
    return -1

print(find(123, [3,6,7,8,9,100,123]))