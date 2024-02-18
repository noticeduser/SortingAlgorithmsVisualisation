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