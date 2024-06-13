import numpy as np

### ESSAY 1 ###
# find max in k-size list sliding window
# Step 1 - find position of sliding window
# Step 2 - slice the list
# Step 3 - append into result list


def max_kernel(num_list, k):
    max_list = []
    for i in range(len(num_list) - k + 1):
        sub_list = num_list[i:i+k]
        max_list.append(max(sub_list))
    return max_list


### ESSAY 2 ###
# count number of each letter in word and return a dict


def count_letters(word):
    letters_dict = {}
    # identify letter and check if the letter exists in dict
    for letter in word:
        if letter not in letters_dict:
            # count the letter
            count = word.count(letter)
            # add letter:count into dict
            letters_dict[letter] = count
    # sort the dict by letter
    letters_dict = dict(sorted(letters_dict.items()))
    return letters_dict


### ESSAY 3 ###
# count number of each words in a text file and return a dict


def count_words(file_path):
    # read the file
    with open(file_path, 'r') as file:
        content = file.read()
    # create word list from file content
    words_list = content.split()
    # turn all word to lower case
    words_list = [word.lower() for word in words_list]

    words_dict = {}
    # identify word and check if the word exists in dict
    for word in words_list:
        if word not in words_dict:
            # count the word
            count = words_list.count(word)
            # add word:count into dict
            words_dict[word] = count
    # sort the dict by letter
    words_dict = dict(sorted(words_dict.items()))
    return words_dict


file_path = 'assets\m01ex02_P1_data.txt'


### ESSAY 4 ###
# Function to calculate Levenshtein distance


def levenshtein_distance(source, target):
    # 1 create the matrix
    n_row = len(source) + 1
    m_column = len(target) + 1
    l_matrix = np.zeros((n_row, m_column))

    # 2 fill the 1st row
    l_matrix[0, :] = range(m_column)
    # 2 fill the 1st column
    l_matrix[:, 0] = range(n_row)

    # calculate associated cost
    def del_cost():
        return 1

    def ins_cost():
        return 1

    def sub_cost(source, target):
        return 0 if source == target else 1

    # 3 fill the remaining cells
    for i in range(1, n_row):
        for j in range(1, m_column):
            del_ = l_matrix[i-1, j] + del_cost()
            ins_ = l_matrix[i, j-1] + ins_cost()
            sub_ = l_matrix[i-1, j-1] + sub_cost(source[i-1], target[j-1])

            l_matrix[i, j] = min(del_, ins_, sub_)

    return l_matrix[n_row-1, m_column-1]


### MULTIPLE CHOICE QUESTION ###
# MC1
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(f"MC1: {max_kernel(num_list, k)} - Answer: a)")

# MC2
print(f"MC2: {count_letters('smiles')} - Answer: a)")

# MC3
result = count_words(file_path)
print(f"MC3: {result['man']} - Answer: c)")

# MC4
print(f"MC4: {levenshtein_distance('hola', 'hello')} - Answer: c)")


def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results


# MC5
n = 2
results = check_the_number(n)
print(f"MC5: {results} - Answer: a)")


def clamp_list(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


# MC6
my_list = [10, 2, 5, 0, 1]
max_value = 2
min_value = 1
print(f"MC6: {clamp_list(my_list, max_value, min_value)} - Answer: c)")


def extend_list(x, y):
    return x + y


# MC7
list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(f'''MC7: {extend_list(list_num1, extend_list(
    list_num2, list_num3))} - Answer: a)''')


def find_min(n):
    return min(n)


# MC8
my_list2 = [1, 2, 3, -1]
print(f"MC8: {find_min(my_list2)} - Answer: c)")


def find_max(n):
    return max(n)


# MC9
my_list2 = [1, 9, 9, 0]
print(f"MC9: {find_max(my_list2)} - Answer: d)")


def is_num_in_list(integers, number):
    return any([True if num == number else False for num in integers])


# MC10
my_list3 = [1, 2, 3, 4]
print(f"MC10: {is_num_in_list(my_list3, 2)} - Answer: c)")


def find_mean(num_list):
    total = 0
    for num in num_list:
        total += num
    mean = total / len(num_list)
    return mean


# MC11
num_list = [0, 1, 2]
print(f"MC11: {find_mean(num_list)} - Answer: a)")


def is_divisible_by_three(num_list):
    divisible_list = []
    for num in num_list:
        if num % 3 == 0:
            divisible_list.append(num)
    return divisible_list


# MC12
num_list2 = [1, 2, 3, 5, 6]
print(f"MC12: {is_divisible_by_three(num_list2)} - Answer: a)")


def find_factorial(number):
    factorial = 1
    while (number > 1):
        factorial *= number
        number -= 1
    return factorial


# MC13
num = 4
print(f"MC13: {find_factorial(num)} - Answer: c)")


def reverse_string(text):
    return text[::-1]


# MC14
text = "apricot"
print(f"MC14: {reverse_string(text)} - Answer: b)")


def is_greater_than_zero(num):
    return "Y" if num > 0 else "N"


def check_positive(num_list):
    is_positive = [is_greater_than_zero(num) for num in num_list]
    return is_positive


# MC15
num_list3 = [2, 3, 5, -1]
print(f"MC15: {check_positive(num_list3)} - Answer: c)")
