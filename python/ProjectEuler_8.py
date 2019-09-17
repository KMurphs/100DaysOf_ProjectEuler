# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

data = "\
73167176531330624919225119674426574742355349194934=\
96983520312774506326239578318016984801869478851843=\
85861560789112949495459501737958331952853208805511=\
12540698747158523863050715693290963295227443043557=\
66896648950445244523161731856403098711121722383113=\
62229893423380308135336276614282806444486645238749=\
30358907296290491560440772390713810515859307960866=\
70172427121883998797908792274921901699720888093776=\
65727333001053367881220235421809751254540594752243=\
52584907711670556013604839586446706324415722155397=\
53697817977846174064955149290862569321978468622482=\
83972241375657056057490261407972968652414535100474=\
82166370484403199890008895243450658541227588666881=\
16427171479924442928230863465674813919123162824586=\
17866458359124566529476545682848912883142607690042=\
24219022671055626321111109370544217506941658960408=\
07198403850962455444362981230987879927244284909188=\
84580156166097919133875499200524063689912560717606=\
05886116467109405077541002256983155200055935729725=\
71636269561882670428252483600823257530420752963450"


# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

processed_data = []

import math
import time
import random


def prepare_data(raw_data):


	proc_data = []
	temp_data = raw_data.split("=")
	for i in range(len(temp_data)):
		proc_data.append([int(elmt) for elmt in list(temp_data[i])])
	# print(proc_data)

	
	# return raw_data.split("=")
	return proc_data

def update_max(max_product, max_i, max_j, max_dir, curr_product, curr_i, curr_j, curr_dir):

	return (curr_product, curr_i, curr_j, curr_dir) if (curr_product > max_product) else (max_product, max_i, max_j, max_dir)

def get_product(i, j, N, dir):
	current_product = 1

	if(dir == 'horizontal'):
		if(j<N): return -1
		for k in range(N):
			current_product *= processed_data[i][j-k]

	elif(dir == 'vertical'):
		# print(f"Testing ({i-N},{j}) to ({i},{j})")
		if(i<N): return -1
		for k in range(N):
			current_product *= processed_data[i-k][j]

	elif(dir == 'down-right'):
		if(i<N): return -1
		if(j<N): return -1
		for k in range(N):
			current_product *= processed_data[i-k][j-k]

	elif(dir == 'up-left'):
		# print(f"Testing ({i+N},{j-N}) to ({i},{j})")
		if(i+N>len(processed_data)): return -1
		if(j<N): return -1
		for k in range(N):
			current_product *= processed_data[i+k][j-k]


	return current_product

def get_greatest_product_of_adjacents(N):

	
	max_product = 0
	max_i = 0
	max_j = 0
	max_dir = ''

	for i in range(len(processed_data)):
		for j in range(len(processed_data[i])):

			direction = 'horizontal'
			current_product = get_product(i, j, N, direction)
			max_product, max_i, max_j, max_dir = update_max(max_product, max_i, max_j, max_dir, current_product, i, j, direction)
			
			direction = 'vertical'
			current_product = get_product(i, j, N, direction)
			max_product, max_i, max_j, max_dir = update_max(max_product, max_i, max_j, max_dir, current_product, i, j, direction)

			direction = 'down-right'
			current_product = get_product(i, j, N, direction)
			max_product, max_i, max_j, max_dir = update_max(max_product, max_i, max_j, max_dir, current_product, i, j, direction)

			direction = 'up-left'
			current_product = get_product(i, j, N, direction)
			max_product, max_i, max_j, max_dir = update_max(max_product, max_i, max_j, max_dir, current_product, i, j, direction)


	return max_product, max_i, max_j, max_dir














def get_greatest_product_of_adjacents_optimized(N):

	
	max_product = 0
	max_i = 0
	max_j = 0
	max_dir = ''
	
	current_product = 0
	running_product = -1
	direction = ''
	update_indexes = False


	i = 0
	j = 0
	while True:
		direction = 'horizontal'
		current_product = 1
		if(i>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i
					j = j + (N-k)
					current_product = -1
					break
				else:
					current_product *= processed_data[i][j-k]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data)):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;		

	i = 0
	j = 0
	while True:
		direction = 'vertical'
		current_product = 1
		if(i>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i + (N-k)
					j = j
					current_product = -1
					break
				else:
					current_product *= processed_data[i-k][j]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data)):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;


	i = 0
	j = 0
	while True:
		direction = 'down-right'
		current_product = 1
		if(i>=N & j>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i + (N-k)
					j = j + (N-k)
					current_product = -1
					break
				else:
					current_product *= processed_data[i-k][j-k]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data)):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;

	i = 0
	j = 0
	while True:
		direction = 'up-left'
		current_product = 1
		if(i+N<=len(processed_data) & j>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i - (N-k)
					j = j + (N-k)
					current_product = -1
					break
				else:
					current_product *= processed_data[i+k][j-k]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data) | i < 0):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;



	return max_product, max_i, max_j, max_dir








