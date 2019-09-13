# A palindromic number reads the same both ways. The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import math
import time
import random


def split_number(N):

	up = 0
	low = 0
	isEven = False
	
	N_temp = abs(N)
	digits = 0

	while(N_temp > 0):
		N_temp = N_temp // 10
		digits = digits + 1

	# print(f"Number {N} has {digits} digits")

	if(digits % 2 == 0):
		low = N % math.pow(10, digits//2)
		up = N // math.pow(10, digits//2)
		union_help = math.pow(10, digits//2)
		isEven = True
	else:
		low = N % math.pow(10, 1 + int(digits//2))
		up = N // math.pow(10, int(digits//2))	
		union_help = math.pow(10, digits//2)
		isEven = False

	# print(f"Number token are: {int(up), int(low), int(union_help)}")	

	return int(up), int(low), int(union_help), isEven


def get_next_palindrome(up, low): 
	up_rev = int(str(up)[::-1])
	# print(f"Next Palyndrome is: {(up, up_rev) if up_rev <= low else (up - 1, int(str(up - 1)[::-1]))}")
	return (up, up_rev) if up_rev <= low else (up - 1, int(str(up - 1)[::-1]))


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


def get_largest_palindrome_from_product(digits):
	N_max = int(math.pow(math.pow(10, digits) - 1, 2)) # Largest Product
	N_min = int(math.pow(10, digits + 1)) # Lowest Product
	print(f"Limits for potential palindroms are {N_min} and {N_max}")

	up, low, union_help, isEven = split_number(N_max)

	factors_low_limit = math.pow(10, digits - 1)
	factors_high_limit = math.pow(10, digits) - 1

	isValid = False
	N_new = N_min

	while(not isValid and N_new >= N_min):
		# print(f"\n\n")

		up, low = get_next_palindrome(up, low-1)

		N_new = int((up if isEven else up // 10) * union_help) + low
		# print(f"New Number is: {N_new} from {up} and {low} using union helper {union_help} and eveness {isEven}")

		isPrime, c, d = fermat_factorization(N_new)
		# print(f"New Number is{' ' if isPrime else ' not '}prime. Factors {c} and {d}")

		isValid = (c >= factors_low_limit) & (c <= factors_high_limit) & (d >= factors_low_limit) & (d <= factors_high_limit)
		# print(f"Current Factors {c} and {d} are{' ' if isValid else ' not '}valid.")


	return N_new, c, d






if __name__ == "__main__": 
	start = time.time()
	print(get_largest_palindrome_from_product(5))
	#print(fermat_factorization(9009))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

