import random

print("Welcome to the PyPassword Generator")

# Define character combinations
combination1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'  # Lowercase letters
]

combination2 = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'  # Uppercase letters
]

combination3 = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',  # Digits
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'   # Special characters
]

# Get user input for password components
length = int(input("How many Letters Would You like in your password?: "))
symbol = int(input("How many Symbols Would You like in your password?: "))
number = int(input("How many Numbers Would You like in your password?: "))

# Create a list to hold the password components
password_list = []

# Append random characters from the combinations
for _ in range(length):
    password_list.append(random.choice(combination1 + combination2))  # Choose from both lowercase and uppercase

for _ in range(symbol):
    password_list.append(random.choice(combination3[10:]))  # Choose only symbols

for _ in range(number):
    password_list.append(random.choice(combination3[:10]))  # Choose only digits

# Shuffle the password list to mix characters
random.shuffle(password_list)

# Join the list to form the final password
password = ''.join(password_list)

print(f"Your password is: {password}")

