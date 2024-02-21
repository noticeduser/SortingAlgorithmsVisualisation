def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    arr[i].row, arr[j].row = arr[j].row, arr[i].row
    arr[i].column, arr[j].column = arr[j].column, arr[i].column


def sift_down(arr, i, upper):
    while True:
        left = i * 2 + 1
        right = i * 2 + 2

        if max(left, right) < upper:
            if arr[i].value >= max(arr[left].value, arr[right].value):
                break
            elif arr[left].value > arr[right].value:
                swap(arr, i, left)
                i = left
            else:
                swap(arr, i, right)
                i = right
        elif left < upper:
            if arr[left].value > arr[i].value:
                swap(arr, i, left)
                i = left
            else:
                break
        elif right < upper:
            if arr[right].value > arr[i].value:
                swap(arr, i, right)
                i = right
            else:
                break
        else:
            break


def heap_sort(arr):
    n = len(arr)
    for j in range((n - 2) // 2, -1, -1):
        sift_down(arr, j, n)
        yield True

    for end in range(n - 1, 0, -1):
        swap(arr, 0, end)
        sift_down(arr, 0, end)
        yield arr[end]
