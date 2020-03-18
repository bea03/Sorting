#Insertion sort guided project

my_list = [1, 2, 10, 15, 66, 7, 9, 45, 16]

def insertion_sort(list_to_sort):
    #separate the first element, think of it as sorted

    #for all other indices, starting at 1
    for i in range(1, len(list_to_sort)):
    #put current number in a temp variable
        temp = list_to_sort[i]
    #look left, until with find where it belongs
        j = i
        while j > 0 and temp < list_to_sort[j-1]:
    #as we look left shift items to the right as we iterate
            list_to_sort[j] = list_to_sort[j-1]
            j-= 1
    #When left is smaller than temp, or we are at zero, put at this spot.
        list_to_sort[j] = temp

    return list_to_sort


print(insertion_sort(my_list))


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        cur_val = arr[i]
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i] = arr[smallest_index]
        arr[smallest_index] = cur_val
    return arr         


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_status = True

    while swap_status == True:
        swap_status = False
        # for loop to compare each number
        for i in range(0, len(arr)-1):

            if arr[i] > arr[i+1]:
                left_value = arr[i]
                right_value = arr[i+1]
                arr[i] = right_value
                arr[i+1] = left_value
                swap_status = True
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
