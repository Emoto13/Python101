import math

def sum_of_digits(num):
	num = abs(num)
	list_nums =  [int(char) for char in str(num)] 
	res = sum(list_nums)
	return res	

print(sum_of_digits(123))




def to_digits1(num):
	lst = [int(i) for i in str(num)]
	return lst

print(to_digits1(123))




def to_digits2(num):
	return list(map(int, list(str(num))))

print(to_digits2(123))




def to_number(lst):
	castedList =[str(i) for i in lst] 
	res = int("".join(castedList))
	return res

print(to_number([1,2,3]))




def fact_digits(num):
	lst = [int(i) for i in str(num)]
	res = 0
	for element in lst:
		res += math.factorial(element)

	return res	

print(fact_digits(145))




def palindrome(object):
	reverseInput = "".join(reversed(object))
	return str(object) == reverseInput

print(palindrome("kapak"))
print(palindrome("kapa"))




def count_vowels(string):
	vowels = 'aeiouy'
	res = 0

	for s in string.lower():
		if s in vowels:
			res += 1

	return res

print(count_vowels('Python'))		




def count_consonants(string):
	consonants = 'bcdfghjklmnpqrstvwxz'
	res = 0

	for s in string.lower():
		if s in consonants:
			res += 1

	return res

print(count_consonants('Python'))




def char_histogram(string):
	map = {}

	for s in string:
		map[s] = string.count(s)

	return map

print(char_histogram('Python!'))




def sum_matrix(m):
	flatten = [item for sublist in m for item in sublist]
	return (sum(flatten))	

print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))




def nan_expand(n):
	list = []
	for i in range(0, n):
		list.append("Not a ")
	list.append("NaN")
	return "".join(list)

print(nan_expand(2))




def prime_factorization(n):
	current_prime = 2
	power = 0
	result_list = []
	if n == 1:
		return [(1,1)]


	while True:
		res = n / current_prime

		if res.is_integer():
			power += 1
			n = int(res)
		else: 
			if power > 0:
				result_list.append((current_prime, power))
			power = 0	
			current_prime = find_next_prime(current_prime)

		if (n == 1):
			result_list.append((current_prime, power))
			break	
	

	return result_list

#Helper function for prime_factorization()
def find_next_prime(prime):
	while True:
		prime += 1
		if prime == 3 or prime == 5 or prime == 7:
			return prime
		if prime % 2 != 0 and prime % 3 != 0 and prime % 5 != 0 and prime % 7 != 0:
			return prime


print(prime_factorization(10))	
print(prime_factorization(14))	
print(prime_factorization(356))	
print(prime_factorization(89))
print(prime_factorization(1000))	
print(prime_factorization(39))
print(prime_factorization(1))	



def group(lst):
	n = len(lst)
	new_list = [lst[0]]
	res_list = []

	for i in range(1, n):
		if lst[i] != lst[i - 1]:	
			res_list.append(new_list.copy())
			new_list.clear()

		new_list.append(lst[i])	

	if new_list:
		res_list.append(new_list)	
		
	return res_list

print(group([1, 1, 1, 2, 3, 1, 1]))




def max_consecutive(list):
	n = len(list)
	max = 0
	current_max = 1;
	for i in range(1, n):
		if list[i] == list[i - 1]:
			current_max += 1
		else:
			if current_max > max:
				max = current_max
			current_max = 1

	if current_max > max:
		max = current_max 

	return max

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))



def is_palindrome(word):
    return word == word[::-1]


def contains_word(word, text):
    if is_palindrome(word):
        return text.count(word)

    return text.count(word) + text[::-1].count(word)


def build_matrix(rows, cols):
    matrix = []
    rows_inputted = 0
    print('Enter matrix: ')

    while rows_inputted < rows:
        row_input = input()

        row = row_input.strip().split(' ')
        if len(row) != cols:
            return 'Wrong input.'

        matrix.append(row)
        rows_inputted += 1

    return matrix


def word_occurances_in_rows(matrix, word):
    word_occurances = 0

    for row in matrix:
        word_occurances += contains_word(word, ''.join(row))

    return word_occurances


def word_occurances_in_cols(matrix, word):
    word_occurances = 0
    cols_count = len(matrix[0])

    for i in range(cols_count):
        column = []
        for row in matrix:
            column.append(row[i])

        word_occurances += contains_word(word, ''.join(column))

    return word_occurances


def word_occurances_in_right_diagonals(matrix, word):
    word_occurances = 0
    rows_count = len(matrix)
    cols_count = len(matrix[0])

    for c in range(rows_count + cols_count - 1):
        diagonal = []
        for i in range(rows_count):
            for j in range(cols_count):
                if i + j == c:
                    diagonal.append(matrix[i][j])

        word_occurances += contains_word(word, ''.join(diagonal))

    return word_occurances


def word_occurances_in_left_diagonals(matrix, word):
    word_occurances = 0
    rows_count = len(matrix)
    cols_count = len(matrix[0])

    for c in range(1 - cols_count, rows_count):
        diagonal = []
        for i in range(rows_count):
            for j in reversed(range(cols_count)):
                if j - i == c:
                    diagonal.append(matrix[i][j])

        word_occurances += contains_word(word, ''.join(diagonal))

    return word_occurances


def word_counter():
    word = input('Enter word: ')
    size = input('Enter matrix size (format: N M): ')

    n = int(size.split(' ')[0])
    m = int(size.split(' ')[1])

    if len(word) > min([n, m]):
        return 'Invalid number of rows or columns!'

    matrix = build_matrix(n, m)

    word_occurances = word_occurances_in_rows(matrix, word)
    word_occurances += word_occurances_in_cols(matrix, word)
    word_occurances += word_occurances_in_right_diagonals(matrix, word)
    word_occurances += word_occurances_in_left_diagonals(matrix, word)

    return word_occurances


print(word_counter())