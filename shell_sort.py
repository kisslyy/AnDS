def shell_sort(data: list[int]) -> list[int]:
    step = len(data) // 2

    while step > 0:
        for i in range(step, len(data)):
            temp = data[i]
            j = i

            while j >= step and data[j - step] > temp:
                data[j] = data[j - step]
                j -= step

            data[j] = temp

        step //= 2

    return data

unsorted_list = [3, 8, 4, 12, 6, 9, 20, 11, 13, 76, 120]

print(shell_sort(unsorted_list))