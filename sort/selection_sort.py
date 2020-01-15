# selection sort algorithm

def sort(l):
    for i in range(len(l)):
        min_ind = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_ind]:
                min_ind = j
        l[i], l[min_ind] = l[min_ind], l[i]
    return l

print(sort([3,2,4,1]))