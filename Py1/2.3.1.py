'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b][a;b] на все числа отрезка [c;d][c;d].

Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a≤ba≤b, c≤dc≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.

Sample Input 1:
7
10
5
6
Sample Output 1:
	5	6
7	35	42
8	40	48
9	45	54
10	50	60
Sample Input 2:
5
5
6
6
Sample Output 2:
	6
5	30
Sample Input 3:
1
3
2
4
Sample Output 3:
	2	3	4
1	2	3	4
2	4	6	8
3	6	9	12
'''
# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c<d:
    s = c - 1
    while s<d:
        if s==c - 1:
            print(' ',end='\t')
            s+=1
            continue
        elif s==d-1:
            print(str(s)+'\t'+str(s+1))
            break
        print(s,end='\t')
        s +=1
elif(c==d):
    s = c-1
    while s<=d:
        if s == c-1:
            print(' ',end='\t')
            s+=1
            continue
        elif s == c:
            print(s)
            break
#print('\t')
    
    
for i in range(a,b+1):
    print(i,end='\t')
    for j in range(c,d+1):
        print(j*i,end='\t')
    print(end='\n')