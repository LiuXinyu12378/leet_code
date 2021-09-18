
def longestCommonPrefix(strs):
    n = len(strs)
    if n == 0:
        return ""

    res = strs[0]
    rn = len(res)
    for ri in range(rn):
        for j in range(1, n):
            if ri == len(strs[j]) or strs[j][ri] != res[ri]:
                return res[0:ri]
    return res


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]

    print(longestCommonPrefix(strs))