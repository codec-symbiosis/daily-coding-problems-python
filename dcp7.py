'''
Good morning! Here's your daily coding problem #7 for today.
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of all possible 
query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''

def auto_comp(query, strings):
    n = len(query)
    response = []
    for string in strings:
        if string[:n] == query:
            response.append(string)
    
    return response

def main():
    strings = list(input().split())
    query = input()
    print(auto_comp(query, strings))

if __name__ == '__main__':
    main()