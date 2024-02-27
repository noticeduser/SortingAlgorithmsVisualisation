def counting_sort(arr, digit, index_grid_pos):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = arr[i].value // digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i].value // digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]
        row, column = index_grid_pos[i]
        arr[i].row = row
        arr[i].column = column
        yield True


def radix_sort(arr, index_grid_pos):
    max_num = max(block.value for block in arr)
    digit = 1
    while max_num // digit > 0:
        yield from counting_sort(arr, digit, index_grid_pos)
        digit *= 10
