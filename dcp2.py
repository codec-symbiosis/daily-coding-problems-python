'''
This problem was asked by Uber. 

Given an array of integers, return a new array such that each element at index i of the new 
array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def find_pair(n, num_list):
    product = 1
    for i in range(n):
        product *= num_list[i]

    product_array = [0 for i in range(n)]
    for i in range(n):
        product_array[i] = int(product/num_list[i])

    print(product_array)

if __name__ == '__main__':
    n = int(input())
    num_list = list(map(int, input().split()))
    find_pair(n, num_list)