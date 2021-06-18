#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests as req
import re
import array
import random

url = 'https://my-calend.ru/names/russian'
page = req.get(url)
soup = BeautifulSoup(page.text, 'lxml')

list = []
z = list




for x in soup.find_all('a', href=True):
    table = x.get_text()
    td_list = x.select('td')
    list.append(table)
    #print(z)

q=1

def reverse(lst):
    return lst[::-1]
    return q
print(*reverse(z), sep=' ')



a = z
x = z
print(*[z for z in a if z.startswith(x)])

# a = z
# x = z
# print(*[s for s in a if s.startswith(x)])

# for a in soup.find_all('a', href=True):
#     print("ссылка:", a['href'])

#
# flist= z[]
# random.choice(flist)

#print(z)
#print('Выберите имя будущего ребенка (1 - муж, 2 - жен, 3 - универсальное, 4 - случ): ')

b = str(input())

if b == '1':
    print(z[113:168])

elif b == '2':
    print(z[57:112])

elif b == '3':
    print(z[3])

elif b == '4':
    print(z[4])

else:
    print('Вы ошиблись')

#получить все ссылки


##################################### request #######################################

# r = re.findall(r'\b[li]\w+.\w+', 'http://server.com/downloads/life_changing_plans.pdf')
#r2 = re.findall(r'\b[li]\w+.\w+', 'http://server.com/downl/life_changing_plans.doc')
#r3 = re.findall(r'\b[r]\w+.\w+', 'https://server-dot.com/root.pdf')

# print(r)
# print(r2)
# print(r3)
