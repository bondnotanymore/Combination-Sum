import unittest
from itertools import combinations as cb


class FindSumCombinations(object):
    """
    This class is used for find all pairs of elements from a
    list of integers that add up to a specific sum/target.

    """

    def __init__(self, nums, target):
        """
        @summary: Initializes the list object from which the pais
                    need to be determined
        @param nums: List of elements
        @type nums: List
        @param target: The target sum
        @type target: int
        """
        self.nums = nums
        self.sum = target

    def __str__(self):

        return "class to find all pairs that add up to the target sum"

    def list_of_pairs(self):
        """
        @summary: find all pairs of elements in the input_list
                    that add up to a specific sum/target
        @param:input_list: Input list that needs to be traversed
        @type: list
        @param: target
        @type: int
        @return: list of pairs split from actual list
        @type: List
        """

        subsets = []

        input_list = self.nums
        target = self.sum

        if not input_list:
            return []

        if len(input_list) == 1 and target not in input_list:
            return []

        if len(input_list) == 2 and sum(input_list) == target:
            return [input_list]

        if len(input_list) == 1 and target in input_list:
            return [input_list]

        my_gen = (list(comb) for comb in cb(input_list, 2) if sum(comb) == target)

        for comb in my_gen:
            subsets.append(comb)
        if target in subsets:
            subsets.append([target])

        return subsets


class TestCombinationSum(unittest.TestCase):

    def test_combination_sum_empty_list(self):

        fsc_object = FindSumCombinations([], 11)
        my_subsets = fsc_object.list_of_pairs()
        self.assertEquals(my_subsets, [])

    def test_combination_sum_single_element_list(self):
        fsc_object = FindSumCombinations([12], 11)
        my_subsets = fsc_object.list_of_pairs()
        self.assertEquals(my_subsets, [])

    def test_combination_sum_single_element_list_1(self):
        fsc_object = FindSumCombinations([11], 11)
        my_subsets = fsc_object.list_of_pairs()
        self.assertEquals(my_subsets, [[11]])
    
    def test_combination_sum_two_element_list(self):
        fsc_object = FindSumCombinations([5, 6], 11)
        my_subsets = fsc_object.list_of_pairs()
        self.assertEquals(my_subsets, [[5, 6]])
    
    def test_combination_sum_general_list(self):
        fsc_object = FindSumCombinations([1, 2, 3, 7, 9, 11], 11)
        my_subsets = fsc_object.list_of_pairs()
        self.assertEquals(my_subsets, [[2, 9], [4, 7], [11]])


if __name__ == '__main__':
    unittest.main()
