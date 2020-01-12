# recursive implementation of the linear search algorithm
def find(x, l, i, s):
    if i > s:
        return -1
    elif l[i] != x:
        return find(x, l, i + 1, s)
    else:
        return i

li = [3,6,7,8,9,100,123]
print(find(9, li, 0, len(li)-1))

# return find i = 1
#   return find i = 2
#       return find i = 3
#           return find i = 4 (l[i] != x) = True
#               return i