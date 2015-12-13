

def merge_sort(arr):
    mid = len(arr) / 2
    if len(arr) <= 1:
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    return res + arr1[i:] + arr2[j:]


print merge([1], [2, 2, 8])
print merge_sort([1, 3, 2, 10, 5, 5, 10])
