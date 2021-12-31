"""Find the Missing Number (easy)


Problem Statement

We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array
has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

Solution

This problem follows the Cyclic Sort pattern. Since the input array contains unique numbers from the
range 0 to ‘n’, we can use a similar strategy as discussed in Cyclic Sort to place the numbers on
their correct index. Once we have every number in its correct place, we can iterate the array to find
the index which does not have the correct number, and that index will be our missing number.

However, there are two differences with Cyclic Sort:

In this problem, the numbers are ranged from ‘0’ to ‘n’, compared to ‘1’ to ‘n’ in the Cyclic Sort.
This will make two changes in our algorithm: In this problem, each number should be equal to its
index, compared to index - 1 in the Cyclic Sort. Therefore => nums[i] == nums[nums[i]] Since the array
will have ‘n’ numbers, which means array indices will range from 0 to ‘n-1’. Therefore, we will ignore
the number ‘n’ as we can’t place it in the array, so => nums[i] < nums.length Say we are at index i.
If we swap the number at index i to place it at the correct index, we can still have the wrong number
at index i. This was true in Cyclic Sort too. It didn’t cause any problems in Cyclic Sort as over
there, we made sure to place one number at its correct place in each step, but that wouldn’t be enough
in this problem as we have one extra number due to the larger range. Therefore, we will not move to
the next number after the swap until we have a correct number at the index i. """


def missing_number(nums: [int]):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1


def main():
    print(missing_number([5, 3, 1, 6, 2]))
    print(missing_number([2, 6, 4, 3, 7, 5]))
    print(missing_number([1, 8, 6, 4, 3, 2]))


main()
