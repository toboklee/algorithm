import unittest


class Solution(object):
    @staticmethod
    def is_palindrome(x):
        """
        Determins whether x is a Palindromic number or not
        """
        
        # Assume negative number is not a palindromic number.
        if x < 0:
            return False

        ten_base = 1
        
        # Determine num size with a base of 10
        while x / ten_base >= 10:
            ten_base *= 10

        while x > 0:
            left_num, right_num = x / ten_base, x % 10
            if left_num != right_num:
                return False
            
            # Update and prep for next iteration.
            x = (x % ten_base) / 10
            ten_base /= 100

        return True
        
        
class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.is_palindrome(0), True)
        self.assertEqual(self.solution.is_palindrome(11), True)
        self.assertEqual(self.solution.is_palindrome(-1), False)
        self.assertEqual(self.solution.is_palindrome(1311), False)
        self.assertEqual(self.solution.is_palindrome(11311), True)

        long_int = 123123123123123123123123123123321321321321321321321321321321
        self.assertEqual(self.solution.is_palindrome(long_int), True)


if __name__ == '__main__':
    unittest.main()
