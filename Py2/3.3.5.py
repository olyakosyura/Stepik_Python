'''

Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей
(тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa
Sample Output:
blabla is a tandem repetition
123123 is good too


'''

import sys
import re
cat = r"\b(\w+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    m = re.findall(cat, line)
    if len(m)> 0:
        print(line)
        
