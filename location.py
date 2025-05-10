
def find_letter_i(word):
    print("Locations of the letter 'i':")
    for i in range(len(word)):
        if word[i] == 'i':
            print(i, end=",\t")
