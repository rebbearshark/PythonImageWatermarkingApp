from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# create a window
window = Tk()
default_water_mark_text = "DEFAULT"
base_image = ""
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
    global base_image
    back_image = Image.open("/" + image_file_input.get())
    front_image = Image.open("/" + watermark_file_input.get())
    resize_height = back_image.height
    resize_ratio = resize_height / back_image.height
    resize_width = int(resize_ratio * back_image.width)
    resized_back = back_image.resize((resize_width, resize_height))
    watermark_percent = 0.3
    resized_front = front_image.resize((int(watermark_percent * resize_ratio * front_image.width),
                                        int(watermark_percent * resize_ratio * front_image.height)))
    merged_image = Image.new("RGBA", (resize_width, resize_height))
    merged_image.paste(resized_back)
    merged_image.paste(resized_front, (0, 0))
    base_image = ImageTk.PhotoImage(merged_image)
    canvas.itemconfig(generated_image, image=base_image)
    canvas.config(width=base_image.width(), height=base_image.height())


# img field
canvas = Canvas(width=300, height=414)
canvas.grid(row=0, column=0, columnspan=3)
base_image = Image.open(fp="/Users/jarrednoffsinger/Pictures/Iphone12 copy.png")
resized_base_image = base_image.resize((400, 350))
background_img = ImageTk.PhotoImage(resized_base_image)
generated_image = canvas.create_image(0, 0, image=background_img, anchor="nw")

# labels to describe fields
image_label = Label(text="Image")
watermark_label = Label(text="Watermark")
image_label.grid(row=1, column=0)
watermark_label.grid(row=2, column=0)

# fields to input file paths
image_file_input = Entry(width=10)
watermark_file_input = Entry(width=10)
image_file_input.grid(row=1, column=1)
watermark_file_input.grid(row=2, column=1)

# upload buttons
image_upload_button = Button(text="Select Image", command=upload_image)
image_upload_button.grid(row=1, column=2)
watermark_upload_button = Button(text="Select Image", command=upload_water_mark)
watermark_upload_button.grid(row=2, column=2)

# create image button
create_button = Button(text="Generate Image", command=make_image)
create_button.grid(row=3, column=0, columnspan=3)

# save button
save_button = Button(text="Save Image")
save_button.grid(row=4, column=0, columnspan=3)

window.mainloop()
