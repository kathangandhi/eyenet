from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from PIL import ImageTk
import feature_extraction
import training
import prediction

# initializes window
window = Tk()
window.title("EyeNet")  # sets window name to EyeNet
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))  # makes window full screen
window.configure(bg="#AFD7FA")  # background color is light blue

# initializes secondary window
tool = Toplevel()
tool.title("Tool Window")  # sets window name to Tool Window
tool.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))  # makes window full screen
tool.configure(bg="#AFD7FA")  # background color is light blue
tool.withdraw()

# inserts main runner frame
frame = Frame(tool, width=870, height=250)
frame.place(relx=0.21, rely=0.6)

feature_extraction.extract(Path("retinopathy-dataset-master"))
training.train()

# global functions
def open_file():
    filename = filedialog.askopenfilename(filetypes=(("PNG Images", "*.png"), ("JPEG Images", "*.jpeg"), ("JPG Images", "*.jpg")))
    if(filename == ""):
        messagebox.askretrycancel("Unexpected Error", "Please choose a PNG or JPEG or JPG image")
    else:
        str = prediction.predict(filename)

        output = Label(frame, text=str, bg="#E13A44", fg="#FFFFFF", font=("Calibri", 18), wraplength=425, justify=LEFT)
        output.place(relx=0.5, rely=0.5)

def back():
    window.deiconify()
    tool.withdraw()

def next_window():
    if(chk_state.get()):
        global p, img
        window.withdraw()
        tool.deiconify()

        # inserts title of the screen
        title = Label(tool, text="Tool Description", bg="#AFD7FA", fg="#0F5CA0", font=("Calibri", 48))  # background - light blue, foreground - darkblue, font - Calibri 48 pt
        title.anchor(CENTER)  # text is center aligned
        title.place(relx=0.36, rely=0.025)  # places header on screen

        # inserts logo image
        p = Path("gui") / "logo.png"  # represents file location
        img = ImageTk.PhotoImage(file=p)  # image loaded from source file
        logo_pic = Label(tool, image=img)  # image is put inside container
        logo_pic.place(relx=0.9, rely=0.02)  # places container on screen

        # inserts project description
        s = "EyeNet is a Convolutional Neural Network based algorithm that determines the likelihood of diabetes within users based on " \
            "retinoscope images (any format). The algorithm relies on hundreds of training images in order to make its prediction and " \
            "is shown to be about 75% accurate on average.\n\n" \
            "Note:\nImages should be as clear as possible (well-lit, good resolution, etc.) for maximum performance."
        tool_desc = Label(tool, text=s, bg="#E13A44", fg="#FFFFFF", font=("Calibri", 16), justify=LEFT, wraplength=900)  # background - red, foreground - white, font - Calibri 14 pt, label length - 1000 px
        tool_desc.place(relx=0.21, rely=0.2)  # places description on screen

        # inserts choose image button
        choose_image = Button(frame, text="Choose Image", bg="#E13A44", fg="#FFFFFF", command=lambda: open_file(), height=5, width=20)
        choose_image.place(relx=0.1, rely=0.35)

        # inserts runner instructions
        ins = "Click the 'Choose Image' button and pick an appropriate image. The image will be processed and the algorithm will run on it. The results " \
              "will be displayed in the console output"
        instructions = Label(frame, text=ins, bg="#AFD7FA", fg="#0F5CA0", font=("Calibri", 12), justify=LEFT, wraplength=425)
        instructions.place(relx=0.5, rely=0.05)

        # inserts back button
        leave = Button(tool, text="Back", bg="#0F5CA0", fg="#FFFFFF", font=("Calibri", 12), command=back)  # background - dark blue, foreground - white, font Calibri 12 pt
        leave.place(relx=0.05, rely=0.9)

        # inserts done button
        finish = Button(tool, text="Done", bg="#0F5CA0", fg="#FFFFFF", font=("Calibri", 12), command=window.quit)  # background - dark blue, foreground - white, font Calibri 12 pt
        finish.place(relx=0.95, rely=0.9)
    else:
        messagebox.askretrycancel("Unexpected Error", "Please click check box before clicking next")

