# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        stop_iteration = 0
        for k in range(len(arr) - 1):
            curr_index = k
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
