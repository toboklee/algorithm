import unittest


class Solution(object):
    @staticmethod
    def isToeplitzMatrix(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        row_count = len(matrix)
        column_count = len(matrix[0])

        if row_count == 1 or column_count == 1:
            return True

        prev_row = matrix[0]

        for i in xrange(1, row_count):
            row = matrix[i]

            if prev_row[:-1] != row[1:]:
                return False

            prev_row = row

        return True


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.isToeplitzMatrix([[1]]), True)
        self.assertEqual(self.solution.isToeplitzMatrix([[1,2]]), True)
        self.assertEqual(self.solution.isToeplitzMatrix([[1],[2]]), True)
        self.assertEqual(self.solution.isToeplitzMatrix([[1,2],[2,2]]), False)
        self.assertEqual(self.solution.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]), True)


if __name__ == '__main__':
    unittest.main()
