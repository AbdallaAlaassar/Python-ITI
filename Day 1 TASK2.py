v = input("enter a word: ")
print("locations of the letter 'i':")

for i in range(len(v)):
    if v[i] == 'i':
        print(i, end=",\t")