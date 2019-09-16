# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.




import math
import time
import random

# see using-generating-functions-find-the-sum-of-progressing-exponents.pdf
def get_sum_of_squared_progression(N):

	return (N*(N+1)/2) * ((2*N+1)/3)

def get_sum_of_progression(N):

	return (N*(N+1)/2)


def get_difference_between_sumofsquare_and_squareofsum(N):

	return math.pow(get_sum_of_progression(N), 2) - get_sum_of_squared_progression(N)






if __name__ == "__main__": 
	N = 1000

	start = time.time()
	print(get_difference_between_sumofsquare_and_squareofsum(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

