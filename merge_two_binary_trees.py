import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None

        if t1 and t2:
            t1.val += t2.val
        elif not t1:
            t1 = TreeNode(t2.val)

        t1_left = t1.left if t1 and t1.left else None
        t2_left = t2.left if t2 and t2.left else None
        t1.left = self.mergeTrees(t1_left, t2_left)

        t1_right = t1.right if t1 and t1.right else None
        t2_right = t2.right if t2 and t2.right else None
        t1.right = self.mergeTrees(t1_right, t2_right)

        return t1


class MainTestCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def runTest(self):
        # TODO ============================
        # Add test cases. Passed on leetcode
        pass


if __name__ == '__main__':
    unittest.main()
