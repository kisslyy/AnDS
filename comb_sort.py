def comb_sort(arr):
    gap = len(arr)
    shrink = 1.2473309
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted_flag = False
            i += 1
    return arr

numbers = list(map(int, input("Введите числа через пробел: ").split()))
sorted_numbers = comb_sort(numbers)
print("Отсортированный массив:", *sorted_numbers)