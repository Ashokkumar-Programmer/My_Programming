'''
Question:

Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.

 

Example 2:

Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0

'''
n = int(input())
arr = list(map(int, input().split()))
def array_leader(n, arr):
    leaders = []
    for i in range(n):
        j = i+1
        while j<n:
            if arr[i]<arr[j]:
                break
            j = j+1
        if j == n:
            leaders.append(arr[i])
    return leaders
print(array_leader(n, arr))