#coding=utf-8

#Given an array of integers, find two numbers such that they add up to a specific target number.
#
#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
#You may assume that each input would have exactly one solution.
#
#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

class Solution:
    def twoSum(self, numbers, target):
        index_to_number = {}
        for index, item in enumerate(numbers):
            index_to_number[item] = index + 1
        for index, first_number in enumerate(numbers):
            second_number = target - first_number
            if second_number in index_to_number:
                index1 = index + 1
                index2 = index_to_number[second_number]
                if index1 != index2:
                    return index1, index2
