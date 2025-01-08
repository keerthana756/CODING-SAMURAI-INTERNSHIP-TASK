import tkinter as tk
import random

# Functionality for the game
def start_game():
    """Start the game and generate a random number."""
    global random_number
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    result_label.config(text="Game started! Guess a number between 1 and 100.")
    guess_button.config(state=tk.NORMAL)
    guess_entry.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)  # Clear the input field
    start_button.config(state=tk.DISABLED)  # Disable the start button while the game is ongoing

def check_guess():
    """Check the user's guess and provide feedback."""
    try:
        # Get the user's guess
        guess = int(guess_entry.get().strip())
        guess_entry.delete(0, tk.END)  # Clear the input field after reading the input

        # Validate the guess and give feedback
        if guess < 1 or guess > 100:
            result_label.config(text="Please guess a number between 1 and 100.")
        elif guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"🎉 Congratulations! {guess} is the correct number!")
            guess_button.config(state=tk.DISABLED)
            guess_entry.config(state=tk.DISABLED)
            start_button.config(state=tk.NORMAL)  # Enable the start button for a new game
    except ValueError:
        # Handle non-integer input
        result_label.config(text="Invalid input! Please enter a valid number.")

# Create the main application window
app = tk.Tk()
app.title("Number Guessing Game")  # Title of the application window
app.geometry("400x300")  # Set the size of the window

# Instructions label
instructions = tk.Label(app, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
instructions.pack(pady=10)

# Button to start the game
start_button = tk.Button(app, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

# Entry box for user's guess
guess_entry = tk.Entry(app, font=("Arial", 14), state=tk.DISABLED)  # Initially disabled
guess_entry.pack(pady=10)

# Button to check the user's guess
guess_button = tk.Button(app, text="Check Guess", font=("Arial", 12), command=check_guess, state=tk.DISABLED)  # Initially disabled
guess_button.pack(pady=10)

# Label to display feedback and results
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run the application
app.mainloop()


