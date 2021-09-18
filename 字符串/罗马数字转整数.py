# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000





def romanToInt(s):
    d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}

    k = []
    for i, n in enumerate(s):
        a = d.get(s[max(i - 1, 0):i + 1], d[n])
        k.append(a)

    return sum(k)

if __name__ == '__main__':
    print(romanToInt("IV"))