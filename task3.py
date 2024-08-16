import random
import string


length = int(input("Enter the desired length of the password: "))


print("Choose the complexity of the password:")
print("1: Lowercase letters only")
print("2: Lowercase and Uppercase letters")
print("3: Letters and Digits")
print("4: Letters, Digits, and Special Characters")

complexity = input("Enter your choice (1/2/3/4): ")

if complexity == '1':
    characters = string.ascii_lowercase
elif complexity == '2':
    characters = string.ascii_letters
elif complexity == '3':
    characters = string.ascii_letters + string.digits
elif complexity == '4':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice. Using default complexity (Letters, Digits, and Special Characters).")
    characters = string.ascii_letters + string.digits + string.punctuation


password = ''.join(random.choice(characters) for _ in range(length))


print("Generated Password:", password)
