def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap].value > temp.value:
                arr[j] = arr[j - gap]
                arr[j - gap] = temp

                arr[j].row, arr[j - gap].row = arr[j - gap].row, arr[j].row
                arr[j].column, arr[j - gap].column = arr[j - gap].column, arr[j].column
                j -= gap
                yield True
        gap //= 2
        yield True

    yield True
