import unittest
from collections import Counter


class Solution(object):
    def subarraySum(self, A, K):
        count = Counter()
        count[0] = 1
        answer = 0
        track = 0
        for x in A:
            track += x  # Sum
            answer += count[track - K]  # If track - K index exists, it's a sub-array
            count[track] += 1
        return answer


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        # TODO: add more test cases. Busy =============
        self.assertEqual(self.solution.subarraySum([1, 1, 1], 2), 2)


if __name__ == '__main__':
    unittest.main()
