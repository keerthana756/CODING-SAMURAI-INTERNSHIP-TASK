import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

# Create the main window
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")

# Entry widget for the calculator screen
screen = tk.Entry(app, font="lucida 20 bold", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(app)
button_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create and place buttons
for row in buttons:
    frame_row = tk.Frame(button_frame)
    frame_row.pack(expand=True, fill="both")
    for button_text in row:
        btn = tk.Button(frame_row, text=button_text, font="lucida 15 bold", relief=tk.RAISED, height=2, width=4)
        btn.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

# Run the application
app.mainloop()



