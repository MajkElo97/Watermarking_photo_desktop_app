from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

img_path = 'bg.jpg'
logo_path = 'bg.jpg'
photo = None
new_logo = None


def open_photo():
    global img_path, photo, label_photo, tk_photo
    img_path = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("All files", "*.*")])
    photo = Image.open(img_path)
    tk_photo = ImageTk.PhotoImage(photo.resize((200, 200)))
    label_photo.configure(image=tk_photo)
    label_photo.image = tk_photo


def open_logo():
    global logo_path, new_logo, logo, label_logo, tk_logo
    logo_path = fd.askopenfilename(
        title="Select a file of any type",
        filetypes=[("All files", "*.*")])
    logo = Image.open(logo_path)
    tk_logo = ImageTk.PhotoImage(logo.resize((200, 200)))
    label_logo.configure(image=tk_logo)
    label_logo.image = tk_logo


def save():
    global new_logo
    width = int(logo_width_input.get())
    height = int(logo_height_input.get())
    x_offset = int(logo_x_offset_input.get())
    y_offset = int(logo_y_offset_input.get())
    new_logo = logo.resize((width, height))
    box = (photo.size[0] - x_offset - new_logo.size[0],
           photo.size[1] - y_offset - new_logo.size[1],
           photo.size[0] - x_offset,
           photo.size[1] - y_offset)
    photo.paste(new_logo, box)
    finished_img_path = img_path[:-4] + "_WM.jpg"
    photo.save('Watermarked_photos\photo_with_watermark.jpg')
    photo.show()
    success_text.set(f"Success!  File saved to {finished_img_path}.")


def close_app():
    root.destroy()


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.config(padx=60, pady=60, bg="white")
root.title("Watermark marker")

button_open_photo = Button(text='Choose photo', command=open_photo, width=30)
button_open_photo.grid(row=0, column=0, padx=10, pady=10)

button_open_logo = Button(text='Choose watermark', command=open_logo, width=30)
button_open_logo.grid(row=0, column=1, padx=10, pady=10)

logo_width_label = Label(text="Choose the width of the logo:", bg="white")
logo_width_label.grid(row=2, column=0)
logo_width_input = Entry(width=20)
logo_width_input.insert(0, "50")
logo_width_input.grid(row=2, column=1, sticky="w")

logo_height_label = Label(text="Choose the height of the logo:", bg="white")
logo_height_label.grid(row=3, column=0)
logo_height_input = Entry(width=20)
logo_height_input.insert(0, "50")
logo_height_input.grid(row=3, column=1, sticky="w")

logo_x_offset_label = Label(text="Choose the offset X of the logo:", bg="white")
logo_x_offset_label.grid(row=4, column=0)
logo_x_offset_input = Entry(width=20)
logo_x_offset_input.insert(0, "20")
logo_x_offset_input.grid(row=4, column=1, sticky="w")

logo_y_offset_label = Label(text="Choose the offset Y of the logo:", bg="white")
logo_y_offset_label.grid(row=5, column=0)
logo_y_offset_input = Entry(width=20)
logo_y_offset_input.insert(0, "20")
logo_y_offset_input.grid(row=5, column=1, sticky="w")

button_render = Button(text='Render', command=save, width=30)
button_render.grid(row=6, column=0, columnspan=2, pady=20)

button_quit = Button(text="Quit", command=close_app, width=30)
button_quit.grid(row=7, column=0, columnspan=2, pady=10)

photo = Image.open(img_path)
tk_photo = ImageTk.PhotoImage(photo.resize((200, 200)))
label_photo = Label(image=tk_photo)
label_photo.grid(row=1, column=0, pady=10)

logo = Image.open(logo_path)
tk_logo = ImageTk.PhotoImage(logo.resize((200, 200)))
label_logo = Label(image=tk_logo)
label_logo.grid(row=1, column=1, pady=10)

success_text = StringVar()
success_text.set("")
success_label = Label(textvariable=success_text, background='white')
success_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
