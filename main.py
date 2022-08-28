import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image, ImageTk

# Max image size
MAX_HEIGHT = 500

# variable to keep user from downloading a non-existent image
image_generated = False
# create a window
window = Tk()
default_water_mark_text = "DEFAULT"
base_image = ""
merged_image = ""
# Title window
window.title("Image Watermarking")

# resize window's min size
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


# defining functions


# Function for opening the
# file explorer window
def upload_image():
    filename = askopenfilename(initialdir="/",
                               title="Select a File",
                               )
    print(filename)
    # Change label contents
    image_file_input.delete(0, END)
    image_file_input.insert(0, filename)


def upload_water_mark():
    filename = askopenfilename(initialdir="/",
                               title="Select a File",
                               )
    print(filename)
    # Change label contents
    watermark_file_input.delete(0, END)
    watermark_file_input.insert(0, filename)


def make_image():
    global base_image, image_generated, merged_image
    back_image = Image.open("/" + image_file_input.get())
    front_image = Image.open("/" + watermark_file_input.get())
    back_image.convert("RGBA")
    front_image.convert("RGBA")
    if back_image.height < MAX_HEIGHT:
        resize_height = back_image.height
    else:
        resize_height = MAX_HEIGHT
    resize_ratio = resize_height / back_image.height
    resize_width = int(resize_ratio * back_image.width)
    resized_back = back_image.resize((resize_width, resize_height))
    resized_front = front_image.resize((resize_width, resize_height))
    try:
        merged_image = Image.blend(resized_back, resized_front, 0.05)
    except ValueError:
        tkinter.messagebox.showerror(
            message="Files must be of the same type to watermark. Please choose another file or convert the files before attemtping")
    else:
        base_image = ImageTk.PhotoImage(merged_image)
        image_generated = True
        canvas.itemconfig(generated_image, image=base_image)
        canvas.config(width=base_image.width(), height=base_image.height())


def save_image():
    global merged_image, image_generated
    if image_generated:
        file_path = askdirectory(initialdir="/",
                                title="Select save location",
                                )
        merged_image.save(file_path + "/watermark.png", "PNG")
    else:
        tkinter.messagebox.showerror(message="A new photo must be generated before you can save")



# img field
canvas = Canvas(width=300, height=414)
canvas.grid(row=0, column=0, columnspan=3)
base_image = Image.open(fp="/Users/jarrednoffsinger/Pictures/Iphone12 copy.png")
resized_base_image = base_image.resize((400, 350))
background_img = ImageTk.PhotoImage(resized_base_image)
generated_image = canvas.create_image(0, 0, image=background_img, anchor="nw")

# labels to describe fields
image_label = Label(text="Image", width=10)
watermark_label = Label(text="Watermark", width=10)
image_label.grid(row=1, column=0)
watermark_label.grid(row=2, column=0)

# fields to input file paths
image_file_input = Entry(width=30)
watermark_file_input = Entry(width=30)
image_file_input.grid(row=1, column=1)
watermark_file_input.grid(row=2, column=1)

# upload buttons
image_upload_button = Button(text="Select Image", command=upload_image, width=10)
image_upload_button.grid(row=1, column=2)
watermark_upload_button = Button(text="Select Image", command=upload_water_mark, width=10)
watermark_upload_button.grid(row=2, column=2)

# create image button
create_button = Button(text="Generate Image", command=make_image, width=60)
create_button.grid(row=3, column=0, columnspan=3)

# save button
save_button = Button(text="Save Image", width=60, command=save_image)
save_button.grid(row=4, column=0, columnspan=3)

window.mainloop()
