'''
Выведите таблицу размером n×nn×n, заполненную числами от 11 до n2n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
n = int(input())
a, s = 1, n
matrix = []
for i in range(n): matrix.append([0] * (n))
while a <= (s ** 2):
  for i in range(s-n, n):
    matrix[s-n][i] = a
    a += 1
  for i in range(s-n+1, n):
    matrix[i][n-1] = a
    a += 1
  for i in range(n-2, s-n-1, -1):
    matrix[n - 1][i] = a
    a += 1
  for i in range(n-2, s-n, -1):
    matrix[i][s-n] = a
    a += 1
  n -= 1
for i in range(len(matrix)):
  for j in range(len(matrix)): print(matrix[i][j], end=" ")
  print()
