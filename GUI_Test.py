import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.messagebox
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk
from customtkinter import CTkImage  # Import CTkImage


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # Triggers
        image_select = False
        hide_text = False
        hide_image = False
        hide_exe = False

        # configure window
        self.title("LSB Steganographer")
        self.geometry(f"{1100}x{420}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="LSB Steganographer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Select an Image")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.return_home_event, text="Return to Menu")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your secret text...")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Inject to Image")
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create imagebox -- where i want to place image
        #self.textbox = customtkinter.CTkTextbox(self, width=250)
        #self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Select What to Hide:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, command=self.hide_text_event, value=0, text="Hide Text")
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, command=self.hide_image_event,value=1, text="Hide Image")
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, command=self.hide_exe_event,value=2, text="Hide Executable")
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Text")
        self.tabview.add("Image")
        self.tabview.add("Exe")
        self.tabview.tab("Text").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Image").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Text"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Text"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Text"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Image"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.info_label = customtkinter.CTkLabel(self, text="Status Information Here", height=30)
        self.info_label.grid(row=0, column=1, padx=(20, 0), pady=(400, 0), sticky="nsew")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.display_image(file_path)

    def return_home_event(self):
        print("Return home click")

    def hide_text_event(self):
        print("Text Hide Selected!")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Image"))
        # Do stuff

    def hide_image_event(self):
        print("Image Hide Selected!")
        # Do stuff

    def hide_exe_event(self):
        print("Executable Hide Selected")
        # Do stuff

    
        

    def display_image(self, file_path):
        # Load and display the image
        image = Image.open(file_path)

        # Resize image while maintaining aspect ratio
        base_width = 500
        w_percent = (base_width / float(image.size[0]))
        h_size = int((float(image.size[1]) * float(w_percent)))
        image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)

        photo = ImageTk.PhotoImage(image)

        # Update or create the image label
        if hasattr(self, 'image_label'):
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Update the reference
        else:
            self.image_label = customtkinter.CTkLabel(self, image=photo, text="")
            self.image_label.image = photo  # Keep a reference
            self.image_label.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
            image_select = True
            print("Image select status: " + str(image_select))
            

        def on_resize(self, event):
            # Check if image_label and image are available
            if hasattr(self, 'image_label') and hasattr(self.image_label, 'image'):
                # Resize the image based on the new window size
                new_width = self.image_label.winfo_width()
                new_height = self.image_label.winfo_height()

                # Resize and display the image
                image = Image.open(file_path)  # You need to store 'file_path' as an instance variable
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=photo)
                self.image_label.image = photo




if __name__ == "__main__":
    app = App()
    app.mainloop()