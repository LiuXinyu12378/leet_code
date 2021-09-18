

def maxSubArray(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    max_num = nums[0]
    num = nums[0]
    for i in range(1, len(nums)):

        if max_num < nums[i]:                 #动态规划找到各个子序列max_num
            max_num = nums[i]
        elif max_num >= nums[i]:
            max_num = max_num + nums[i]

        if num < max_num:                     # 保留最大的子序列num
            num = max_num

    return num


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print(maxSubArray(nums))
