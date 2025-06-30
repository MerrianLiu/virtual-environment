import tkinter as tk
from PIL import Image, ImageTk
# This is Merrian's stuff
def main():
    root = tk.Tk()
    root.title("Men Viewer")

    pil_image = Image.open("pig.jpg")

    tk_image = ImageTk.PhotoImage(pil_image)

    label = tk.Label(root, image=tk_image)
    label.pack(padx=10, pady=10)

    root.mainloop()

if __name__=="__main__":
    main()
