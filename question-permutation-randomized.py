#Question Permutation study on 2/9/2020 19:16PM
#(C)Tsubasa Kato 
#Referenced: https://www.geeksforgeeks.org/permutation-and-combination-in-python/
#And: https://www.codespeedy.com/get-first-n-items-from-a-list-in-python/
from itertools import permutations
perm = permutations([1,2,3,4])
print ("start!")
for i in list(perm):
	print (i)
	if (i == (1,2,3,4)):
		print ("yay")
	for y in range(2):
		#Making some random questions
		prev_y = i[y] - 1

	if (prev_y ==  3 and i[y] == 4):	
		print ("What is")
	elif (prev_y == 2 and i[y] == 3):
		print ("When is")
	elif (prev_y == 1 and i[y] == 2):
		print ("When will")
		


