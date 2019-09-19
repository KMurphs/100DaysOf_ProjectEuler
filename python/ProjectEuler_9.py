

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math
import time
import random


def get_pythagorian_triplets_with_sum(N):

    # a < b < c
	a = 1
	b = 1
	c = 1
    
	for c in  range(int(N/3-1), int(N/2+1)):
		for b in range(int(N/3-1), c):
			for a in range(1, b):
				if((a*a)+(b*b)==(c*c)):
					# print(f"Found Pythagorian triplets: {a,b,c} with sum {a+b+c} (c square is {c*c})")
					if(a+b+c==N):
						print(f"	Found Solution for triplets: {a,b,c} with sum {a+b+c} (c square is {c*c})")
						return a,b,c,a*b*c,a+b+c,a*a+b*b,c*c


	return "[No Data]"


# One useful way to look at this is to note that a,b,c form a triangle because of the constant perimeter (a+b+c).
# see a string of fixed length that is extended by 3 fingers, each side being either a,b, or c
def get_pythagorian_triplets_with_sum_v2(N):

    # a < b < c
	a = 1
	b = 1
	c = 1
    
	for c in  range(int(N/3-1), int(N/2+1)):
		for b in range(int(N/3-1), c):
			a = N - b - c
			if((a*a)+(b*b)==(c*c)):
				print(f"	Found Solution for triplets: {a,b,c} with sum {a+b+c} (c square is {c*c})")
				return a,b,c,a*b*c,a+b+c,a*a+b*b,c*c

	return "[No Data]"

def get_pythagorian_triplets_with_sum_v3(N):

    # a < b < c
	a = 1
	b = 1
	c = 1
	# using N=a+b+c, and c^2=a^2+b^2, with tan(alpha) = b/a, cos(alpha) = a/c, tan(alpha/2) = t
	# t = 1 - 2a/N, b = a*2t/(1-t^2), c = a (1+t^2)/(1-t^2)
	# a = int(N/3+1) + 1
	a = 1
	for _ in range(int(N/3+1)):
		
		# a -= 1
		a += 1

		# t = 1 - 2*a/N
		# t_sqr = (1 - 2*a/N)*(1 - 2*a/N)
		# b = a*2*t/(1-t_sqr)
		# c = a*(1+t_sqr)/(1-t_sqr)

		# When getting a final developped expression for b anc c, we get the expression below for b and c

		b = (N*N-2*a*N)/(2*N-2*a)
		if(a>b): continue

		c = ((N*N)-(2*a*N)+(2*a*a))/(2*N-2*a)
		# c = math.pow(a*a+b*b, 0.5)
		if(b>c): continue

		# if((int(a)+int(b)+int(c)==int(N)) & (a<b) & (b<c)):
		if((a+int(b)+int(c)==N)):
		# if(int(a+b+c)==N):
			# print(f"	Found Solution for triplets: {a,b,c} with sum {a+b+c} (c square is {c*c})")
			return a,b,c,a*b*c,a+b+c,a*a+b*b,c*c
		

	return "[No Data]"






def gcd(a, b):
	y = 0;
	x = 0;
 
	if (a > b):
		x = a
		y = b
	else:
		x = b
		y = a
	
	while (x % y != 0): 
		temp = x
		x = y
		y = temp % x

	return y


# https://www.mathblog.dk/pythagorean-triplets/
def get_pythagorian_triplets_with_sum_by_number_theory(N):

	a=0
	b=0
	c=0
	s = N

	m = 0
	k = 0
	n = 0
	d = 0

	found = False

	mlimit = int(math.sqrt(s / 2))
	for m in range(2, mlimit + 1):
		if ((s // 2) % m == 0): # m found
			if (m % 2 == 0): #  ensure that we find an odd number for k
				k = m + 1
			else:
				k = m + 2;

			while ((k < (2 * m)) & (k <= (s / (2 * m)))):
				if (((s / (2 * m)) % k == 0) & (gcd(k, m) == 1)):
					d = s / (2 * (k * m))
					n = k - m
					a = d*(m * m - n * n)
					b = 2 * d * n * m
					c = d * (m * m + n * n)
					found = True
					break

				k += 2

		if found:
			return a,b,c,a*b*c,a+b+c,a*a+b*b,c*c
			# break;
			

	return "[No Data]"





if __name__ == "__main__":
	N = 100000000

	# start = time.time()
	# print(get_pythagorian_triplets_with_sum(N))
	# end = time.time()
	# print(f"Operation took {1000*(end - start):.2f}ms")

	# start = time.time()
	# print(get_pythagorian_triplets_with_sum_v2(N))
	# end = time.time()
	# print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_pythagorian_triplets_with_sum_v3(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_pythagorian_triplets_with_sum_by_number_theory(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")


