'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
'''

def solution2(s, k):
    
    start_index, end_index, max_length = 0, k, k
    while end_index < len(s):

        end_index += 1
        while True:

            distinct_characters = len(set(s[start_index:end_index]))
            if distinct_characters <= k:
                break

            start_index += 1

        max_length = max(max_length, end_index - start_index)

    return max_length

def main():
    s = input()
    k = int(input())
    print(solution2(s, k))

if __name__ == '__main__':
    main()