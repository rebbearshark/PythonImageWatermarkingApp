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
# create image variables that will be edited by functions later on
base_image = ""
merged_image = ""
# Title window
window.title("Image Watermarking")

# resize window's min size
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


# defining functions


def upload_image():
    # open file explorer window to select file
    filename = askopenfilename(initialdir="/",
                               title="Select a File",
                               )
    # Change label contents
    image_file_input.delete(0, END)
    image_file_input.insert(0, filename)


def upload_water_mark():
    # open file explorer window to select file
    filename = askopenfilename(initialdir="/",
                               title="Select a File",
                               )
    print(filename)
    # Change label contents
    watermark_file_input.delete(0, END)
    watermark_file_input.insert(0, filename)


def make_image():
    global base_image, image_generated, merged_image
    # open images pulled in from the watermark and image field if fields are full otherwise alerts user
    if image_file_input.get() != "" and watermark_file_input != "":
        back_image = Image.open("/" + image_file_input.get())
        front_image = Image.open("/" + watermark_file_input.get())
        # converts both images to RGBA, originally added to try to use different formats together but couldn't solve
        # the issue yet
        back_image.convert("RGBA")
        front_image.convert("RGBA")
        # resize the images if they are too large
        if back_image.height < MAX_HEIGHT:
            resize_height = back_image.height
        else:
            resize_height = MAX_HEIGHT
        # resize both images to match each other
        resize_ratio = resize_height / back_image.height
        resize_width = int(resize_ratio * back_image.width)
        resized_back = back_image.resize((resize_width, resize_height))
        resized_front = front_image.resize((resize_width, resize_height))
        # merge images together
        try:
            merged_image = Image.blend(resized_back, resized_front, 0.05)
        except ValueError:
            # if a ValueError is received because the file types don't match user will receive an error
            tkinter.messagebox.showerror(
                message="Files must be of the same type to watermark. Please choose another file or convert the files "
                        "before attempting")
        else:
            # if no value error the new image will be created and the canvas will change to show the user the image
            # they generated
            base_image = ImageTk.PhotoImage(merged_image)
            image_generated = True
            canvas.itemconfig(generated_image, image=base_image)
            canvas.config(width=base_image.width(), height=base_image.height())
    else:
        tkinter.messagebox.showerror(message="A file and watermark must be selected to generate a new image")


def save_image():
    global merged_image, image_generated
    # checks to make sure user has set a file name
    if file_name_input.get() != "":
        if image_generated:
            # user selects a directory to save the file
            file_path = askdirectory(initialdir="/",
                                     title="Select save location",
                                     )
            # file is saved as a png and user is alerted
            merged_image.save(file_path + "/" + file_name_input.get() + ".png", "PNG")
            tkinter.messagebox.showinfo(message="Save Successful!")
        else:
            # message shown if new image has not been generated
            tkinter.messagebox.showerror(message="A new photo must be generated before you can save")
    else:
        # message shown if file name does not exist
        tkinter.messagebox.showerror(message="You must choose a file name before saving")


# img field
canvas = Canvas(width=400, height=500)
canvas.grid(row=0, column=0, columnspan=3)
base_image = Image.open(fp="images/intro_banner.png")
background_img = ImageTk.PhotoImage(base_image)
generated_image = canvas.create_image(0, 0, image=background_img, anchor="nw")

# labels to describe fields
image_label = Label(text="Image", width=15)
watermark_label = Label(text="Watermark", width=15)
file_name_label = Label(text="Output file name", width=15)
image_label.grid(row=1, column=0)
watermark_label.grid(row=2, column=0)
file_name_label.grid(row=4, column=0)

# fields to input file paths
image_file_input = Entry(width=40)
watermark_file_input = Entry(width=40)
file_name_input = Entry(width=60)
image_file_input.grid(row=1, column=1)
watermark_file_input.grid(row=2, column=1)
file_name_input.grid(row=4, column=1)

# upload buttons
image_upload_button = Button(text="Select Image", command=upload_image, width=10)
image_upload_button.grid(row=1, column=2)
watermark_upload_button = Button(text="Select Image", command=upload_water_mark, width=10)
watermark_upload_button.grid(row=2, column=2)

# create image button
create_button = Button(text="Generate Image", command=make_image, width=58)
create_button.grid(row=3, column=0, columnspan=3)

# save button
save_button = Button(text="Save Image", width=58, command=save_image)
save_button.grid(row=5, column=0, columnspan=3)

window.mainloop()
