# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



import math
import time
import random

def extract_primes_by_trial_division(N):

	primes = []
	exponents = []
	N_temp = int(N)
	# print(f"\n")

	for i in range(2, int(math.sqrt(N)) + 1):

		counter = 0
		while(N_temp%i==0):
			N_temp //= i
			counter += 1
		# print(f"Tested {N} for division by {i}. Got: {counter} as exponent")

		if(counter > 0):
			if(i not in primes):
				primes.append(i)
				exponents.append(counter)
			else:
				index = primes.index(i)
				exponents[index] = counter

	if(len(primes) == 0):
		primes.append(N)
		exponents.append(1)	
	elif(N_temp != 1):
		primes.append(N_temp)
		exponents.append(1)	

	# print(f"Primes and Exponents for {N} are: {primes, exponents}")
	return primes, exponents

def extract_primes_by_sieve(N):

	primes = []
	exponents = []
	sieve = [True] * N
	N_temp = int(N)
	# print(f"\n")

	for i in range(1, N):
		if(sieve[i]):
			prime = i + 1
			
			for j in range((prime*prime)-1, N, prime):
				sieve[j] = False

			counter = 0
			while(N_temp%prime==0):
				N_temp //= prime
				counter += 1


			if(counter > 0):
				if(prime not in primes):
					primes.append(prime)
					exponents.append(counter)
				else:
					index = primes.index(prime)
					exponents[index] = counter

			# print(f"Current Sieve: {sieve}")
			# print(f"Tested {N} for division by {prime}. Got: {counter} as exponent")


	# print(f"Primes and Exponents for {N} are: {primes, exponents}")
	return primes, exponents



def get_smallest_divisible_by_all_below(N, useSieve=False):
	scm = 1 
	primes = []
	exponents = []


	for i in range(2, N + 1):
		if not useSieve:
			temp_primes, temp_exponents = extract_primes_by_trial_division(N + 2 - i)
		else:
			temp_primes, temp_exponents = extract_primes_by_sieve(N + 2 - i)


		for counter in range(len(temp_primes)):

			current_prime = temp_primes[counter]
			current_expon = temp_exponents[counter]

			if(current_prime not in primes):
				scm *= math.pow(current_prime, current_expon)
				primes.append(current_prime)
				exponents.append(current_expon)
				

			elif(current_expon > exponents[primes.index(current_prime)]):
				scm *= math.pow(current_prime, (current_expon - exponents[primes.index(current_prime)]))
				exponents[primes.index(current_prime)] = current_expon
				

			# print(f"scm was updated to {scm}")


	return scm






if __name__ == "__main__": 
	N = 200

	start = time.time()
	print(get_smallest_divisible_by_all_below(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_smallest_divisible_by_all_below(N, True))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")
