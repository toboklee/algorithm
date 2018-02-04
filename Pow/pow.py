import unittest


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:  # Negative --> positive conversion
            return 1 / self.myPow(x, -n)
        if n % 2:  # Odd n
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.myPow(2, 10), 1024)
        self.assertEqual(self.solution.myPow(2.1, 3), 9.26100)

if __name__ == '__main__':
    unittest.main()