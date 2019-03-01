##Written by Shigeto Baba, Kumamoto, Japan

import random

num = set([])
i = 0

while(i != 6):
	new_num = random.randrange(1,43)
	num.add(new_num)
	i = len(num)
	
print(num)
	
