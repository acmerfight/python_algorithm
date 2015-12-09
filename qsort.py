
def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])

def qsort(a):
    length = len(a)
    start_index = 1
    end_index = length - 1
    while start_index <= end_index:
        while a[start_index] <= a[0] and start_index <= end_index:
            start_index += 1
            if start_index == end_index:
                break
        while a[end_index] >= a[0] and start_index <= end_index:
            end_index -= 1
            if start_index == end_index:
                break
        print start_index, end_index
        a[start_index], a[end_index] = a[end_index], a[start_index]
        print a
        start_index += 1
        end_index -= 1
    print start_index, end_index
    a[0], a[start_index] = a[start_index], a[0]
    print a

qsort([1, 3, 2, -1])

