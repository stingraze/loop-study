#study on 2/9/2020 
#(C)Tsubasa Kato 
#Referenced: https://www.geeksforgeeks.org/permutation-and-combination-in-python/
#And: https://www.codespeedy.com/get-first-n-items-from-a-list-in-python/

from itertools import permutations
perm = permutations([1,2,3])

for i in list(perm):
	print (i)
	if (i == (1,2,3)):
		print ("yay")
	for y in range(2):	
		print (i[y])