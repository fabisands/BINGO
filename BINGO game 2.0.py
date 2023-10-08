import random
import msvcrt  # Import msvcrt for keyboard input on Windows

# Function to generate random Bingo numbers
def generate_bingo_numbers():
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

# Function to generate a random code
def generate_random_code():
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
    print(random_code)

# Call the function to generate Bingo numbers once
generate_bingo_numbers()

# Allow the user to generate random codes by pressing Enter and terminate on any other key press
print("Press Enter to generate a random code, or any other key to exit...")
while True:
    key = msvcrt.getch()  # Get a key press
    if key == b'\r':  # Enter key was pressed
        generate_random_code()
    else:
        break  # Exit the loop if any other key
