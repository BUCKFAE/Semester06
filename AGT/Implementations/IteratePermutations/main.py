"""Demonstrates how to get all possible permutations of a list of numbers"""

from typing import List

def get_permutations(nums: List[int]) -> List[List[int]]:
    """Returns all permutations of the given list"""

    # Stores all permutations
    all_permutations = []

    while True:

        all_permutations.append(nums.copy())

        i = len(nums) - 2

        while nums[i] >= nums[i + 1]:
            i -= 1
            if i == -1:
                return all_permutations

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]


get_permutations(list(range(0, 15)))

