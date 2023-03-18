from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

translator = Translator()

# Get a list of all available languages
language_codes = list(LANGUAGES.keys())
language_names = list(LANGUAGES.values())

def translate_text():
    text = input_text.get("1.0", END).strip()
    source_language = language_codes[language_names.index(source_var.get())]
    target_language = language_codes[language_names.index(target_var.get())]
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    output_text.configure(state='normal')
    output_text.delete('1.0', END)
    output_text.insert(END, translated_text.text)
    output_text.configure(state='disabled')

root = Tk()
root.title("Translator")

# Create input and output text widgets
input_text = Text(root, height=5, width=50)
input_text.grid(row=0, column=0, padx=10, pady=10)

output_text = Text(root, height=5, width=50, state='disabled')
output_text.grid(row=1, column=0, padx=10, pady=10)

# Create language selection dropdowns
source_var = StringVar()
source_var.set("English")

target_var = StringVar()
target_var.set("Spanish")

source_dropdown = OptionMenu(root, source_var, *language_names)
source_dropdown.grid(row=2, column=0, padx=10, pady=10)

target_dropdown = OptionMenu(root, target_var, *language_names)
target_dropdown.grid(row=3, column=0, padx=10, pady=10)

# Create translate button
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()