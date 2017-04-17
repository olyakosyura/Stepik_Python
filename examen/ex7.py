"""
Вам дана ссылка на HTML-документ.
Посчитайте в нем количество ссылок, ведущие на несуществующие документы.

Ссылка на страницу – это тег <a ... href="link" ...>...</a>
Документ считается несуществующим, если при его запросе сервер вернет сообщение с status code равным 404.

Sample Input:
https://stepic.org/media/attachments/lesson/25670/sample.html
Sample Output:
2
"""


import requests
import re

linkToHTMLFile = "https://stepic.org/media/attachments/lesson/25670/sample.html"
linkToHTMLFile = "https://vk.com/feed"
linkToHTMLFile = input()
response = requests.get(linkToHTMLFile)
if response.status_code == 200:
    data = response.text
#string = r"<a (.*?)href(.*?)=(.*?)(((.*?):\/\/)|(\.\.)|)((.*?)(\/|:))*?(\"|')>(.*)"
string = r"<a (.*?)href(.*?)=(\"http((.*?))\")(.*?) "
result = []
num = 0
n = 0
#print(data)
for link in re.findall(string, data):
    #print(link)
    domain = 'http'+link[3]
    
    #domain = domain[1:(len(domain)-1)]
    #print(domain)
    response = requests.get(domain)
    if response.status_code == 404:
        num += 1
        #print(num)
    if response.status_code == 200:
        n +=1
#print(n)
print(num)


