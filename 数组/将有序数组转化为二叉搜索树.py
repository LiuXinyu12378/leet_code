# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    def helper(left, right):
        if left > right:
            return None

        # 总是选择中间位置左边的数字作为根节点
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums) - 1)





if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(sortedArrayToBST(nums))
