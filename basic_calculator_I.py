import re
import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(r'[\s\t]+', '', s)
        operator_list = [char for char in s if not char.isdigit()]
        num_list = [int(num) for num in re.split(r'[+-/*]', s)]

        operator_p = 0

        # TODO ================================================================================
        # Both pop and append operations are extremely slow. Refactor later.
        # Find a way to merge both (multiplication and division) and (addition and subtraction)
        while operator_p < len(operator_list):
            if operator_list[operator_p] == '*' or operator_list[operator_p] == '/':
                operator = operator_list.pop(operator_p)

                first = num_list[operator_p]
                second = num_list.pop(operator_p + 1)

                if operator == '*':
                    num_list[operator_p] = first * second
                else:
                    num_list[operator_p] = first / second
            else:
                operator_p += 1

        operator_p = 0

        while operator_p < len(operator_list):
            if operator_list[operator_p] == '-' or operator_list[operator_p] == '+':
                operator = operator_list.pop(operator_p)

                first = num_list[operator_p]
                second = num_list.pop(operator_p + 1)

                if operator == '+':
                    num_list[operator_p] = first + second
                else:
                    num_list[operator_p] = first - second
            else:
                operator_p += 1

        return num_list[0]


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.calculate("2+2"), 4)
        self.assertEqual(self.solution.calculate("0-123123"), -123123)
        self.assertEqual(self.solution.calculate("3+3+2+5/3*2+1-1"), 10)


if __name__ == '__main__':
    unittest.main()
