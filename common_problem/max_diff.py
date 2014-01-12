#coding=utf-8

#要求找出一个互异数组中两个元素的最大差值。具体描述如下：
#有一个整数数组d[0,...,n-1]，并且数组满足不存在相同的元素，要求找出
#1) max{d[i] - d[j]} 且 i > j;(对应实际生活中的股票买卖，找出可能的最大收益)

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
