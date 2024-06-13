import math
import random

### ESSAY 1 ###
# F1-Score function to assess Classification Model


def f1_score(tp, fp, fn):
    # input validation
    input_check = [tp, fp, fn]
    for value in input_check:
        if type(value) is not int:
            print(f"{value} must be int")
            break
        if value <= 0:
            print("tp and fp and fn must be greater than zero")
            break
    # calculate precision
    precision = tp / (tp + fp)
    # calculate recall
    recall = tp / (tp + fn)
    # calculate F1-Score
    f1_score = 2 * (precision * recall / (precision + recall))
    # print result
    print(f"precision is {precision}\nrecall is {
          recall}\nf1-score is {f1_score}")
    return f1_score

# f1_score(tp=2, fp=3, fn=5)

### ESSAY 2 ###
# Function to check validation of x in activation function


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# print(is_number(1))
# print(is_number('n'))

# Activation Function (Sigmoid, ReLU, ELU)


def activation_function():
    # get input
    x = input("Input x: ")
    function_name = input("Input Activation Function (sigmoid | relu | elu): ")

    if is_number(x) == True:
        x = float(x)
        # function name validation
        supported_functions = ["sigmoid", "relu", "elu"]

        if function_name not in supported_functions:
            print(f"{function_name} is not supported")
        else:
            if function_name.lower() == "sigmoid":
                result = 1 / (1 + math.e**-x)

            if function_name.lower() == "relu":
                if x <= 0:
                    result = 0
                else:
                    result = x

            if function_name.lower() == "elu":
                if x <= 0:
                    result = 0.01*(math.e**x - 1)
                else:
                    result = x

            print(f"{function_name.lower()}: f({x}) = {result}")
            return result
    else:
        print("x must be a nunber")

# activation_function()

### ESSAY 3 ###
# Choose regression loss function to calculate loss


def regression_loss():
    # get input from users
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    loss_name = input("Input loss name (MAE | MSE | RMSE): ").lower()

    # validate num_samples
    if num_samples.isnumeric() == True:
        num_samples = int(num_samples)
        # choose loss function
        supported_functions = ["mae", "mse", "rmse"]
        if loss_name in supported_functions:

            # calculate MAE loss
            if loss_name == "mae":
                accumuated_loss = 0
                for i in range(num_samples):
                    predict = random.uniform(0, 10)
                    target = random.uniform(0, 10)
                    loss = abs(target - predict)
                    accumuated_loss += loss
                    print(f"loss name: {loss_name}\nsample: {i}\npred: {
                          predict}\ntarget: {target}\nloss: {loss}\n")
                final_loss = accumuated_loss / num_samples
                print(f"final {loss_name.upper()}: {final_loss}")

            # calculate MSE loss
            if loss_name == "mse":
                accumuated_loss = 0
                for i in range(num_samples):
                    predict = random.uniform(0, 10)
                    target = random.uniform(0, 10)
                    loss = (target - predict)**2
                    accumuated_loss += loss
                    print(f"loss name: {loss_name}\nsample: {i}\npred: {
                          predict}\ntarget: {target}\nloss: {loss}\n")
                final_loss = accumuated_loss / num_samples
                print(f"final {loss_name.upper()}: {final_loss}")

            # calculate RMSE loss
            if loss_name == "rmse":
                accumuated_loss = 0
                for i in range(num_samples):
                    predict = random.uniform(0, 10)
                    target = random.uniform(0, 10)
                    loss = math.sqrt((target - predict)**2)
                    accumuated_loss += loss**2
                    print(f"loss name: {loss_name}\nsample: {i}\npred: {
                          predict}\ntarget: {target}\nloss: {loss}\n")
                final_loss = math.sqrt(accumuated_loss / num_samples)
                print(f"final {loss_name.upper()}: {final_loss}")

            return final_loss
        else:
            print(f"{loss_name} function is not supported")
    else:
        print("Number of samples must be an integer number")

# regression_loss()

### ESSAY 4 ###
# Trigonometry and Hyperbolic Functions
# Sin Function


def sin(x, n):
    final_sin = 0
    for i in range(0, n):
        sin = (-1)**i * (x**(2 * i + 1) / math.factorial(2 * i + 1))
        # print(f"{i}: {sin}")
        final_sin += sin
    return final_sin
# Cos Function


def cos(x, n):
    final_cos = 0
    for i in range(0, n):
        cos = (-1)**i * (x**(2 * i) / math.factorial(2 * i))
        final_cos += cos
    return final_cos
# Sinh Function


def sinh(x, n):
    final_sinh = 0
    for i in range(0, n):
        sinh = x**(2 * i + 1) / math.factorial(2 * i + 1)
        final_sinh += sinh
    return final_sinh
# Cosh Function


def cosh(x, n):
    final_cosh = 0
    for i in range(0, n):
        cosh = x**(2 * i) / math.factorial(2 * i)
        final_cosh += cosh
    return final_cosh

# print(sin(3.14, 10))
# print(cos(3.14, 10))
# print(sinh(3.14, 10))
# print(cosh(3.14, 10))


### ESSAY 5 ###
# Mean Difference of n_th Root Error Function
def md_nre_simple(y, y_hat, n, p):
    md_nre = (y**(1 / n) - y_hat**(1 / n))**p
    return md_nre

# print(md_nre_simple(0.6, 0.1, 2, 1))

### MULTIPLE CHOICE ###
# MC 1
# f1_score(tp=2, fp=3, fn=5)

# MC 2
# print(is_number(1))
# print(is_number('n'))

# MC 3
# ReLU

# MC 4 & 5 & 6
# calculate_loss()

# MC 7
# calculate absolute error


def absolute_error(y, y_hat):
    absolute_error = abs(y - y_hat)
    return absolute_error
# print(absolute_error(y=2, y_hat=9))

# MC 8
# calculate squared error


def squared_error(y, y_hat):
    squared_error = (y - y_hat)**2
    return squared_error
# print(squared_error(y=2, y_hat=1))

# MC 9
# print(cos(3.14, 10))

# MC 10
# print(sin(3.14, 10))

# MC 11
# print(sinh(3.14, 10))

# MC 12
# print(cosh(3.14, 10))

# MC 13
# see essay 5
