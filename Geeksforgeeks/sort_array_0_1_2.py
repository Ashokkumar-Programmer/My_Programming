'''
Question:

Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.

'''

n = int(input())

arr = list(map(int, input().split()))

def sort_0_1_2(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    
    # Count the number of 0s, 1s and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
    
        elif arr[i] == 1:
            cnt1 += 1
    
        elif arr[i] == 2:
            cnt2 += 1
    
    # Update the array
    i = 0
    
    # Store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1
    
    # Then all the 1s
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1
    
    # Finally all the 2s
    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1
    
    # Print the sorted array
    return arr

print(sort_0_1_2(arr))