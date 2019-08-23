'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
'''


def unique_ways(n, ways):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif ways[n] != 0:
        return ways[n]

    total_ways = unique_ways(n-1, ways) + unique_ways(n-2, ways)
    ways[n] = total_ways
    return total_ways

if __name__=='__main__':
    n = int(input())
    ways = [0 for i in range(n+1)]
    print(unique_ways(n, ways))