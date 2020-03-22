def anagrams():
	words = input().lower().split()
	first_word = list(words[0])
	second_word = list(words[1])

	compare = first_word.sort() == second_word.sort()

	if compare == True:
		return "ANAGRAMS"
	else:
		return "NOT ANAGRAMS"

print(anagrams())




def credit_card_validation(number):
	lst =  list(map(int, str(number)))
	lst = ''.join([str(lst[i] *  2) if i % 2 != 0 else str(lst[i]) for i in range(len(lst))])
	lst = list(map(int, lst))
	res = sum(lst)

	if (res / 10).is_integer():
		return True
	else:
		return False	

print(credit_card_validation(79927398713))
print(credit_card_validation(79927398715))




#Helper function for goldbach()
def is_prime(prime):
	if prime == 2 or prime == 3 or prime == 5 or prime == 7:
		return True
	if not (prime / 2).is_integer() and not (prime / 3).is_integer() and not (prime / 5).is_integer()  and  not (prime / 7).is_integer() :
		return True
	return False	

def goldbach(number):
	compliments = []
	result = []
	for i in range(2, number):
		if is_prime(i) and number - i not in compliments:
			compliments.append(number - i)

		if is_prime(i) and i in compliments:
			result.insert(0, (number - i, i))	

	return result

print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))



def matrix_bombing_plan():
	size = input("Enter matrix size (N M): ").split()
	n = int(size[0])
	m = int(size[1])

	print("Enter matrix: ")
	matrix = init_matrix(n, m)


	matrix_value = get_matrix_value(matrix, n, m)
	res_dict = {}

	for row in range(n):
		for col in range(m):
			bombed_value = matrix_value
			current_position = matrix[row][col]
			start_row = row - 1
			start_col = col - 1
			end_row = row + 1 
			end_col = col + 1

			for bomb_row in range(start_row, end_row + 1):
				for bomb_col in range(start_col, end_col + 1):
					if not check_if_index_is_in_range(n, m, bomb_row, bomb_col):
						continue
					if bomb_row == row and bomb_col == col:
						continue

					bombed_position =  matrix[bomb_row][bomb_col]
					decrease_by = calculate_decrease_by(current_position, bombed_position)
					bombed_value -= decrease_by

			res_dict[(row, col)] = bombed_value


	return res_dict

def init_matrix(n, m):
	matrix = []
	for row in range(n):
		current_row = input().strip().split()
		if len(current_row) > m:
			raise TypeError('Wrong input')
		matrix.append(current_row)
	return matrix	



def calculate_decrease_by(current_position, bombed_position):
	decrease_by = 0	
	if current_position > bombed_position:
		decrease_by = bombed_position
	else:
		decrease_by = current_position
	return decrease_by	


def get_matrix_value(matrix, n, m):
	total = 0
	for row in range(n):
		for col in range(m):
			matrix[row][col] = int(matrix[row][col])
			total += matrix[row][col]
	return total

def check_if_index_is_in_range(n, m, row, col):
	if n - 1 < row or m - 1 < col or row < 0 or col < 0:
		return False
	return True	 

def check_if_cell_has_negative_value(matrix, row, col):
	if matrix[row][col] < 0:
		return 0
	return matrix[row][col]

print(matrix_bombing_plan())