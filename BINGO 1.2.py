# Write a script to generate an aleatoric code with a letter and a number (like a BINGO code)

import random

# Define the available letters and numbers
letters = ['B', 'I', 'N', 'G', 'O']
min_number = 1
max_number = 99

# Generate a random letter
random_letter = random.choice(letters)

# Generate a random number between 1 and 99
random_number = random.randint(min_number, max_number)

# Ensure the random number is two digits by adding a leading zero if necessary
random_number_str = str(random_number).zfill(2)

# Create the random code by combining the letter and number
random_code = f"{random_letter}{random_number_str}"

# Display the random code
print("Random Code:", random_code)
