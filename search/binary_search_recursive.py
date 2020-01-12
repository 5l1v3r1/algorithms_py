# recursive implementation of the binary search algorithm
# this algorithm only works with sorted arrays
def find(x, l, left, right, mid):
    mid = left + int((right - left) / 2)
    if left > right:
        return -1
    elif l[mid] == x:
        return mid
    elif x > l[mid]:
        return find(x, l, mid+1, right, mid)
    else:
        return find(x, l, left, mid-1, mid)


li = list(range(0, 100))
print(find(1, li, 0, len(li)-1, 0))