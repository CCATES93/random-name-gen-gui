import tkinter as tk
import random

# List of first names
first_names = ['John', 'Jane', 'Mike', 'Emily', 'David', 'Rachel', 'Matthew', 'Olivia', 'William', 'Lily', 'Jacob', 'Sophia', 'Ethan', 'Ava', 'Noah', 'Emma', 'Liam', 'Mia', 'Mason', 'Madison', 'Lucas', 'Isabella', 'Alexander', 'Chloe', 'Daniel', 'Elizabeth', 'Benjamin', 'Grace', 'Luke', 'Hannah', 'Samuel']

# List of last names
last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Anderson', 'Wilson', 'Moore', 'Jackson', 'Lee', 'Garcia', 'Perez', 'Martin', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson', 'Carter', 'Mitchell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Turner']

# Create main window
root = tk.Tk()
root.title('Random Name Generator')

# Create label for first name
label_first = tk.Label(root, text='First Name:')
label_first.pack()

# Create entry box for first name
entry_first = tk.Entry(root)
entry_first.pack()

# Create label for last name
label_last = tk.Label(root, text='Last Name:')
label_last.pack()

# Create entry box for last name
entry_last = tk.Entry(root)
entry_last.pack()

# Function to generate random name
def generate_name():
    # Select a random first name and last name from the lists
    first = random.choice(first_names)
    last = random.choice(last_names)
    
    # Set the entry boxes to the generated name
    entry_first.delete(0, tk.END)
    entry_first.insert(0, first)
    entry_last.delete(0, tk.END)
    entry_last.insert(0, last)

# Create button to generate random name
button_generate = tk.Button(root, text='Generate', command=generate_name)
button_generate.pack()

# Function to open second window
def open_window():
    # Create new window
    window = tk.Toplevel(root)
    window.title('Random Names List')

    # Create label for instructions
    label_instruction = tk.Label(window, text='Click the button to generate a random name:')
    label_instruction.pack()

    # Create list box to display generated names
    listbox_names = tk.Listbox(window)
    listbox_names.pack()

    # Function to generate and display random name
    def generate_and_display_name():
        # Select a random first name and last name from the lists
        first = random.choice(first_names)
        last = random.choice(last_names)

        # Create full name and add to list box
        name = first + ' ' + last
        listbox_names.insert(tk.END, name)

    # Create button to generate and display random name
    button_generate = tk.Button(window, text='Generate', command=generate_and_display_name)
    button_generate.pack()

# Create button to open second window
button_open = tk.Button(root, text='Open Names List', command=open_window)
button_open.pack()

# Run the GUI
root.mainloop()