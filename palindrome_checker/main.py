with open("./input.txt", "r") as f:
    input = f.readlines()


def parse_char(char):
    if char.isalnum():
        return char.lower()
    else:
        return ""


def check_palindrome(string):
    length = len(string)
    left = 0
    right = length - 1
    dict = {}

    while left <= right:
        left_char = parse_char(string[left])
        right_char = parse_char(string[right])
        # if left == right:

        if not left_char:
            left += 1
            continue

        if not right_char:
            right -= 1
            continue

        if left_char != right_char:
            print("No, -1")
            return
        else:
            dict[left_char] = dict.get(left_char, 0) + 1
            left += 1
            right -= 1
            continue

    print(f"YeS, {dict.__len__()}")
    return


for line in input:
    check_palindrome(line)
