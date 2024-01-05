import customtkinter
#from PIL import Image, ImageTk
import tkinter.filedialog as filedialog

# Set appearance and theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Initialize the main window
root = customtkinter.CTk()
root.title("LSB Steganography Tool")
root.geometry("500x350")

def extract_data():
    print("Extract data")

def select_cover_image():
    print("Select Target image")

def open_hide_data_window():
    hide_window = customtkinter.CTkToplevel(root)
    hide_window.title("Hide Data")
    hide_window.geometry("600x400")

    def select_file_type(file_type):
        print(f"Selected file type to hide: {file_type}")

    def select_target_image():
        file_path = filedialog.askopenfilename()
        print(f"Selected target image: {file_path}")
        # Display the selected image (as a thumbnail) in the window
        # Note: Add your own logic to handle the image display

    # Buttons for selecting the type of content to hide
    hide_text_button = customtkinter.CTkButton(hide_window, text="Hide Text", command=lambda: select_file_type("text"))
    hide_text_button.pack(pady=12, padx=10)

    hide_image_button = customtkinter.CTkButton(hide_window, text="Hide Image", command=lambda: select_file_type("image"))
    hide_image_button.pack(pady=12, padx=10)

    hide_program_button = customtkinter.CTkButton(hide_window, text="Hide Program", command=lambda: select_file_type("program"))
    hide_program_button.pack(pady=12, padx=10)

    # Button to select the target image
    target_image_button = customtkinter.CTkButton(hide_window, text="Select Target Image", command=select_target_image)
    target_image_button.pack(pady=12, padx=10)

# Other functions (extract_data, select_cover_image) remain the same

# Main window content
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="LSB Steganography Program", font=("Roboto", 24))
label.pack(pady=12, padx=10)

hide_button = customtkinter.CTkButton(frame, text="Hide Data", command=open_hide_data_window, font=("Roboto", 16))
hide_button.pack(pady=12, padx=10)

extract_button = customtkinter.CTkButton(frame, text="Extract Data", command=extract_data, font=("Roboto", 16))
extract_button.pack(pady=12, padx=10)

cover_image_button = customtkinter.CTkButton(frame, text="Select Target Image", command=select_cover_image, font=("Roboto", 16))
cover_image_button.pack(pady=12, padx=10)

info_label = customtkinter.CTkLabel(frame, text="Status Information Here", height=10)
info_label.pack(pady=12, padx=10, fill="both")

root.mainloop()




"""
with open('photo.jpeg', 'ab') as f: #Open the jpg file then append bytes as you do not want to overwrite the file.
    f.write(b"Hello World")
with open('photo.jpeg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)
    print(f.read())


import PIL.Image
import io

img = PIL.Image.open('hiddenimage.jpeg')
byte_arr = io.BytesIO()
img.save(byte_arr, format='JPEG')

with open('photo.jpeg', 'ab') as f:
    f.write(byte_arr.getvalue())


with open('photo-hiddenphoto.jpeg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset + 2)

    new_img = PIL.Image.open(io.BytesIO(f.read()))
    new_img.save("new_image.png")
"""