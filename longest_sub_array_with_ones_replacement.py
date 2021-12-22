"""Longest Subarray with Ones after Replacement (hard)


Problem Statement

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def length_of_longest_subarray_with_ones(arr: list, k: int):
    window_start, max_length, max_frequency = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_frequency += 1

        current_window_length = window_end - window_start + 1
        if current_window_length - max_frequency > k:
            if arr[window_start] == 1:
                max_frequency -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_subarray_with_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_subarray_with_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
