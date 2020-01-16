# insertion sort algorithm

def sort(l):
    for index in range(1, len(l)):
        k = l[index]
        j = index-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j-=1
        l[j+1] = k

    return l

print(sort([9,1,3,8,2,5,4]))