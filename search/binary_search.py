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

print(find(72, list(range(0, 100))))

# binary search problem:
# find the square root of X using binary search
def findsqrt(x, l):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = left + int((right - left) / 2)
        if l[mid]*l[mid] == x:
            return mid
        elif x < l[mid]*l[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

nums = range(0, 1001)
print(list(filter(lambda n: False if findsqrt(n, nums) == -1 else True, nums)))