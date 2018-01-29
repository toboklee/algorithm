import unittest


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []

        for com in ops:
            try:
                stack.append(int(com))
            except Exception:
                if com == "C":
                    stack.pop()
                elif com == "D":
                    stack.append(stack[-1] * 2)
                elif com == "+":
                    stack.append(stack[-1] + stack[-2])

        return sum(stack)


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.calPoints(["-21", "-66", "39", "+", "+"]), -63)
        self.assertEqual(self.solution.calPoints(["5", "2", "C", "D", "+"]), 30)
        self.assertEqual(self.solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)


if __name__ == '__main__':
    unittest.main()
