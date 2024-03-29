# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
# https://www.mathsisfun.com/numbers/fibonacci-sequence.html

import time
import math








sqrt_5 = math.sqrt(5)
phi_plus  = (1 + sqrt_5)/2
phi_minus = (1 - sqrt_5)/2

# fib(n) = (phi_plus ^ n - phi_minus ^ n) / sqrt_5
# every nth number is a multiple of xn
def get_fib_number_at(index): return int((math.pow(phi_plus, index) - math.pow(phi_minus, index)) / sqrt_5)

def get_closest_fibonacci_number_index(limit):
	# index = (2 * log(limit) + log(5)) / (2 * log(phi_plus))
	index = int(math.floor((2 * math.log(limit) + math.log(5)) / (2 * math.log(phi_plus)))) 
	fib = get_fib_number_at(index)
	# print(f"Fibonnaci number at index {index} is: {fib}")

	while(fib > limit):
		index -= 1
		fib = get_fib_number_at(index)
		# print(f"Fibonnaci number at index {index} is: {fib}")

	return index

def get_sum_of_even_fibonacci_numbers_below(limit):

	max_index = get_closest_fibonacci_number_index(limit)	

	# the first even fibonacci number "2" has an index of "3". 
	# Thereafter, every "3"rd term is even
	# https://www.mathsisfun.com/numbers/fibonacci-sequence.html

	even_fib_sum = 0
	for index in range(3, max_index + 1, 3):
		even_fib_sum += get_fib_number_at(index)

	return even_fib_sum

def get_optimized_sum_of_even_fibonacci_numbers_below(limit):

	max_index = get_closest_fibonacci_number_index(limit)	

	# the first even fibonacci number "2" has an index of "3". 
	# Thereafter, every "3"rd term is even
	# https://www.mathsisfun.com/numbers/fibonacci-sequence.html

	# see get_sum_by_brute_force_and_multiples_of_even_fibonacci_numbers_below
	# for an explaination
	f3_n_1 = 2
	f3_n = 8
	even_fib_sum = f3_n_1
	for _ in range(6, max_index + 1, 3):
		even_fib_sum += f3_n

		f3_n, f3_n_1 = 4*f3_n + f3_n_1, f3_n

	return even_fib_sum







# Since the fibonnaci sequence grows so quickly, the brute force might be something to consider.
# Although, the current implementation is actually fast enough not to be a problem
# The closest fibonacci number to 4000000 has an index of only 33

def get_sum_by_brute_force_of_even_fibonacci_numbers_below(limit):

	fn = 1
	fn_1 = 0
	even_fib_sum = 0

	while(fn < limit):
		if(fn % 2 == 0):
			even_fib_sum += fn

		# temp = fn
		# fn = fn + fn_1
		# fn_1 = temp
		fn, fn_1 = fn + fn_1, fn

	return even_fib_sum






# One could also exploit the fact that every nth term is a multiple of xn so that
# a general expression for these multiples can be developped
# f3_next = f3_n + 4*f3_n_1

def get_sum_by_brute_force_and_multiples_of_even_fibonacci_numbers_below(limit):

	f3_n_1 = 2
	f3_n = 8
	even_fib_sum = f3_n_1

	while(f3_n < limit):
		even_fib_sum += f3_n

		# temp = f3_n
		# f3_n = 4*f3_n + f3_n_1
		# f3_n_1 = temp

		f3_n, f3_n_1 = 4*f3_n + f3_n_1, f3_n

	return even_fib_sum











if __name__ == "__main__":  
	start = 1000*time.time()
	limit = 4000000
	print(f"The sum of even fibonacci numbers below {limit} is: {get_sum_of_even_fibonacci_numbers_below(limit)}")
	# print(get_closest_fibonacci_number_index(4000000))
	end = 1000*time.time()
	print(f"Operation took {end - start:.2f}msec to complete")

	start = 1000*time.time()
	limit = 4000000
	print(f"The sum of even fibonacci numbers below {limit} is: {get_optimized_sum_of_even_fibonacci_numbers_below(limit)}")
	# print(get_closest_fibonacci_number_index(4000000))
	end = 1000*time.time()
	print(f"Operation took {end - start:.2f}msec to complete")

	start = 1000*time.time()
	limit = 4000000
	print(f"The sum of even fibonacci numbers below {limit} is: {get_sum_by_brute_force_of_even_fibonacci_numbers_below(limit)}")
	# print(get_closest_fibonacci_number_index(4000000))
	end = 1000*time.time()
	print(f"Operation took {end - start:.2f}msec to complete")

	start = 1000*time.time()
	limit = 4000000
	print(f"The sum of even fibonacci numbers below {limit} is: {get_sum_by_brute_force_and_multiples_of_even_fibonacci_numbers_below(limit)}")
	# print(get_closest_fibonacci_number_index(4000000))
	end = 1000*time.time()
	print(f"Operation took {end - start:.2f}msec to complete")
