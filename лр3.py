
import os
my = os.environ['SECRET_KEY']
print(my)

#Задание номер 1 (делала с Мурзагалиевой Эльмирой)
import os
GOSHKO = os.environ['GOSHKO']
print(GOSHKO)

import os
SECRET_KEY_GOSHKO = os.environ['SECRET_KEY_GOSHKO']
print(SECRET_KEY_GOSHKO)

import os
GOSHKO_KEY = os.environ['GOSHKO_KEY']
print(GOSHKO_KEY)

import os
SECRET_KEY = os.environ['SECRET_KEY']
print(SECRET_KEY)

#Задание номер 2 вариант 5 (Делала с Черепановым Майеславом)
#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 20000 #Замена выполнена верно
Am_lst = []
C_ost_lst = []
for i in range(6):#Замена выполнена верно
  Am = (C - L)/T
  C_ost -= Am.subs({C: 20000, T:6, L:0}) #Замена выполнена верно
  Am_lst.append(round(Am.subs({C: 20000, T:6, L:0}), 2)) #Замена выполнена верно
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst) 
print('C_ost_lst:', C_ost_lst) 
#пункт 2

Aj = 0
C_ost = 20000 #Замена выполнена верно
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(6): #Замена выполнена верно
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 20000, T:6, k:2}) # Замена выполнена верно
  Am_lst_2.append(round(Am.subs({C: 20000, T:6, k:2}), 2)) #Замена выполнена верно
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 20000   #Замена выполнена верно
Am_lst = []
C_ost_lst = []
for i in range(6):  #Замена выполнена верно
  Am = (C - L) / T
  C_ost -= Am.subs ({C:20000, T:6, L:0})  #Замена выполнена верно
  Am_lst.append(round(Am.subs({C: 20000, T:6, L:0}), 2))  #Замена выполнена верно
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 20000  #Замена выполнена верно
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(6):  #Замена выполнена верно
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 20000, T:6, k:2})  #Замена выполнена верно
   Am_lst_2.append(round(Am.subs({C: 20000, T:6, k:2}), 2)) #Замена выполнена верно
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 7)  #Замена выполнена верно
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt 
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart8.png')


vals = Am_lst
labels = [str(x) for x in range(1,7)]    #Замена выполнена верно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  #Замена выполнена верно
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart9.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,7)]  #Замена выполнена верно
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) #Замена выполнена верно
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart10.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.png')
#Задание сделано правильно, 5 баллов, возьми с полки пирожок

#Задание 3 сделано


#Задание номер 4 (делала с Полиной Зайцевой)
#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 100000
Am_lst = []
C_ost_lst = []
for i in range(5):
  Am = (C - L)/T
  C_ost -= Am.subs({C: 100000, T:5, L:0})
  Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst) 
print('C_ost_lst:', C_ost_lst) 
#пункт 2

Aj = 0
C_ost = 100000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 100000, T:5, k:2})
  Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2)) #Что это значит? (Зайцева П.)
  #Ответ: это значит, что мы добавляем в список C_ost_lst_2 значение C_ost, округленное до 2 знаков после запятой (Гошко Я.)
  #Ответ правильный, 5 баллов (Зайцева П.)
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 30000
Am_lst = []
C_ost_lst = []
for i in range(8):
  Am = (C - L) / T
  C_ost -= Am.subs ({C:30000, T:8, L:0})
  Am_lst.append(round(Am.subs({C: 30000, T:8, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 30000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 30000, T:8, k:2})
   Am_lst_2.append(round(Am.subs({C: 30000, T:8, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 9) #Что это значит? (Зайцева П.) 
#Ответ: это значит, что мы создаем переменную Y, которая будет принимать значения от 1 до 8 (Гошко Я.)
#Ответ правильный, 5 баллов (Зайцева П.)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt #Что это значит? (Зайцева П.)
#Ответ: это значит, что мы импортируем библиотеку matplotlib.pyplot, которая позволяет нам строить графики (Гошко Я.)
#Ответ правильный, 5 баллов (Зайцева П.)
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart7.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart8.png')


vals = Am_lst
labels = [str(x) for x in range(1,9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart9.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart10.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart11.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart12.png')


#Индивидуальная часть 

#Контейнер расчета

from sympy import *
k, T, C, L = symbols('k C T L')

#пункт 1

C_ost = 2000000
Am_lst = []
C_ost_lst = []
for i in range(16):
  Am = (C - L)/T
  C_ost -= Am.subs({C: 2000000, T:16, L:0})
  Am_lst.append(round(Am.subs({C: 2000000, T:16, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am.lst:', C_ost_lst)
print('C_ost_lst:', C_ost_lst)

#пункт 2

Aj = 0
C_ost = 2000000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(16):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 2000000, T:16, k:2})
  Am_lst_2.append(round(Am.subs({C: 2000000, T:16, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am.lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Пункт 3
#Линейный способ

from sympy import *
k, T, C, L =symbols("k C T L")

C_ost = 2000000
Am_lst = []
C_ost_lst = []
for i in range(16):
  Am = (C - L) / T
  C_ost -= Am.subs ({C:2000000, T:16, L:0})
  Am_lst.append(round(Am.subs({C: 2000000, T:16, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#Способ уменьшаемого остатка 

Aj = 0 
C_ost = 2000000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(16):
   Am = k * 1 / T * (C - Aj)
   C_ost -= Am.subs({C: 2000000, T:16, k:2})
   Am_lst_2.append(round(Am.subs({C: 2000000, T:16, k:2}), 2))
   Aj += Am
   C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода 

import pandas as pd
Y = range(1, 17)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])
print(tfame)
print(tfame2)

#Контейнер визуализатора 

import numpy as np 
import matplotlib.pyplot as plt 
plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
plt.savefig('chart1.png')
plt.figure()
plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
plt.savefig('chart2.png')


vals = Am_lst
labels = [str(x) for x in range(1,17)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals, 
  labels = labels, 
  autopct = '%1.1f%%', 
  shadow = True, 
  explode = explode, 
  wedgeprops = {'lw':1, 'ls':'--', 'edgecolor': 'k'},
  rotatelabels = True  
)
ax.axis("equal")
plt.savefig('chart3.png')

vals = Am_lst_2
labels = [str(x) for x in range (1,17)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
  vals,
  labels = labels,
  autopct = '%1.1f%%',
  shadow = True,
  explode = explode,
  wedgeprops = {'lw':1, 'ls': '--', 'edgecolor': "k"},
  rotatelabels = True
)
ax.axis("equal")
plt.savefig('chart4.png')

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame_am = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2_am = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])
plt.bar(tfame['Y'], tfame['Am_lst'])
plt.savefig('chart5.jpeg')
plt.figure()
plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.savefig('chart6.png')