# inserts header of the screen
header = Label(window, text="Welcome to EyeNet", bg="#AFD7FA", fg="#0F5CA0", font=("Calibri", 48))  # background - light blue, foreground - darkblue, font - Calibri 48 pt
header.anchor(CENTER)  # text is center aligned
header.place(relx=0.35, rely=0.0)  # places header on screen

# inserts logo image
path = Path("gui") / "logo.png"  # represents file location
image = ImageTk.PhotoImage(file=path)  # image loaded from source file
logo = Label(window, image=image)  # image is put inside container
logo.place(relx=0.9, rely=0.02)  # places container on screen

# inserts scrollable text biography section
bio = scrolledtext.ScrolledText(window, width=125, height=15, wrap=WORD)  # creates scrollable text box
bio.insert(INSERT, "Hello User,\n\n"
                   "Hi, I am Kathan Gandhi, the creator of this application (EyeNet). I am currently a senior at Liberty High School. "
                   "Ever since I took computer science in high school, I have become very invested in programming and "
                   "digital technologies. I have gained a lot of experience in Java and C# through my high school courses.\n\n"
                   "Yet, for ISM, I decided to explore artificial intelligence (AI). My interest in AI grew over last summer when "
                   "I undertook Stanford's online machine learning course. Within the course, I learned a variety of techniques. "
                   "I'm sure many of you have heard about linear regression, since it is an introductory concept in AI. I wanted "
                   "to expand my expertise, so I pursued image analysis when I was researching in ISM. With the assistance of my "
                   "mentor, I eventually decided to implement the program that you are currently operating. This seemed very "
                   "unrealistic when I started out, but I am excited about the way it turned out and I hope you like it too. "
                   "After searching Google, learning from more online courses, and getting used to Python, I was finally able to "
                   "implement my algorithm and create this GUI. My product has helped me realize the potential an individual has "
                   "to create change and I will continue working on new initiatives even in the future. \n\n"
                   "This algorithm embodies my technical knowledge but also my good intentions and commitment to make a difference "
                   "in society. I dedicate my product to my grandmother who is afflicted with diabetes, my mentor who gave me the "
                   "idea and helped me throughout my ISM experience, and medical practitioners around the world who work very hard "
                   "to keep everyone healthy.\n\n"
                   "Respectfully,\n"
                   "Kathan Gandhi")
bio.place(relx=0.05, rely=0.2)  # places text box on screen

# inserts profile image
path2 = Path("gui") / "profile.png"  # represents file location
image2 = PhotoImage(file=path2)  # loads image from source file
profile = Label(window, image=image2)  # image is put inside container
profile.place(relx=0.85, rely=0.2)  # places container on screen

# inserts project description
str = "This program intends to help health-care and associated personnel. The program conducts image analysis automatically on a data set " \
      "of retinoscope images. The knowledge learned from the analysis is then utilized to make predictions about the likelihood of diabetes " \
      "in patients. The entire application is made with Python and several of its libraries - keras, joblib, Path, tkinter, numpy, etc.\n\n" \
      "Note:\nNone of the user's data is stored by the application. All files will remain in local environment and data integrity will " \
      "be maintained."
desc = Label(window, text=str, bg="#E13A44", fg="#FFFFFF", font=("Calibri", 16), justify=LEFT, wraplength=1025)  # background - red, foreground - white, font - Calibri 14 pt, label length - 1000 px
desc.place(relx=0.05, rely=0.55)  # places description on screen

# inserts user confirmation
chk_state = BooleanVar()
chk_state.set(False)  # set check state
chk = Checkbutton(window, text="I understand all expectations", var=chk_state)  # check box is set to false by default
chk.place(relx=0.45, rely=0.85)  # places check box on screen

# inserts quit button
quit = Button(window, text="Quit", bg="#0F5CA0", fg="#FFFFFF", font=("Calibri", 12), command=window.quit)  # background - dark blue, foreground - white, font Calibri 12 pt
quit.place(relx=0.05, rely=0.9)

# inserts next button
next = Button(window, text="Next", bg="#0F5CA0", fg="#FFFFFF", font=("Calibri", 12), command=next_window)
next.place(relx=0.95, rely=0.9)

window.mainloop()