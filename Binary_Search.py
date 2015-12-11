

def bin_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) / 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid

print bin_search([1, 2], 2)
