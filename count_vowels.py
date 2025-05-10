def count_vowels():
    text = input("Enter a word to count vowels: ")
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
