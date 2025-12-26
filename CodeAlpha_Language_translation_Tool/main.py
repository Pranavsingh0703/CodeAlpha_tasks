# py -3.10 -m venv ai_env
# ai_env\Scripts\activate
# python main.py
import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Initialize translator
translator = Translator()

# Language options
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko"
}

# Translate function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text")
            return

        src_lang = languages[source_lang.get()]
        tgt_lang = languages[target_lang.get()]

        translated = translator.translate(
            text,
            src=src_lang,
            dest=tgt_lang
        )

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy function
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# UI setup
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x450")

# Title
tk.Label(root, text="Language Translation Tool",
         font=("Arial", 16, "bold")).pack(pady=10)

# Input text
tk.Label(root, text="Enter Text").pack()
input_text = tk.Text(root, height=6)
input_text.pack(padx=10, pady=5)

# Language selection
frame = tk.Frame(root)
frame.pack(pady=10)

source_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15)
source_lang.set("English")
source_lang.grid(row=0, column=0, padx=10)

target_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15)
target_lang.set("Hindi")
target_lang.grid(row=0, column=1, padx=10)

# Translate button
tk.Button(root, text="Translate", command=translate_text,
          bg="green", fg="white", width=15).pack(pady=10)

# Output text
tk.Label(root, text="Translated Text").pack()
output_text = tk.Text(root, height=6)
output_text.pack(padx=10, pady=5)

# Copy button
tk.Button(root, text="Copy Text", command=copy_text,
          bg="blue", fg="white", width=15).pack(pady=10)

root.mainloop()
