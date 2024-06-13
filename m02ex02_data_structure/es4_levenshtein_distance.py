import numpy as np
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

# MC4
print(f"MC4: {levenshtein_distance('hola', 'hello')} - Answer: c)")