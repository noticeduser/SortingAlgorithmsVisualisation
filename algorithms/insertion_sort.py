def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1].value > arr[j].value:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            arr[j - 1].row, arr[j].row = arr[j].row, arr[j - 1].row
            arr[j - 1].column, arr[j].column = arr[j].column, arr[j - 1].column
            j -= 1
            yield True
