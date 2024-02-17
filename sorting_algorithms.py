
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

#Selection Sort
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



















