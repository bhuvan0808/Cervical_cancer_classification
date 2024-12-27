import tkinter as tk
from tkinter import filedialog

def load_image():
    file_path = filedialog.askopenfilename()
    # Load the selected image for processing

root = tk.Tk()
button = tk.Button(root, text="Select Image", command=load_image)
button.pack()

root.mainloop()
