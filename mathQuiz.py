import tkinter as tk
import random

def new_question():
   global x, y
   x = random.randint(1, 100)
   y = random.randint(1, 100)
   question_label.config(text=f"{x} + {y} = ?")
   entry.delete(0, tk.END)
   feedback_label.config(text="")
  feedback_label.config(text="")

def check():
   try:
       answer = int(entry.get())
       if answer == x + y:
      if answer == x + y:
           feedback_label.config(text="✅ Richtig!", fg="green")
       else:
           feedback_label.config(text=f"❌ Falsch! Richtige Antwort: {x + y}", fg="red")
       root.after(1500, new_question)
   except:
       feedback_label.config(text="Bitte Zahl eingeben!", fg="orange")

root = tk.Tk()
root.title("Mathe Quiz")

question_label = tk.Label(root, font=("Arial", 18))
question_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack()

check_button = tk.Button(root, text="Antwort prüfen", command=check)
check_button.pack(pady=5)

feedback_label = tk.Label(root, font=("Arial", 14))
feedback_label.pack(pady=10)

new_question()
root.mainloop()
