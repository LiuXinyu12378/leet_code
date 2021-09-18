def strStr(haystack, needle):
    a = len(needle)
    b = len(haystack)
    if a == 0:
        return 0
    i = j = 0
    next = getnext(a, needle)
    while (i < b and j < a):
        if j == -1 or needle[j] == haystack[i]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == a:
        return i - j
    else:
        return -1


def getnext(a, needle):
    next = ['' for i in range(a)]
    j, k = 0, -1
    next[0] = k
    while (j < a - 1):
        if k == -1 or needle[k] == needle[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    print("next:",next)
    return next

if __name__ == '__main__':
    haystack = "aabaabaafa "
    needle = "aabaaf"

    print(strStr(haystack,needle))

