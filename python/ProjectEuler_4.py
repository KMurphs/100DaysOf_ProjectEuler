# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import math
import time
import random


def split_number(N):

	# up = 0
	# low = 0
	N_temp = abs(N)
	# digits = 0

	# while(N_temp > 0):
	# 	N_temp = N_temp // 10
	# 	digits = digits + 1

	digits = len(str(N_temp))
	splitter = math.pow(10, int(digits//2))

	# print(f"Number {N} has {digits} digits")

	if(digits % 2 == 0):
		low = N % splitter
		up = N // splitter
		isEven = True
	else:
		low = N % (splitter*10)
		up = N // splitter
		isEven = False

	# print(f"Number token are: {int(up), int(low), int(union_help)}")	

	return int(up), int(low), int(splitter), isEven


def get_next_palindrome(up, low): 
	up_rev = int(str(up)[::-1])
	# print(f"Next Palyndrome is: {(up, up_rev) if up_rev <= low else (up - 1, int(str(up - 1)[::-1]))}")
	return (up, up_rev) if up_rev <= low else (up - 1, int(str(up - 1)[::-1]))

def get_next_palindrome_without_check(up, low): 
	# print(f"Next Palyndrome is: {(up, up_rev) if up_rev <= low else (up - 1, int(str(up - 1)[::-1]))}")
	return (up - 1, int(str(up - 1)[::-1]))


def fermat_factorization(N):
	N_sqrt = math.sqrt(N)
	a = int(N_sqrt + 1)
	b = math.sqrt(a*a - N)

	# print(f"N is: {N}, a and asquare: {a, a*a}, b and bsquare is {b, b*b}")
	while(b != int(b) and b < N_sqrt):
		a += 1
		b = math.sqrt(a*a - N)
		# print(f"N is: {N}, a and asquare: {a, a*a}, b and bsquare is {b, b*b}")

	if(b < N_sqrt):
		c = int(a+b)
		d = int(a-b)
	else:
		c = N
		d = 1		

	return c == N, c, d

def trial_factorization(N):
	N_sqrt = math.sqrt(N)
	a = int(N_sqrt + 1)
	b = math.sqrt(a*a - N)

	# print(f"N is: {N}, a and asquare: {a, a*a}, b and bsquare is {b, b*b}")
	while(N % a != 0):
		a -= 1
		# print(f"N is: {N}, a and asquare: {a, a*a}, b and bsquare is {b, b*b}")	

	return a == 1, int(N/a), a


def get_largest_palindrome_from_product(digits, useFermatFactorization=True):
	# N_max = int(math.pow(math.pow(10, digits) - 1, 2)) # Largest Product
	N_max = int(math.pow(10, 2*digits) - 1) # Largest Palindrom
	N_min = int(math.pow(10, digits + 1)) # Lowest Product
	print(f"Limits for potential palindroms are {N_min} and {N_max}")

	up, low, union_help, isEven = split_number(N_max)

	factors_low_limit = math.pow(10, digits - 1)
	factors_high_limit = math.pow(10, digits) - 1

	isValid = False
	N_new = N_min

	while(not isValid and N_new >= N_min):
		# print(f"\n\n")

		# up, low = get_next_palindrome(up, low-1)
		up, low = get_next_palindrome_without_check(up, low-1)

		N_new = int((up if isEven else up // 10) * union_help) + low
		# print(f"New Number is: {N_new} from {up} and {low} using union helper {union_help} and eveness {isEven}")

		if(useFermatFactorization):
			isPrime, c, d = fermat_factorization(N_new)
		else:
			isPrime, c, d = trial_factorization(N_new)
		# print(f"New Number is{' ' if isPrime else ' not '}prime. Factors {c} and {d}")

		isValid = (c >= factors_low_limit) & (c <= factors_high_limit) & (d >= factors_low_limit) & (d <= factors_high_limit)
		# print(f"Current Factors {c} and {d} are{' ' if isValid else ' not '}valid.")


	return N_new, c, d





def isPalyndrom(a, b=None): 
	up, low, _, _ = split_number(a*b if b is not None else a[0]*a[1])
	return low == int(str(up)[::-1])

def get_largest_palindrome_from_product_by_brute_force(digits):
	# N_max = int(math.pow(math.pow(10, digits) - 1, 2)) # Largest Product
	N_max = int(math.pow(10, 2*digits) - 1) # Largest Palindrom
	N_min = int(math.pow(10, digits + 1)) # Lowest Product
	print(f"Limits for potential palindroms are {N_min} and {N_max}")

	up, low, union_help, isEven = split_number(N_max)

	factors_low_limit = int(math.pow(10, digits - 1))
	factors_high_limit = int(math.pow(10, digits) - 1)
	# print(f"Limits for potential factors are {factors_low_limit} and {factors_high_limit}")

	palindroms = []


	for counter in range(0, int(2 * factors_high_limit)):
		for potential_c in range(int(counter / -2), 1):
			potential_c_translated = int(potential_c + factors_high_limit)
			potential_d_translated = int((-1*potential_c_translated) + (2*factors_high_limit) - counter)
			# print(f"Counter, potential_c, potential_c_translated, potential_d_translated: {counter, potential_c, potential_c_translated, potential_d_translated}")

			if(potential_c_translated <= factors_low_limit | potential_d_translated <= factors_low_limit):
				continue


			# print(f"Checking palindromness for factors {potential_c_translated, potential_d_translated} giving product {potential_c_translated * potential_d_translated}")
			if(isPalyndrom(potential_c_translated, potential_d_translated)):
				# print(f"Found palindrom {potential_c*potential_d} from {potential_c, potential_d} splitted in {split_number(potential_c*potential_d)}")
				return potential_c_translated*potential_d_translated, potential_c_translated, potential_d_translated




	return "OOps! Something unexpected happened... Can't compute the largest palindrom by brute force for some obscure reason"



if __name__ == "__main__": 
	digits = 5

	start = time.time()
	print(get_largest_palindrome_from_product(digits))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_largest_palindrome_from_product(digits, False))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_largest_palindrome_from_product_by_brute_force(digits))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

