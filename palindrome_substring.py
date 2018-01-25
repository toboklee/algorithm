import unittest


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        length = len(s)

        for i in xrange(length):
            for j in xrange(i, length):
                target = s[i:j + 1]
                target_reverse = s[i:j + 1][::-1]
                if target == target_reverse:
                    res += 1
        return res


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        self.assertEqual(
            self.solution.countSubstrings(["aaa"]),
            ["a", "a", "a", "aa", "aa", "aaa"]
        )
        self.assertEqual(
            self.solution.countSubstrings(["abc"]),
            ["a", "b", "c"]
        )
        self.assertEqual(
            self.solution.countSubstrings(["a"]),
            ["a"]
        )


if __name__ == '__main__':
    unittest.main()
