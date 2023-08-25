'''Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.'''

import random
import math

x = random.randint(0,1000)
print ('Peter\'s x = ', x)
y = random.randint(0,1000)
print ('Peter\'s y = ', y)

s = x + y 
p = x * y
print (f's = {s},  p = {p}')

 # x = s - y          -->  p = (s - y)*y
 # y*y - s*y + p = 0   -   equivalent square

d = s*s - 4*p

y1 = (s - math.sqrt(d))/2

y2 = (s + math.sqrt(d))/2

print('Kate\'s x = ', y1)
print('Kate\'s y = ', y2)

