def selection_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        current_min = i
        for j in range(i + 1, n):
            if arr[j].value < arr[current_min].value:
                current_min = j

        arr[i], arr[current_min] = arr[current_min], arr[i]
        arr[i].row, arr[current_min].row = arr[current_min].row, arr[i].row
        arr[i].column, arr[current_min].column = arr[current_min].column, arr[i].column
        yield True