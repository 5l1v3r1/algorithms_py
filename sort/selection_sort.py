# selection sort algorithm

def sort(l):
    for i in range(len(l)):
        min_ind = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_ind]:
                min_ind = j
        #print(f"Swapping {l[i]} with {l[min_ind]}, {l}")
        l[i], l[min_ind] = l[min_ind], l[i]
    return l

print(sort([9,1,3,2,8,4,5]))