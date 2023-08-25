'''Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть'''

import random

n = int(input())
tails = random.randint(0,n)
print ('number of tails: ', tails)
heads = n - tails
print ('number of heads%:', heads)


if tails > heads:
    print('number of coins to flip: ', heads)
elif tails == heads:
    print ('draw')
else:
    print ('number of coins to flip: ', tails)