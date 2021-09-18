# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。


def merge(nums1, m, nums2, n):
    p1 ,p2 = m - 1 ,n - 1
    right = m + n - 1

    while p1 >=0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[right] = nums1[p1]
            p1 -= 1
        else:
            nums1[right] = nums2[p2]
            p2 -= 1
        right -= 1

    if p2 >= 0:  # 如果nums2中还有剩余的元素
        nums1[0:p2 + 1] = nums2[0:p2 + 1]

    return nums1

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1,m,nums2,n))