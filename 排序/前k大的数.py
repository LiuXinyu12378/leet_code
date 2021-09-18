
# def quick_choice(alist, start, end,k):
#     if start > end:
#         return None
#
#     mid = alist[start]
#     low = start
#     high = end
#
#     while low < high:
#         while low < high and alist[high] <= mid:
#             high -= 1
#         alist[low] = alist[high]
#         while low < high and alist[low] > mid:
#             low += 1
#         alist[high] = alist[low]
#
#     alist[low] = mid
#
#     if low == k- 1:
#         return alist[low]
#
#     elif low < k-1:
#         quick_choice(alist, low+1, end, k)
#     elif low > k-1:
#         quick_choice(alist, start, low-1, k)
#
#     # return alist[k - 1]
#
#
# def findKthLargest(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     return quick_choice(nums, 0, len(nums) - 1, k)


def findKthLargest(nums, k):
    n = len(nums)
    l = 0
    r = n - 1
    while True:
        idx =partition(nums, l, r)
        if idx == k - 1:
            return nums[idx]
        elif idx < k - 1:
            l = idx + 1
        else:
            r = idx - 1

# ----左右挖坑互填
def partition( nums, l, r):
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] <= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] >= pivot:
            l += 1
        nums[r] = nums[l]

    nums[l] = pivot
    return l

if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums,k))