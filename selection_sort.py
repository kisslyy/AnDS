a = [2,8,5,3,9,4,1]

for j in range(len(a)-1):
    i_min = j
    for i in range(j+1, len(a)):
        if a[i] < a[i_min]:
            i_min = i

    if i_min != j:
        a[i_min],a[j] = a[j],a[i_min]

print(a)