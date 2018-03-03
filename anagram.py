import unittest
import itertools

class Solution(object):
    @staticmethod
    def is_anagram(s, t):
        """
        :type s: str
        :type t: str abc
        :rtype: bool
        """

        return sorted(s) == sorted(t)

    @staticmethod
    def is_anagram_dict(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Map s
        s_dict = {}
        for char in s:
            try:
                s_dict[char] += 1
            except KeyError:
                s_dict.update({char: 1})
                pass

        # Check mapped s with string t
        for char in t:
            try:
                count = s_dict[char]
                s_dict[char] -= 1

                if count < 1:
                    return False
            except KeyError:
                return False

        # Check for any remaining char
        return not any(v > 0 for k, v in s_dict.iteritems())


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        # base case
        self.assertEqual(self.solution.is_anagram("", ""), True)
        self.assertEqual(self.solution.is_anagram_dict("", ""), True)

        # Same letters
        self.assertEqual(self.solution.is_anagram("aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa"), True)
        self.assertEqual(self.solution.is_anagram_dict("aaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaa"), True)

        # long vs short & short vs long
        self.assertEqual(self.solution.is_anagram("anagram1", "anagram"), False)
        self.assertEqual(self.solution.is_anagram_dict("anagram1", "anagram"), False)

        self.assertEqual(self.solution.is_anagram("anagram", "anagram1"), False)
        self.assertEqual(self.solution.is_anagram_dict("anagram", "anagram1"), False)

        # All possible permutations.
        perm = ["".join(perm) for perm in itertools.permutations("anagram")]

        for item in perm:
            self.assertEqual(self.solution.is_anagram("anagram", item), True)
            self.assertEqual(self.solution.is_anagram_dict("anagram", item), True)


if __name__ == '__main__':
    unittest.main()
