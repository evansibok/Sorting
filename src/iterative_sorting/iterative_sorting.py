# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if cur_index != smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


print(selection_sort([38, 390, 94, 209, 34]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(len(arr)):
        stop_iteration = 0
        for j in range(len(arr) - i - 1):
            curr_index = j
            if arr[curr_index] > arr[curr_index + 1]:
                arr[curr_index], arr[curr_index +
                                     1] = arr[curr_index + 1], arr[curr_index]
                stop_iteration = 1
        if stop_iteration == 0:
            break
    return arr

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
