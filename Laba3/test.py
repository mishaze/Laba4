import string

a = "abcdefghijklmnopqrstuvwxyz"


def matrix(key):
    b = key + a
    l1 = []
    for i in b:
        if b.count(i) > 1 or i == 'j':
            c = b.rfind(i)
            b = list(b)
            b.pop(c)
            b = ''.join(b)

    for i in range(1,6):
        l1.append(list(b[5*i-5:5*i]))
        print(l1[i-1])
    return l1
matrix("hay")