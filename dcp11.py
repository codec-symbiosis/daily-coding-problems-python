'''
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
'''

class Node(object):
    def __init__(self, val=None, next_n=None):
        self.val = val
        self.next = next_n

def reconstruct(string, dict_set):
    ptr = [None] * (len(string) + 1)

    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            sub_string = string[i:j]
            if sub_string in dict_set:
                new_node = Node(sub_string)
                if not ptr[j]:
                    ptr[j] = new_node
                else:
                    add_at_tail(ptr[j], new_node)

    res = list()
    curr = list()
    dfs(ptr, res, curr, len(ptr) - 1)
    return res


def add_at_tail(head, node):
    while head.next:
        head = head.next
    head.next = node


def dfs(ptr, result, current, idx):
    if idx == 0:
        result.append(current)
        return

    if not ptr[idx]:
        return
    else:
        node = ptr[idx]
        while node:
            word = node.val
            temp = current[:]
            temp.insert(0, word)
            dfs(ptr, result, temp, idx - len(word))
            node = node.next


def main():
    
    words = list(input().split())
    sentence = input()
    # dict_set_2 ={'bed', 'bath', 'bedbath', 'and', 'beyond','dba'}
    # string_2 = 'bedbathandbeyond'
    print(reconstruct(sentence, words))


if __name__ == '__main__':
    main()