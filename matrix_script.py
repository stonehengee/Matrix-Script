n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in xrange(n):
    matrix_t = str(raw_input())
    matrix.append(matrix_t)

regex_char = r"[A-Z, a-z, 0-9]"
regex_char_end = r"([A-Z, a-z, 0-9]+)*$"
regex_nonchar = r"([^A-Z, a-z, 0-9]+|\s+)*"
regex_nonchar_end = r"([^A-Z, a-z, 0-9]+|\s+)*$"

# n = 2
# m = 4
# matrix = ['# i#', ' @#U']

class MatrixMatch:
    def __init__(self):
        self.output = ""
        self.buff = ""

    def matrix_match(self, x):
        self.output += self.buff
        print(x)
        self.output += x
        return ""

answer = MatrixMatch()

import re

i = 0
matrix_unwrap = ""

while i < m:
    for each in matrix:
        matrix_unwrap += each[i]
    i += 1

# print(matrix_unwrap)

i = 0

while i < len(matrix_unwrap):
    # i -= 1
    while not matrix_unwrap[0].isalnum() and not bool(re.match(regex_nonchar_end, matrix_unwrap[i:])):
        answer.output += matrix_unwrap[0]
        matrix_unwrap = matrix_unwrap[1:]
    while matrix_unwrap[i].isalnum():
        answer.output += matrix_unwrap[i]
        i += 1
    while not bool(re.match(regex_nonchar_end, matrix_unwrap[i:])):
        matrix_unwrap1 = matrix_unwrap.replace(re.match(regex_nonchar, matrix_unwrap[i:]).group(), " ", 1)
        matrix_unwrap = matrix_unwrap1
        answer.output += " "
        # i += 1
        break
    while bool(re.match(regex_nonchar_end, matrix_unwrap[i:])) or bool(re.match(regex_char_end, matrix_unwrap[i:])):
        answer.output += matrix_unwrap[i:]
        print (answer.output)
        i = len(matrix_unwrap)
        break
        # exit()
    i += 1



# while i < m:
    # for each in matrix:
        # e = each[i]
        # t = bool(re.match(regex_nonchar, e))
       # print(t)
        # answer.buff = {False: answer.matrix_match(e)}.get(t, " ")
    # i += 1

# print answer.output













### We're going to unravel the matrix and use ([^A-Z, a-z, 0-9]+|\s+)* and ([^A-Z, a-z, 0-9]+|\s+)*$ to do replacements



# \w*\S
