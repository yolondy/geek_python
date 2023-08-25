'''Задача 14: 
Требуется вывести все целые степени двойки(т.е. числа вида 2**k), не превосходящие числа N.'''

import random

n = random.randint(0,64)
print ('n = ', n)
k = 0
flag = True

while flag:
    if 2**k < n:
        print(2**k)
        k+=1 
    else:
        flag = False

