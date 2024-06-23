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


# MC2
print(f"MC2: {count_letters('smiles')} - Answer: a)")
