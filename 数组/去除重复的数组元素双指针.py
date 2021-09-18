


def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j+1,nums[:j+1]


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums))