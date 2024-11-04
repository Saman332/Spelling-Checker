import tkinter
from tkinter import *
from textblob import TextBlob

# Initialize the main window
root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    blob = TextBlob(word)
    corrected_word = str(blob.correct())
    
    if word.lower() == corrected_word.lower():
        result_text = "Correct spelling"
    else:
        result_text = f"Corrected spelling: {corrected_word}"
    
    result_label.config(text=result_text)

heading = Label(root, text="Spelling Checker", font=("Times New Roman", 30, "bold"), bg="gray", fg="white")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
button.pack(pady=20)

result_label = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
result_label.place(x=100, y=250)

root.mainloop()
