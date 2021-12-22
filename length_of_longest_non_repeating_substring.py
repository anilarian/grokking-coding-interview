"""Longest Substring with Distinct Characters (hard)


Problem Statement

Given a string, find the length of the longest substring, which has all distinct characters.

 Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""


def non_repeat_substring(string: str):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            window_start = max(window_start, char_frequency[right_char] + 1)
        char_frequency[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccdbe")))


main()
