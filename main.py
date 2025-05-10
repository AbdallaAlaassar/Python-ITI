
import count_vowels
vowel_count = count_vowels.count_vowels()
print(f"Number of vowels: {vowel_count}")


import location
word = input("Enter a word to find location of letter i: ")
location.find_letter_i(word)


import multi
num = int(input("Enter a single number: "))
multi.multiplication_table(num)



import mario
height = int(input("Enter the height of the pyramid: "))
mario.mario_pyramid(height)


import order
order.sort_elements()



import table
n = int(input("Enter a number to generate its multiplication table: "))
multiplication_table = table.multiplication_table(n)
print(multiplication_table)



import mail
name, email = mail.get_user_info()
print("\n✅ Your Information:")
print(f"Name : {name}")
print(f"Email: {email}")




import auth
auth.validate_user_credentials()