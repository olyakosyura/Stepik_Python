'''

Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
Sample Input:
\w denotes word character
No slashes here
Sample Output:
\w denotes word character

'''

import sys
import re
cat = r"\\"
for line in sys.stdin:
    line = line.rstrip()
    m = re.findall(cat, line)
    if len(m)> 0:
        print(line)
        
