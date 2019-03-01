#Written by Shigeto Baba, Kumamoto, Japan

import random

sel_num = set()
i = 0

print('How may numbers do you want? :', end ='')
num = int(input())

print('min :', end ='')
min = int(input())

print('max :', end ='') 
max = int(input())

while(i != num):
	new_sel_num = random.randrange(min,max,1)
	sel_num.add(new_sel_num)
	i = len(sel_num)
	
print(sel_num)
