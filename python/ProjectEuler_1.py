# pip install virtualenv 
# # pip install virtualenvwrapper
# pip install virtualenvwrapper-win  
# mkvirtualenv ideaswatch-scrapper
# workon ideaswatch-scrapper
# pip install -r requirements.txt
# pip freeze >> requirements.txt
# deactivate # or source deactivate


# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
from functools import reduce



def get_sum_of_multiples_of_3_5_below(limit):
	multiple_sum = 0
	for counter in range(3, limit):
		if(counter%3==0 or counter%5==0):
			# print(f"{counter} is a multiple of 3 or 5")
			multiple_sum += counter

	return multiple_sum





def do_sum(x1, x2): return x1 + x2

def get_sum_of_multiples_using_sieve_of_3_5_below(limit):
	sieve = [0] * limit
	for counter in range(3, limit, 3):
		sieve[counter] = counter
	for counter in range(5, limit, 5):
		sieve[counter] = counter

	return reduce(do_sum, sieve)






# [2 * uo + ((uf/r) - 1)r] * (uf/r) / 2 # uo first term, uf last term, reason is the progression increment
def get_arithmetic_progression_sum(reason, uo, uf): return (2 * uo + ((uf / reason) - 1) * reason) * (uf / reason)/ 2

def get_sum_of_multiples_using_arithmetic_progressions_of_3_5_below(limit):
	scm = 3 * 5
	multiple_sum = 0
	
	for up_counter in range(1, scm + 1): # + 1 to account for case where limit is already a multiple of scm  
		down_counter = limit - up_counter
		if(down_counter % scm == 0):
			multiple_sum -= get_arithmetic_progression_sum(scm, scm, down_counter)
			break


	for up_counter in range(1, 3 + 1):
		down_counter = limit - up_counter			
		if(down_counter % 3 == 0):
			multiple_sum += get_arithmetic_progression_sum(3, 3, down_counter)
			break


	for up_counter in range(1, 5 + 1):
		down_counter = limit - up_counter			
		if(down_counter % 5 == 0):
			multiple_sum += get_arithmetic_progression_sum(5, 5, down_counter)
			break

	return multiple_sum






if __name__ == "__main__": 
	start = time.time()
	print(get_sum_of_multiples_of_3_5_below(10000000))
	end = time.time()
	print(f"Operation took: {end - start:.2f}sec to complete")

	start = time.time()
	print(get_sum_of_multiples_using_sieve_of_3_5_below(10000000))
	end = time.time()
	print(f"Operation took: {end - start:.2f}sec to complete")

	start = time.time()
	print(get_sum_of_multiples_using_arithmetic_progressions_of_3_5_below(10000000))
	end = time.time()
	print(f"Operation took: {end - start:.2f}sec to complete")
