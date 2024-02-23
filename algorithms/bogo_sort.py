from random import shuffle


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i].value > arr[i + 1].value:
            return False
    return True

def bogo_sort(arr, index_grid_pos):
    while not is_sorted(arr):
        shuffle(arr)
        for i, block in enumerate(arr):
            row, column = index_grid_pos[i]
            block.row = row
            block.column = column
        yield arr

