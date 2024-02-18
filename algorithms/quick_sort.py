def partition(arr, left, right):
    pivot = arr[right].value
    i = left - 1

    for j in range(left, right):
        if arr[j].value < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i].row, arr[j].row = arr[j].row, arr[i].row
            arr[i].column, arr[j].column = arr[j].column, arr[i].column
            yield True

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    arr[i + 1].row, arr[right].row = arr[right].row, arr[i + 1].row
    arr[i + 1].column, arr[right].column = arr[right].column, arr[i + 1].column
    yield i + 1


def quick_sort(arr):
    stack = []

    stack.append(0)
    stack.append(len(arr) - 1)

    while stack:
        right = stack.pop()
        left = stack.pop()

        partition_gen = partition(arr, left, right)
        pivot_index = None
        for pivot_index in partition_gen:
            yield True

        if pivot_index - 1 > left:
            stack.append(left)
            stack.append(pivot_index - 1)

        if pivot_index + 1 < right:
            stack.append(pivot_index + 1)
            stack.append(right)