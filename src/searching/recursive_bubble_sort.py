def bubble_sort(arr, unsorted_length):
    # find the unsorted_length 
    # iterate through the arr
    # figure out, starting from the right side, how many elements 
    # of the array are sorted 
    # recursive implementation of bubble sort 
    # base case 
    # what's the length of the unsorted portion of our array? 
    # once we get to an empty unsorted portion, then everything is sorted 
    # how are we moving closer to our base case? 
    for i in range(0, unsorted_length - 1):
        # compare two elements 
        if arr[i] > arr[i+1]:
            # swaps them if the two elements aren't in order 
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # we've done one iteration of the swapping, check to see 
    # if there's more sorting to do 
    if unsorted_length > 0:
        bubble_sort(arr, unsorted_length - 1)