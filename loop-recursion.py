#(C)Tsubasa Kato 2/6/2019
#Written for study of loops and recursion.
import random

i = 1
rand_num = (random.randrange(10))

print('The Random Number Picked was:')
print(rand_num)

while i <= rand_num:
	#print("Random Number:")	
	#print(rand_num)
	print("Current Number:")
	print(i)
	i = i + 1
	#to continue this script with more iterations of loop
print('This time, it ended in:') 
result_num = i - 1
print(result_num)
print('times')

print("Recursion Test Starting:")

#recursive function to calculate factorial
#Referenced: http://www.trytoprogram.com/python-programming/python-recursive-function/

def recursion(n):
  if n == 1:
    return 1
  else:
    print ("n:", n)
    return (n * recursion(n-1))

print (recursion(100))
