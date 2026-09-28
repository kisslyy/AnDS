x = int(input("Введите число x: "))
results = []

k = 0
while 3**k <= x:
    l = 0
    while (3**k) * (5**l) <= x:
        m = 0
        while (3**k) * (5**l) * (7**m) <= x:
            val = (3**k) * (5**l) * (7**m)
            results.append(val)
            m += 1
        l += 1
    k += 1

results.sort()
print("Подходящие числа:")
for val in results:
    print(val)