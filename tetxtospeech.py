import tkinter as tk
import pyttsx3

def speak_text():
    engine = pyttsx3.init()
    engine.say(text.get())
    engine.runAndWait()
    
window = tk.Tk()
window.title("Text to Speech")
window.geometry("400x200")

tk.Label(window, text="Enter text:", font=("Times New Roman", 14)).pack(pady=10)
text = tk.Entry(window, font=("Times New Roman", 14))
text.pack(pady=10)

button = tk.Button(window, text="Speak", font=("Arial", 14), command=speak_text)
button.pack(pady=10)

window.mainloop()
