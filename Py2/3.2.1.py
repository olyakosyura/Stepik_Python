s= input()
a = input()
b = input()
k=0
if (a in s) and (a in b):
    k = 100
while a in s:
    s = s.replace(a, b)
    if a in b:
        k = 100
        break
    else:
         k += 1 
if k == 100:
    print('Impossible')
else:
    print(k)
