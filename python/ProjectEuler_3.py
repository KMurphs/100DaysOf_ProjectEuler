# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
import time
import random

def extract_composite(N, prime): 
	N_temp = N
	while(N_temp%prime==0):
		N_temp //= prime

	# print(f"Extracted composite: {prime} from {N_temp}: {N_temp != N}")
	return N_temp, N_temp != N

def get_largest_prime_factor(N):
	N_temp = N
	largest_prime = 1

	for i in [2, 3, 5]:
		N_temp, found = extract_composite(N_temp, i)
		if(found): 
			largest_prime = i

	for i in range(7, int(math.sqrt(N) + 1), 6):
		N_temp, found = extract_composite(N_temp, i)
		if(found): 
			largest_prime = i		

	if(N_temp != 1):
		largest_prime = N_temp	

	return largest_prime

def get_largest_prime_factor_using_odd_numbers(N):
	N_temp = N
	largest_prime = 1

	for i in [2]:
		N_temp, found = extract_composite(N_temp, i)
		if(found): 
			largest_prime = i

	for i in range(3, int(math.sqrt(N) + 1), 2):
		N_temp, found = extract_composite(N_temp, i)
		if(found): 
			largest_prime = i		

	if(N_temp != 1):
		largest_prime = N_temp	

	return largest_prime


def primality_test_using_fermat_theorem(potential_prime, iterations = 10, random_max_bound = 1000): 
	isPrime = False

	# if p is prime then => a ^ (p-1) mod p = 1
	# we repeat the test (iterations) times to eliminate pseudo prime numbers
	# these pseudo prime numbers can be generated for a given a with a probability of at worse 1/2
	# if after (iterations) trials we still find that the potential_prime stands the test, the 
	# probability of it being a pseudo prime fall at (1 / 2 ^ iterations)
	# one must fix iterations to give the acceptable error probability
	for _ in range(iterations):
		random_number_mod = 0
		while(random_number_mod == 0):
			random_number = random.randint(1, random_max_bound) # Generate random number
			random_number_mod = random_number % potential_prime # Get random number mod result
		# print(f"Random Number {random_number} mod {potential_prime} is: {random_number_mod}")

		# use random number mod result to perform fermat's test
		# multiplication is performed in step to reduce the result by using (result mod prime)
		temp = 1
		for _ in range(potential_prime - 1):
			temp = (temp * random_number_mod) % potential_prime
		isPrime = (temp % potential_prime == 1) 

		if not isPrime:
			break
	
	return isPrime


def get_largest_prime_factor_using_odd_numbers_and_fermat(N):
	largest_prime = 1

	for i in [2, 3, 5]:
		if(primality_test_using_fermat_theorem(i)): 
			largest_prime = i

	for i in range(7, int(math.sqrt(N) + 1), 6):
		if(primality_test_using_fermat_theorem(i)): 
			largest_prime = i

	if(largest_prime == 1):
		largest_prime = N	

	return largest_prime


if __name__ == "__main__": 
	start = time.time()
	print(get_largest_prime_factor(600851475143))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_largest_prime_factor_using_odd_numbers(600851475143))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print("This is impractical for use with fermat's little theorem")
	print(get_largest_prime_factor_using_odd_numbers_and_fermat(600851475143))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")