

def merge_sort(arr, start, end):
    mid = start + (end - start) / 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)


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
