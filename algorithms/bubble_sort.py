def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].value > arr[j + 1].value:
                arr[j].row, arr[j + 1].row = arr[j + 1].row, arr[j].row
                arr[j].column, arr[j + 1].column = arr[j + 1].column, arr[j].column
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield True
