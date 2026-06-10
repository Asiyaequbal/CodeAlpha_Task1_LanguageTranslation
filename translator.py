from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Function for translation
def translate_text():
    try:
        translated = GoogleTranslator(
            source=source_lang.get(),
            target=target_lang.get()
        ).translate(input_text.get("1.0", END))

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {e}")

# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

# Source Language
Label(root, text="Source Language").pack()

source_lang = ttk.Combobox(root, values=[
    "english", "hindi", "french", "german", "spanish"
])
source_lang.pack()
source_lang.set("english")

# Target Language
Label(root, text="Target Language").pack()

target_lang = ttk.Combobox(root, values=[
    "english", "hindi", "french", "german", "spanish"
])
target_lang.pack()
target_lang.set("hindi")

# Input Text
Label(root, text="Enter Text").pack()

input_text = Text(root, height=8, width=70)
input_text.pack()

# Translate Button
Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

# Output Text
Label(root, text="Translated Text").pack()

output_text = Text(root, height=8, width=70)
output_text.pack()

root.mainloop()