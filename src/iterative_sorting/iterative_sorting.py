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


test = [0, 5, 7, 4, 1]
# TO-DO:  implement the Bubble Sort function below

# print(len(test))

for i in range(len(test) - 2):
    # test[i + 1]
    current_index = i
    if test[i] > test[i + 1]:
        print(i)
    # print(i)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
