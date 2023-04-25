'''
Question:

Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

 

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.

'''
#getting input

n = int(input())
s = int(input())

input_arr = list(map(int, input().split()))

#split subarrays and sum of subarray is equal to s
def sum_subarray(n,s,arr):
    curr_sum = arr[0]
    start = 0
    for end in range(1, n+1):
        while curr_sum > s and start < end-1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == s:
            return [start+1, end]
        if end < n:
            curr_sum += arr[end]
    return [-1]
print(sum_subarray(n,s,input_arr))