
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].value > arr[j+1].value:
                arr[j].row, arr[j+1].row = arr[j+1].row, arr[j].row
                arr[j].column, arr[j+1].column = arr[j+1].column, arr[j].column
                arr[j], arr[j+1] = arr[j+1], arr[j]
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


 # Merge Sort and related       
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    arr[i].row, arr[j].row = arr[j].row, arr[i].row
    arr[i].column, arr[j].column = arr[j].column, arr[i].column


def siftDown(arr, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if arr[i].value >= max(arr[l].value, arr[r].value): break
            elif arr[l].value > arr[r].value:
                swap(arr, i, l)
                i = l
            else:
                swap(arr, i, r)
                i = r
        elif l < upper:
            if arr[l].value > arr[i].value:
                swap(arr, i, l)
                i = l
            else: break
        elif r < upper:
            if arr[r].value > arr[i].value:
                swap(arr, i , r)
                i = r 
            else: break
        else: break

def heap_sort(arr):
    n = len(arr)
    for j in range((n - 2) // 2, -1, -1):
        siftDown(arr, j, n)
    
    for end in range(n - 1, 0, -1):
        swap(arr, 0, end)
        siftDown(arr, 0, end)
        yield arr[end]

# def merge_sort(arr):
#     n = len(arr)

#     if n > 1:
#         left_arr = arr[:n//2]
#         right_arr = arr[n//2:]

#         # recursion
#         yield from merge_sort(left_arr)
#         yield from merge_sort(right_arr)

#         # merge
#         i = 0 # left array index
#         j = 0 # right array index
#         k = 0 # merged array index

#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i].value < right_arr[j].value:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1

#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1

#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1

#         for i in left_arr:
#             print("new iteration")
#             print(f"\nl: {i.value}\n")

#         yield True 



















        



































