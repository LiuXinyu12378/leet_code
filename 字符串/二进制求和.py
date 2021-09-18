

def addBinary(a,b):

    return "{0:b}".format(int(a,2)+int(b,2))

if __name__ == '__main__':
    a = "1010"
    b = "1011"

    print(addBinary(a,b))


