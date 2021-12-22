"""Longest Substring with K Distinct Characters (medium)

Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: "
          + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
