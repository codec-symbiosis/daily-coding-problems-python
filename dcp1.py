'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def if_availabe(n, num_list, num_to_chk):
    notavailable = True
    i = 0
    j = n-1
    num_list.sort()
    while i<n and j>0:
        t_sum = num_list[i] + num_list[j]
        if t_sum > num_to_chk:
            j -= 1
        elif t_sum < num_to_chk:
            i += 1
        else:
            print(str(num_list[i]) + ' ' + str(num_list[j]))
            notavailable = False
            break

    if notavailable:
        print('No pair available')

if __name__ == '__main__':
    n = int(input())
    num_list = list(map(int, input().split()))
    num_to_chk = int(input())
    if_availabe(n, num_list, num_to_chk)