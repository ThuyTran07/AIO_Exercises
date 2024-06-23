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

# MC3
result = count_words(file_path)
print(f"MC3: {result['man']} - Answer: c)")
