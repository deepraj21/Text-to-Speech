import tkinter as tk
import pyttsx3


def speak_text():
    engine = pyttsx3.init()
    engine.say(text.get())
    engine.runAndWait()


# Create a tkinter window
window = tk.Tk()
window.title("Text to Speech")
window.geometry("400x200")

# Create a label and an entry widget for user input
tk.Label(window, text="Enter text:", font=("Times New Roman", 14)).pack(pady=10)
text = tk.Entry(window, font=("Times New Roman", 14))
text.pack(pady=10)

# Create a button to trigger text-to-speech conversion
button = tk.Button(window, text="Speak", font=(
    "Arial", 14), command=speak_text)
button.pack(pady=10)

# Run the tkinter event loop
window.mainloop()
