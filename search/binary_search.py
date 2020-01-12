# binary search algorithm
# only works with sorted arrays
# divide and conquer
def find(x, l):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if l[mid] == x:
            return mid
        elif x < l[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(find(4, list(range(0, 100))))