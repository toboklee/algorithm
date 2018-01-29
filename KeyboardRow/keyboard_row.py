import re
import unittest


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        pattern_group_one = '[qwertyuiop]*'
        pattern_group_two = '[asdfghjkl]*'
        pattern_group_three = '[zxcvbnm]*'

        regex_pattern = '(?i)^({}|{}|{})$'.format(
            pattern_group_one,
            pattern_group_two,
            pattern_group_three
        )

        result = filter(lambda x: re.compile(regex_pattern).match(x), words)
        return result


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(self.solution.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])


if __name__ == '__main__':
    unittest.main()
