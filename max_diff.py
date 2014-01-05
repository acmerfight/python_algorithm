def max_diff(a):
    assert len(a) >= 2, "list's length maust greater than two"
    diff = a[1] - a[0]
    min_number = a[0] 
    for index, item in enumerate(a[1:]):
        if item < min_number:
            min_number = item
        if diff < item - min_number:
            diff  = item - min_number
    return diff

def max_diff_brute(a):
    assert len(a) >= 2, "list's length maust greater than two"
    diff = 0
    for index, i in enumerate(a): 
        for j in a[index + 1:]: 
            if j - i > diff:
                diff = j - i
    return diff
            

if __name__ == "__main__":
    a = [1, 3, 11, 5]
    assert max_diff(a) == 10 == max_diff_brute(a)
    b = [5, 4, 3, 2, 1]
    assert max_diff(b) == 0 == max_diff_brute(b)
