'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways 
it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'
'''

def no_ways(str):
    n = len(str)
    if n==1:
        return 1
    elif n==2:
        if int(str)>26:
            return 1
        else:
            return 2
    
    if int(str[:2]) <= 26:
        total_ways = no_ways(str[1:]) + no_ways(str[2:])
    else:
        total_ways = no_ways(str[1:])

    return total_ways

if __name__ == '__main__':
    str = input()
    print(no_ways(str))
