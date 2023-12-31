import random
import tkinter as tk
from tkinter import Canvas, Scrollbar

# Initialize a variable to keep track of the code number
code_number = 0

# Function to generate random Bingo numbers
def generate_bingo_board():
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

    # Clear the existing text in the bingo_label
    bingo_label.config(text="")

    # Display the letters BINGO above each column
    bingo_label.config(text="B   I   N   G   O")

    # Display the generated numbers in 5 rows of 5 numbers each
    for i in range(5):
        row = random_numbers[i * 5: (i + 1) * 5]
        row_str = "  ".join(row)
        bingo_label.config(text=bingo_label.cget("text") + f"\n{row_str}")

# Function to generate a random code
def generate_random_code():
    global code_number  # Use the global code_number variable
    code_number += 1  # Increment the code_number

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
    random_code = f"Code Number {code_number}: {random_letter}{random_number_str}"

    # Append the random code to the code_label
    code_label_text.set(code_label_text.get() + f"\n{random_code}")

# Create the main window
window = tk.Tk()
window.title("Random Code Generator")

# Create a frame to hold the buttons and position it at the top of the window
button_frame = tk.Frame(window)
button_frame.pack()

# Create a button to generate Bingo board without "Generate" in the label
bingo_button = tk.Button(button_frame, text="BINGO Board", command=generate_bingo_board, font=("Helvetica", 16))
bingo_button.pack(side=tk.LEFT)

# Create a button to generate random codes without "Generate" in the label
code_button = tk.Button(button_frame, text="Random Code", command=generate_random_code, font=("Helvetica", 16))
code_button.pack(side=tk.LEFT)

# Create a label to display BINGO board
bingo_label = tk.Label(window, text="", padx=20, pady=10, font=("Helvetica", 24))
bingo_label.pack()

# Create a Canvas to hold the code_label and add a vertical scrollbar
canvas = Canvas(window, height=300, width=400)
canvas.pack()

# Create a Text widget for displaying random codes
code_label_text = tk.StringVar()
code_label_text.set("")
code_label = tk.Label(canvas, textvariable=code_label_text, padx=20, pady=10, font=("Helvetica", 24))
code_label.pack()

# Create a Scrollbar for the Canvas
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the Canvas to work with the Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.create_window((0, 0), window=code_label, anchor="nw")

# Bind mousewheel scrolling to the Canvas
def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

# Run the Tkinter main loop
window.mainloop()
