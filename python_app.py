import tkinter as tk
from tkinter import filedialog,messagebox

def replace_word_in_file(file_path, old_word, new_word):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    words = content.split()
    # Checks wheather the word is present in the file or not
    for w in words:
        if w == old_word:
            break
        else:
            print("Word not found in the file")
            messagebox.showinfo("Error", "Word Not found")
            return False
    
    # Replace the old word with the new word
    modified_content = content.replace(old_word, new_word)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

    print("Word replacement completed and file saved successfully!")
    messagebox.showinfo("Success", "Word replacement completed and file saved successfully!")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)

def replace_words():
    file_path = file_entry.get()
    old_word = old_word_entry.get()
    new_word = new_word_entry.get()

    replace_word_in_file(file_path, old_word, new_word)

    # Clear the entry fields
    file_entry.delete(0, tk.END)
    old_word_entry.delete(0, tk.END)
    new_word_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Word Replacement Tool")

# File selection
file_label = tk.Label(window, text="Select File:")
file_label.pack()

file_entry = tk.Entry(window, width=50)
file_entry.pack()

file_button = tk.Button(window, text="Browse", command=select_file)
file_button.pack()

# Word replacement
old_word_label = tk.Label(window, text="Word to Replace:")
old_word_label.pack()

old_word_entry = tk.Entry(window, width=50)
old_word_entry.pack()

new_word_label = tk.Label(window, text="New Word:")
new_word_label.pack()

new_word_entry = tk.Entry(window, width=50)
new_word_entry.pack()

replace_button = tk.Button(window, text="Replace", command=replace_words)
replace_button.pack()

window.mainloop()

