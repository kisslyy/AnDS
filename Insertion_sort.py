a = [5,4,3,2,1]

for i in range(1, len(a)):
    j = i
    while j > 0 and a[j-1] > a[j]:
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1

print(a)