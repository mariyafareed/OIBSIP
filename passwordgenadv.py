#project title : PASSWORD GENERATOR(ADVANCE)
import random
import string
import tkinter as tk
from tkinter import messagebox, IntVar
import pyperclip

def generate_password():
    """
    Generates a random password based on the selected length and character types.
    """
    length = length_slider.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_uppercase or use_lowercase or use_digits or use_special):
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

def copy_to_clipboard():
    """
    Copies the generated password to the clipboard.
    """
    generated_password = password_entry.get()
    if generated_password:
        pyperclip.copy(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning", "No password generated yet.")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.config(bg='gray20')

# Title label for the application
passwordLabel = tk.Label(root, text="PASSWORD GENERATOR", font=('times new roman', 20, 'bold'), bg='lightblue', fg='black')
passwordLabel.grid()

# Choice variable for radiobuttons (Not used in this implementation)
choice = IntVar()

# Radiobuttons for password strength (for potential future use)
Font = ('times new roman', 16, 'bold')
weakradiobutton = tk.Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradiobutton.grid(pady=5)
mediumradiobutton = tk.Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradiobutton.grid(pady=5)
strongradiobutton = tk.Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradiobutton.grid(pady=5)

# Label for password length
lengthLabel = tk.Label(root, text="Password Length:", font=Font, bg='lightblue', fg='black')
lengthLabel.grid()

# Slider to select password length
length_slider = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_slider.set(12)
length_slider.grid()

# Frame for character type checkboxes
checkbox_frame = tk.Frame(root, bg='gray20')
checkbox_frame.grid(pady=10)
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

# Checkboxes for selecting character types
tk.Checkbutton(checkbox_frame, text="Uppercase", variable=uppercase_var).grid(row=0, column=0, sticky='w')
tk.Checkbutton(checkbox_frame, text="Lowercase", variable=lowercase_var).grid(row=0, column=1, sticky='w')
tk.Checkbutton(checkbox_frame, text="Digits", variable=digits_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_var).grid(row=1, column=1, sticky='w')

# Button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(pady=10)

# Entry to display the generated password
password_entry = tk.Entry(root, width=40, bd=2, relief=tk.SOLID)
password_entry.grid(pady=10)

# Button to copy the password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(pady=10)

# Run the main event loop
root.mainloop()