"""Happy Number (medium)


Problem Statement

Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3 ^22
​2
​​ +3
​2
​​  = 4 + 9 = 13
1^2 + 3^21
​2
​​ +3
​2
​​  = 1 + 9 = 10
1^2 + 0^21
​2
​​ +0
​2
​​  = 1 + 0 = 1
"""


def find_happy_number(num):
    fast, slow = num, num
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if slow == fast:
            break
    if slow == 1:
        return num
    else:
        return None


def find_square_sum(num: int):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit ** 2
        num = num // 10
    return _sum


def main():
    x = list(range(1, 1000))
    happy_numbers = [find_happy_number(num) for num in x if find_happy_number(num)]
    print(happy_numbers)
    print(find_happy_number(32))
    print(find_happy_number(12))


main()


def digits_square_sum(num: int):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit ** 2
        num = num // 10
    return _sum


def is_happy_number(num: int):
    fast, slow = num, num
    while True:
        fast = digits_square_sum(digits_square_sum(fast))
        slow = digits_square_sum(slow)
        if fast == slow:
            break
    if slow == 1:
        return True
    else:
        return False


def main():
    x = list(range(1, 1000))
    happy_numbers = [is_happy_number(num) for num in x if is_happy_number(num)]
    print(happy_numbers)
    print(is_happy_number(32))
    print(is_happy_number(12))


main()
