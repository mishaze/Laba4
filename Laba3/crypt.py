from collections import Counter
import string


class TXT:

    def read_string(self, txt):
        file = open(txt, "r")
        string = file.read()
        file.close()
        return string.lower()

    def record(self, result, output="output.txt"):
        file = open(output, "w")
        file.write(result)
        file.close()
        return 0

    def fanalis(self, txt):
        text = open(txt).read()
        your_counts = Counter(text.lower())
        return your_counts


class Coder:
    __alphabet = string.ascii_lowercase

    def __init__(self, msg):
        self.__msg = msg

    def cesar(self, shift=3):
        ret = ""
        for x in self.__msg:
            if (x in self.__alphabet) and (-(len(self.__alphabet)) < shift < len(self.__alphabet)):
                ind = self.__alphabet.index(x)
                if ind + shift < len(self.__alphabet):
                    ret += self.__alphabet[ind + shift]
                elif ind + shift >= len(self.__alphabet):
                    ret += self.__alphabet[(ind + shift) - len(self.__alphabet)]
            else:
                ret += x
        return ret

    def jener(self, key='hello', f=1):
        cipher = ""
        j = 0
        if f != 0 and f != 1:
            return
        for i in self.__msg:
            if i not in self.__alphabet:
                cipher += i

            else:
                cipher += self.__alphabet[
                    (self.__alphabet.index(i) + self.__alphabet.index(key[j]) * f) % len(self.__alphabet)]

                if j == len(key) - 1:
                    j = 0
                else:
                    j += 1

        return cipher

    def Playfair(self, key=''):
        matrix = self.__matrix(key)
        print(matrix)
        res = []
        for i in self.__msg:
            if i in self.__alphabet and i != 'j':
                res.append(i)

        res.append(' ')

        k = 0
        while True:
            if res[k] == ' ' or res[k + 1] == ' ':
                break
            if res[k] == res[k + 1]:
                res.insert(k + 1, 'x')

            k = k + 2
        res.pop()
        if len(res) % 2 == 1:
            res.append('x')
        for i in range(0, len(res), 2):
            for j in range(5):
                if matrix[j].count(res[i]) == matrix[j].count(res[i + 1]):
                    continue
            for j in range(5):
                for k in range(5):
                    pass
        return ''.join(res)

    def __matrix(self, key):
        b = key + self.__alphabet
        l1 = []
        for i in b:
            if b.count(i) > 1 or i == 'j':
                c = b.rfind(i)
                b = list(b)
                b.pop(c)
                b = ''.join(b)

        for i in range(1, 6):
            l1.append(list(b[5 * i - 5:5 * i]))
            print(l1[i - 1])
        return l1


class Decoder:
    pass


txt = TXT()
a = Coder(txt.read_string("ex.txt"))
print(a.Playfair())
