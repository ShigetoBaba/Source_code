#Written by Shigeto Baba, Kumamoto, Japan

import random

sel_num = set()		#No duplication

print('How may numbers do you want? :', end ='')
num = int(input())

print('min :', end ='')
min = int(input())

print('max :', end ='') 
max = int(input())

while(len(sel_num) != num):
	new_sel_num = random.randrange(min, max)
	sel_num.add(new_sel_num)
	
print(sel_num)
