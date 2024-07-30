import pandas as pd
import numpy as np

def create_train_data(file_path):
    data = pd.read_csv(file_path)
    return data.to_numpy()

def compute_prior_probability(train_data):
    y_unique = ["No", "Yes"]
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = len(np.where(train_data[:,-1] == y_unique[i])[0])/len(train_data)
    return prior_probability

def compute_conditional_probability(train_data):
    y_unique = ["No", "Yes"]
    conditional_probability = []
    list_x_name = []
    for i in range(1, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:,i])
        list_x_name.append(x_unique)
        
        x_conditional_probability = np.zeros((len(x_unique), len(y_unique)))
        for m in range(len(x_unique)):
            for n in range(len(y_unique)):
                x_conditional_probability[m,n] = len(np.where((train_data[:,-1] == y_unique[n]) & (train_data[:,i] == x_unique[m]))[0])/ len(np.where(train_data[:,-1] == y_unique[n])[0])

        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name

def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]

def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name

def predict_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p0 = 0
    p1 = 0

    p0 = prior_probability[0] \
        *conditional_probability[0][x1,0] \
        *conditional_probability[1][x2,0] \
        *conditional_probability[2][x3,0] \
        *conditional_probability[3][x4,0]
    p1 = prior_probability[1] \
        *conditional_probability[0][x1,1] \
        *conditional_probability[1][x2,1] \
        *conditional_probability[2][x3,1] \
        *conditional_probability[3][x4,1]
    
    print(p0, p1)

    if  p0>p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred

file_path = "m02ex03_naive_bayes_classifier\data\data.csv"
train_data = create_train_data(file_path)

prior_probability = compute_prior_probability(train_data)
print("P(Play Tennis = No) = ", prior_probability[0])
print("P(Play Tennis = Yes) = ", prior_probability[1])

conditional_probability , list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])

outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

x1 = get_index_from_value("Sunny", list_x_name[0])
print("P(Outlook = Sunny | Play Tennis = Yes) = ", np.round(conditional_probability[0][x1, 1], 2))
print("P(Outlook = Sunny | Play Tennis = No) = ", np.round(conditional_probability[0][x1, 0], 2))

X = ['Sunny','Cool','High','Strong']
prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)
pred = predict_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
