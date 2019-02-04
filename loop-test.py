import random

i = 1
rand_num = (random.randrange(10))

print('The Random Number Picked was:')
print(rand_num)

while i < rand_num:
	#print("Random Number:")	
	#print(rand_num)
	print("Current Number:")
	print(i)
	i = i + 1
	#to continue this script with more iterations of loop
print('This time, it ended in') 
print(i)
print('times')
