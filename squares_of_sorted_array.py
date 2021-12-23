"""Squaring a Sorted Array (easy)


Problem Statement

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""


def squares_of_sorted_array(arr: list):
    left, right = 0, len(arr) - 1
    squares = [0 for x in arr]
    highest_sq_idx = len(arr) - 1
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2

        if left_square > right_square:
            squares[highest_sq_idx] = left_square
            left += 1
        else:
            squares[highest_sq_idx] = right_square
            right -= 1
        highest_sq_idx -= 1
    return squares


def main():
    print("Squares: " + str(squares_of_sorted_array([-2, -1, 0, 2, 3])))
    print("Squares: " + str(squares_of_sorted_array([-3, -1, 0, 1, 2])))


main()
