#Ui
from tkinter import *
import random
import tkinter.ttk as ttk
from tkinter import messagebox
def __init__(self):
    self.root = Tk()
    self.root.geometry("1000x560+150+90")
    self.root.minsize("1000", "560")
    self.root.maxsize("1000", "560")
    self.root.title("Memory Game - Home Page")

    self.bg = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\image.png")
    label2 = Label(self.root, image=self.bg)
    label2.place(x=0, y=0)

    label1 = Label(self.root, text="Planetary Pairs", font="times 25 italic ", background="black", foreground="#00FF00")
    label1.pack(side="top", ipadx=50, ipady=20, pady=75)

    button1 = Button(self.root, text="New Game", font="Roboto", background="#B2E0E6", foreground="#005B5C", command=self.new_game)
    button1.pack(side="left", expand=True, fill=X, padx=100, ipadx=20, ipady=10)

    button2 = Button(self.root, text="View History", font="Roboto", background="#B2E0E6", foreground="#005B5C", command=self.view_history)
    button2.pack(side="right", expand=True, fill=X, padx=80, ipadx=20, ipady=10)

    how_to_play_button = Button(self.root, text="How to Play", font=("Times New Roman", 14), background="#B2E0E6", foreground="#005B5C", command=self.show_instructions)
    ipadx = 10
    ipady = 5
    how_to_play_button.place(x=450, y=450, width=100 + ipadx * 2, height=50 + ipady * 2)

def run(self):
    self.root.mainloop()

def show_instructions(self):
    instruction_window = Toplevel(self.root)
    instruction_window.title("How to Play")
    instruction_window.geometry("800x500")
    instruction_window.minsize("800", "500")
    instruction_window.maxsize("800", "500")

    instruction_image = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\instruction.png")
    label = Label(instruction_window, image=instruction_image)
    label.image = instruction_image
    label.pack()

    close_button = Button(instruction_window, text="Close", command=instruction_window.destroy, font=("Times New Roman", 14), background="red", foreground="white")
    close_button.pack(pady=10)

def new_game(self):
    global n, l1, l2, l3
    n = 0
    l1.clear()
    l2.clear()
    l3.clear()
    timer.reset()
    self.root.withdraw()
    self.enter_name()

def enter_name(self):
    i2 = Toplevel(self.root)
    i2.title("Memory Game - Enter Name")
    i2.geometry("600x600")
    i2.minsize("600", "600")
    i2.maxsize("600", "600")

    self.bg1 = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\background2.png")
    label3 = Label(i2, image=self.bg1)
    label3.place(x=0, y=0)

    frame = Frame(i2, bg="#00FF00", bd=1)
    frame.place(x=195, y=240)

    name = Label(frame, text="Enter your name", font=("Pacific", 20, "bold italic"), background="#E74C3C", foreground="#FFFFFF")
    name.pack(padx=1, pady=1)

    Name = StringVar(i2)
    e1 = Entry(i2, textvariable=Name, width=17, font=("Times New Roman", 13))
    e1.place(x=231, y=298)

    def submit_fun():
        if Name.get():
            self.start_game(Name.get(), i2)
            i2.destroy()
        else:
            messagebox.showinfo(title="Error", message="Please enter your name")
            e1.delete(0, END)
            e1.focus_set()

    submit = Button(i2, text="Submit", font=("Lobster", 17), command=submit_fun, background="yellow", foreground="#4B0082")
    submit.place(x=385, y=361)

    def go_back():
        i2.destroy()
        self.root.deiconify()

    back = Button(i2, text="Back", font=("Lobster", 17), command=go_back, background="yellow", foreground="#4B0082")
    back.place(x=143, y=361)

def start_game(self, player_name, name_window):
    name_window.destroy()
    timer.start()
    i3 = Toplevel(self.root)
    i3.geometry("696x696")
    i3.minsize("696", "696")
    i3.maxsize("696", "696")
    i3.title("Memory Game")
    i3.configure(cursor="target")

    backbutton = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\background.png")
    planet_images = [PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\{}.png".format(planet)) for planet in
                     ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]]

    l = planet_images * 2
    random.shuffle(l)

    buttons = [Button(i3, image=backbutton) for _ in range(16)]
    def show_instructions(self):
    instruction_window = Toplevel(self.root)
    instruction_window.title("How to Play")
    instruction_window.geometry("800x500")
    instruction_window.minsize("800", "500")
    instruction_window.maxsize("800", "500")

    instruction_image = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\instruction.png")
    label = Label(instruction_window, image=instruction_image)
    label.image = instruction_image
    label.pack()

    close_button = Button(instruction_window, text="Close", command=instruction_window.destroy, font=("Times New Roman", 14), background="red", foreground="white")
    close_button.pack(pady=10)