def get_indexes(counter, direction):


	if(direction == 'horizontal'):
		temp_i = counter//data_row_length
		temp_j = counter%data_row_length
		# return (temp_i, temp_j, (counter-N)//data_row_length, (counter-N)%data_row_length, False) if(temp_j >= N) else (temp_i, N-1, temp_i, 0, True)
		return (temp_i, temp_j, temp_i, temp_j-N, False) if(temp_j >= N) else (temp_i, N-1, temp_i, 0, True)

	if(direction == 'vertical'):
		temp_i = counter//data_col_length
		temp_j = counter%data_col_length
		# return (temp_j, temp_i, (counter-N)%data_col_length, (counter-N)//data_col_length, False) if(temp_j >= N) else (N-1, temp_i, 0, temp_i, True)
		return (temp_j, temp_i, temp_j-N, temp_i, False) if(temp_j >= N) else (N-1, temp_i, 0, temp_i, True)

	if(direction == 'down-right'):
		temp_i = counter//data_row_length
		temp_j = counter%data_row_length
		if(temp_j>N):
			return (temp_i, temp_j, temp_i-N, temp_j-N, False) if(temp_i >= N) else (N-1, temp_j, 0, temp_j-N, True)
		else:
			return (temp_i, N-1, temp_i-N, 0, True) if(temp_i >= N) else (N-1, N-1, 0, 0, True)




def get_greatest_product_of_adjacents_optimized_v2(N):

	
	max_product = 0
	max_i = 0
	max_j = 0
	max_dir = ''
	

	counter = N - 1
	direction = 'horizontal'
	persistent_product = -1
	while counter < data_row_length * data_col_length:
		i, j, last_i, last_j, didJump = get_indexes(counter, direction)
		# print(f"Processing Data Element '{processed_data[i][j]}' at index '{i,j}' for counter value '{counter}'")
		# print(f"Processing Data Element '{processed_data[i][j]}' at index '{i,j}' (Old '{last_i, last_j, processed_data[last_i][last_j]}') for Counter value '{counter}' - Persistent product is {persistent_product} - Jump Occured: {didJump}")
		# print(f"Processing Data Element '{processed_data[i][j]}' at index '{i,j}' for Counter value '{counter}' - Persistent product is {persistent_product} - Jump Occured: {didJump}")

		if(processed_data[i][j] == 0):
			counter = counter + N
			persistent_product = -1
			continue
		if(didJump):
			counter = i*data_row_length+j
			# print(f"Counter Value: {counter}")
			persistent_product = -1
			# continue



		if(persistent_product == -1):
			current_product = 1
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					counter = counter + N-k	
					persistent_product = -1
					break			
				else:	
					current_product *= processed_data[i][j-k]
					if(k==N-1):
						persistent_product = current_product
						counter = counter + 1
						# print(f"persistent_product Value: {persistent_product}")
						# for k in range(N):
							# print(processed_data[i][j-k])

						if (persistent_product > max_product):
							max_product, max_i, max_j, max_dir = persistent_product, i, j, direction	

		else:
			persistent_product = persistent_product * processed_data[i][j] / processed_data[last_i][last_j]
			counter = counter + 1

			if (persistent_product > max_product):
				max_product, max_i, max_j, max_dir = persistent_product, i, j, direction	



	counter = N - 1
	direction = 'vertical'
	persistent_product = -1
	while counter < data_row_length * data_col_length:
		i, j, last_i, last_j, didJump = get_indexes(counter, direction)
		# print(f"Processing Data Element '{processed_data[i][j]}' at index '{i,j}' (Old '{last_i, last_j, processed_data[last_i][last_j]}') for Counter value '{counter}' - Persistent product is {persistent_product} - Jump Occured: {didJump}")
		# print(f"Processing Data Element '{processed_data[i][j]}' at index '{i,j}' for Counter value '{counter}' - Persistent product is {persistent_product} - Jump Occured: {didJump}")

		if(processed_data[i][j] == 0):
			counter = counter + N
			persistent_product = -1
			continue
		if(didJump):
			counter = j*data_col_length+i
			persistent_product = -1
			# continue

		if(persistent_product == -1):
			current_product = 1
			for k in range(N):
				if(processed_data[i-k][j] == 0):
					counter = counter + N-k	
					persistent_product = -1
					break			
				else:	
					current_product *= processed_data[i-k][j]
					if(k==N-1):
						persistent_product = current_product
						counter = counter + 1

						if (persistent_product > max_product):
							max_product, max_i, max_j, max_dir = persistent_product, i, j, direction	

		else:
			persistent_product = persistent_product * processed_data[i][j] / processed_data[last_i][last_j]
			counter = counter + 1

			if (persistent_product > max_product):
				max_product, max_i, max_j, max_dir = persistent_product, i, j, direction	



	i = 0
	j = 0
	while True:
		direction = 'down-right'
		current_product = 1
		if(i>=N & j>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i + (N-k)
					j = j + (N-k)
					current_product = -1
					break
				else:
					current_product *= processed_data[i-k][j-k]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data)):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;

	i = 0
	j = 0
	while True:
		direction = 'up-left'
		current_product = 1
		if(i+N<=len(processed_data) & j>=N): 
			for k in range(N):
				if(processed_data[i][j-k] == 0):
					i = i - (N-k)
					j = j + (N-k)
					current_product = -1
					break
				else:
					current_product *= processed_data[i+k][j-k]

			if (current_product > max_product):
				max_product, max_i, max_j, max_dir = current_product, i, j, direction

		if(i >= len(processed_data) | i < 0):
			break;
		j += 1
		if(j >= len(processed_data[i])):
			i += 1
			j = 0	
			if(i >= len(processed_data)):
				break;




	return max_product, max_i, max_j, max_dir











if __name__ == "__main__":
	processed_data = prepare_data(data) 
	data_row_length = len(processed_data[0])
	data_col_length = len(processed_data)

	N = 4

	start = time.time()
	print(get_greatest_product_of_adjacents(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_greatest_product_of_adjacents_optimized(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

	start = time.time()
	print(get_greatest_product_of_adjacents_optimized_v2(N))
	end = time.time()
	print(f"Operation took {1000*(end - start):.2f}ms")

