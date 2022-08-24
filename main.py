from tkinter import *
from tkinter.filedialog import askopenfilename

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
    global base_image
    filename = askopenfilename(initialdir="/",
                               title="Select a File",
                               )
    print(filename)
    # Change label contents
    image_file_input.delete(0, END)
    image_file_input.insert(0, filename)
    base_image = PhotoImage(file=str(filename))
    canvas.itemconfig(back_image, image=base_image)




def upload_water_mark(file):
    pass


def make_image(image, watermark):
    pass


# img field
canvas = Canvas(width=300, height=414)
canvas.grid(row=0, column=0, columnspan=3)
background_img = PhotoImage(file="/Users/jarrednoffsinger/Pictures/Iphone12 copy.png")
back_image = canvas.create_image(150, 207, image=background_img, anchor="center")

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
watermark_upload_button = Button(text="Select Image", command=upload_image)
watermark_upload_button.grid(row=2, column=2)

# save button
save_button = Button(text="Save Image")
save_button.grid(row=3, column=0, columnspan=3)


window.mainloop()
