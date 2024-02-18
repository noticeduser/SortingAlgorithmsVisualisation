# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].value > arr[j + 1].value:
                arr[j].row, arr[j + 1].row = arr[j + 1].row, arr[j].row
                arr[j].column, arr[j + 1].column = arr[j + 1].column, arr[j].column
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield True


# Insertion Sort
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


# Selection Sort
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


# Heap Sort and related
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    arr[i].row, arr[j].row = arr[j].row, arr[i].row
    arr[i].column, arr[j].column = arr[j].column, arr[i].column


def siftDown(arr, i, upper):
    while True:
        left, right = i * 2 + 1, i * 2 + 2
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
        siftDown(arr, j, n)
        yield True

    for end in range(n - 1, 0, -1):
        swap(arr, 0, end)
        siftDown(arr, 0, end)
        yield arr[end]


# Quick Sort and Related
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


# Merge Sort and Related
def update_block_positions(arr, index_grid_pos):
    for i, block in enumerate(arr):
        row, column = index_grid_pos[i]
        block.row = row
        block.column = column


def merge_sort(arr, index_grid_pos):
    n = len(arr)

    if n > 1:
        left_arr = arr[: n // 2]
        right_arr = arr[n // 2 :]

        # Recursion
        yield from merge_sort(left_arr, index_grid_pos)
        yield from merge_sort(right_arr, index_grid_pos)

        # Merge
        i = 0  # Left array index
        j = 0  # Right array index
        k = 0  # Merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].value < right_arr[j].value:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

            update_block_positions(arr, index_grid_pos)
            yield arr

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

            update_block_positions(arr, index_grid_pos)
            yield arr

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

            update_block_positions(arr, index_grid_pos)
            yield arr

        yield True
