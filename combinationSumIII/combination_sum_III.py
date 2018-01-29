import unittest
from itertools import combinations


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        base_list = [i for i in range(1, 10)]
        combo = combinations(base_list, k)
        return [list(num_set) for num_set in combo if sum(num_set) == n]


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.combinationSum3(3, 7), [[1, 2, 4]])
        self.assertEqual(
            self.solution.combinationSum3(3, 9),
            [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        )


if __name__ == '__main__':
    unittest.main()
