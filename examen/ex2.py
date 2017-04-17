"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "===".

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен единице, если в восьми соседних клетках находится не меньше трёх и не больше шести единиц. В противном случае элемент в позиции i, j равен нулю. У крайних элементов соседние элементы находятся с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
0 0 0 0
0 1 1 0
0 1 1 0
0 0 0 0
===
Sample Output 1:
0 0 0 0
0 1 1 0
0 1 1 0
0 0 0 0
Sample Input 2:
1 0
1 0
1 0
===
Sample Output 2:
0 1
0 1
0 1
"""
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == '===':
        break
    m.append([int(s) for s in n.split()]) 
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[i-1][j-1], m[(i+1)%li][j], m[(i+1)%li][j-1], m[(i+1)%li][(j+1)%lj], m[i-1][(j+1)%lj], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        if new[i][j]>=3 and new[i][j]<=6:
            new[i][j] = 1
        else:
            new[i][j] = 0
        print(new[i][j], end =' ')
    print()
