'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4
'''
# put your python code here
input_str = ""
matrix = []
resMatrix = []
while True:
  input_str = input()
  if input_str != "end":
    lst = list(map(int, input_str.split()))
    lst.insert(0, lst[len(lst) - 1])
    lst.append(lst[1])
    matrix.append(lst)
  else:
    matrix.insert(0, lst)
    matrix.append(matrix[1])
    for i in range(len(matrix) - 2): resMatrix.append([0] * (len(matrix[0]) - 2)) 
    break
for i in range(len(resMatrix)):
  for j in range(len(resMatrix[i])): resMatrix[i][j] = matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+2]+matrix[i+2][j+1]
for i in range(len(resMatrix)):
  for j in range(len(resMatrix[i])): print(resMatrix[i][j], end=" ")
  print()
