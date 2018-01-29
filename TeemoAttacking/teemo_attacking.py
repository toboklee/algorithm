import unittest


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0

        result = duration
        prev = timeSeries[0]

        for i in xrange(1, len(timeSeries)):
            if timeSeries[i] - prev < duration:
                result += timeSeries[i] - prev
            else:
                result += duration

            prev = timeSeries[i]

        return result


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.findPoisonedDuration([1, 4], 2), 4)
        self.assertEqual(self.solution.findPoisonedDuration([1, 2], 2), 3)
        self.assertEqual(self.solution.findPoisonedDuration([], 100000), 0)


if __name__ == '__main__':
    unittest.main()
