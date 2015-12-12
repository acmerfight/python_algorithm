

def merge_sort(arr, start, end):
    mid = start + (end - start) / 2
    merge_sort(arr, start, mid)
    merge_sort(mid + 1, end)
