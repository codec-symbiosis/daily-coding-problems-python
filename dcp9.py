'''
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and
you do not need to store the results. You can simply print them out as you
compute them.
Reference:
https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
'''


from __future__ import print_function
from collections import deque

def printMax(arr, n, k):
    q = deque()

    for i in range(k):

        while q and arr[i] >= arr[q[-1]] :
            q.pop()

        q.append(i)

    for i in range(k, n):
        print(str(arr[q[0]]) + " ", end = "")

        while q and q[0] <= i-k:
            q.popleft()

        while q and arr[i] >= arr[q[-1]] :
            q.pop()

        q.append(i)

    print(str(arr[q[0]]))


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    printMax(arr, len(arr), k)


if __name__ == '__main__':
    main()