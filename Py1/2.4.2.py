'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2
Sample Input 2:
abc
Sample Output 2:
a1b1c1
'''
s=input()
s2=""
k=0
ch=s[0]
for i in s:
    if i==ch :
        k+=1
    else:
        s2=s2+ch+str(k)
        ch=i
        k=1
print (s2+ch+str(k))
