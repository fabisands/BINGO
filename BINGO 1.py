# Randomly generate a series of 25 numbers.

import random

# Initialize an empty set to keep track of generated numbers
generated_numbers = set()

# Initialize an empty list for the random numbers
random_numbers = []

# Generate 25 unique random numbers between 1 and 99
while len(generated_numbers) < 25:
    num = random.randint(1, 99)
    if num not in generated_numbers:
        generated_numbers.add(num)
        random_numbers.append(f"{num:02d}")

# Display the letters BINGO above each column
print("B   I   N   G   O")

# Display the generated numbers in 5 rows of 5 numbers each
for i in range(5):
    row = random_numbers[i * 5: (i + 1) * 5]
    row_str = "  ".join(row)
    print(row_str)
