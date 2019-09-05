'''
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''


def is_balanced(brackets):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    dictionary = {')': '(', ']': '[', '}': '{'}

    br_stack = []

    for br in brackets:
        if br in open_brackets:
            br_stack.append(br)
        elif br in close_brackets:
            if match(br_stack, br, dictionary): # balance
                br_stack.pop()
            else:
                return False
        else:
            raise ValueError('Invalid String.')

    if not br_stack:
        return True
    else:
        return False


def match(br_list, br, dic):
    if not br_list:
        return False
    else:
        if br_list[-1] == dic[br]:
            return True
        else:
            return False


def main():
    brackets = input()
    print(is_balanced(brackets))

if __name__ == '__main__':
    main()