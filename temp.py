from tkinter import *
from tkinter import font

# Initialize the main Tkinter window
root = Tk()

# Get a list of all available font families
lis = font.families()

# Create a scrollable frame to hold the labels
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
frame = Frame(canvas)

# Configure canvas and frame to support scrolling
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw")
frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Add labels for each font family
for j, font_name in enumerate(lis):
    label = Label(frame, text=f"Hello world {font_name}", font=(font_name, 10))
    label.grid(row=j, column=0, sticky="w", padx=5, pady=2)

# Run the Tkinter event loop

for j in lis:
    if "Math" in j:
        print(j)
root.mainloop()
