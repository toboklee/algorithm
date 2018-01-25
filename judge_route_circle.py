import unittest
from math import sqrt


class Solution(object):
    def __init__(self):
        self.x_vector = {'R': 1, 'L': -1}
        self.y_vector = {'U': 1, 'D': -1}
        self.x = 0
        self.y = 0

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        for char in moves:
            if char in self.x_vector:
                self.x += self.x_vector[char]
            else:
                self.y += self.y_vector[char]

        return False if self.get_distance(self.x, self.y) > 0 else True

    @staticmethod
    def get_distance(x, y):
        return sqrt(x * x + y * y)


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertTrue(self.solution.judgeCircle("UD"))
        self.assertFalse(self.solution.judgeCircle("LL"))


if __name__ == '__main__':
    unittest.main()
