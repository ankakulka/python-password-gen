import random as rd
import string
import PyPDF2 as P2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

reader = P2.PdfReader("example.pdf")
writer = P2.PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF


# Save the new PDF to a file
with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)

#  Generate alphanumeric random password ( generate alphabet and pick random letters)
my_pass = []
alphabet_U = list(string.ascii_uppercase)
alphabet_L = list(string.ascii_lowercase)
alphabet = alphabet_U + alphabet_L
special_char = ["!", "#", "$", "@", "^", "*", "_"]

i = 0
while(i < 12):
    if i % 2 == 0:
        my_num = rd.randrange(10)
        my_pass.append(my_num)
    else:
        rand_al = rd.randrange(52)
        my_pass.append(alphabet[rand_al])
    i += 1

special_char_num = rd.randrange(7)
my_pass_rand = rd.randrange(12)

# Replace a character in the password list at a random index with a special character
my_pass[my_pass_rand] = special_char[special_char_num]

# Map the password list to create a string
temp_pass = map(str, my_pass)
final_pass = ''.join(temp_pass)

print(final_pass)

# Create the main window
app = tk.Tk()
app.title("Password Gen App")

def copy_to_clipboard():
    if final_pass:
        app.clipboard_clear()
        app.clipboard_append(final_pass)
        app.update()  # required on macOS
        messagebox.showinfo("Copy Successful", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Copy Warning", "No text to copy. Generate a new password first.")

copy_button = ttk.Button(app, text="Generate random password", command=copy_to_clipboard)
copy_button.pack(pady=20)


# Set window size
app.geometry("200x80")

# Change the app background color
app.configure(bg='#856ff8')

writer.encrypt(final_pass)

# Run the main loop
app.mainloop()


