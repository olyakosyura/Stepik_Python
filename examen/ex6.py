'''
Вам дана последовательность строк.
В каждой строке при помощи регулярного выражения удалите символы после каждой открывающейся скобки до ближайшей закрывающейся.
Sample Input:
(word) outside (1 open (2 open))
x * (3 + (x - 2) + 2)
Nothing here
Sample Output:
() outside ())
x * () + 2)
Nothing here
'''
import re
import sys
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r'\([^\)]+\)', '()', line))
