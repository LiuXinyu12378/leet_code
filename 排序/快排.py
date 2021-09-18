def quick_sort(alist, start, end):
    if start > end:
        return None


    mid = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] <= mid:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] >= mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)



if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)



