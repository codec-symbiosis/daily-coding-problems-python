'''
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''

def encoding(string):
    if not string:
        return ''

    coding = []

    code = string[0]
    for char in string[1:]:
        if char != code[-1]:
            coding.append(str(len(code)) + code[-1])
            code = char
        else:
            code += char

    if code:
        coding.append(str(len(code)) + code[-1])

    return ''.join(coding)

if __name__ == '__main__':
    string = input()
    print(encoding(string))