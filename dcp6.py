'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should 
return 10, since we pick 5 and 5.
'''

def max_non_adj_sum(arr):
    incl_sum, excl_sum = 0, 0
    for i in arr:
        temp = max(incl_sum, excl_sum)
        incl_sum = excl_sum + i
        excl_sum = temp
    
    return max(incl_sum, excl_sum)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(max_non_adj_sum(arr))