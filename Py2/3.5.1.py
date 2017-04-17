'''

Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv


'''

import csv
primaries = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] in primaries:
            primaries[row[5]] += 1
        else:
            primaries[row[5]] = 0
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

#print(primaries)
#print(primaries.get(max(primaries.values())))
print(get_key(primaries,max(primaries.values())))

