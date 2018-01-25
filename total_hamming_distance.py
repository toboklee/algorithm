import unittest
from itertools import combinations


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        # TODO ==========================================
        # Too slow refactor combination finding algorithm
        combos = combinations(nums, 2)

        for combo in combos:
            result += self.hamming_distance(combo[0], combo[1])

        return result

    def hamming_distance(self, x, y):
        return bin(x ^ y).count('1')


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.totalHammingDistance([4, 14, 2]), 6)


if __name__ == '__main__':
    unittest.main()
