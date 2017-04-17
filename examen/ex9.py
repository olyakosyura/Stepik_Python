"""
Подходящим назовем файл, имеющий расширение .json с данными в формате JSON внутри.
Интересным назовем подходящий файл, данные которого задают JSON объект с полями kind и age в любом регистре (kInD, KINd, Age, ...).
Хорошим назовем интересный файл, значение поля kind равно строке human, а значение поля age равно числу большему или равному 18 (Слова kind, human, age могут быть в любом регистре).

Вам дана файловая структура. Найдите количество хороших файлов в ней.

Пример содержимого хорошего файла:

{"kiND" : "HumAn", "name" : "47", "AGE" : 21}

Пример данных:
sample.zip 

Пример ответа:
214

Основные данные:
data.zip 

"""
import sys
import os
import json
from operator import itemgetter
 

def read_input():
    #with open("input.json", "r") as f:
    #     data = json.load(f)
    data_json = sys.stdin.read()
    data = json.loads(data_json)
    return data

number = 1
kind = r'[k|K][i|I][n|N][d|D]'
age = r'[A|a][g|G][e|E]'
for current_dir, dirs, files in os.walk("data"):
    for file in files:
        if file.endswith('.json'):
            with open(current_dir+"\\"+file, 'r', encoding='utf-8') as jsonfile:
                reader = json.load(jsonfile) #загружаем из файла данные в словарь data
            dict2 = {}
            for key, value in reader.items():
                dict2[key.lower()] = value
           
            if 'kind' in dict2 and 'age' in dict2:
                if dict2['kind'].lower() == 'human' and int(dict2['age'])>=18:
                    number +=1
            print(current_dir+"\\"+file)
            print(reader)
            print(dict2)
            print(number)
 
               
 
print(number - 1)
