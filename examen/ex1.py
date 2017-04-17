"""
На первой строчке подаётся числа n и m. Вам необходимо прочесть n строк и вывести m самых частых слов и их количество (в любом порядке)
Sample Input:
3 3
aaa cbc aaa
bbb
cbc ggg aaa bbb
Sample Output:
aaa 3
bbb 2
cbc 2
"""
n,m = map(int, input().split())
d = {}
for i in range(0,n):
    s = input().split()
    for j in s:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
d = sorted(d.items(), key=lambda x:x[1])
for i in range(1, m+1):
    print(d[len(d)-i][0],d[len(d)-i][1])
