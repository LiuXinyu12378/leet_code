

def removeElement(nums,val):
    # while val in nums:
    #     nums.remove(val)
    # return len(nums)

    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return j,nums[:j]

if __name__ == '__main__':
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2

    nums = [3, 2, 2, 3]
    val = 3

    print(removeElement(nums,val))
