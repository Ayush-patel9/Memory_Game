#importing all the needed modules for the code
from tkinter import *
import csv
import time
import random
import datetime
import tkinter.ttk as ttk
from tkinter import messagebox
import pygame


#l1-a list to store the images of the currently selcted button
l1 = []
#l2 is a list to store thebuttons that have been pressed
l2 = []
#l3 is a list to hold all the buttons that have been correctly guessed
l3 = []
#n is the counter for the no of moves taken by player to complete the game
n = 0
#here we are defining a class , which is responsible for tracking game time
class GameTimer:
    #here we are instancing the class by uskng the init function in which we are setting the elasped time as 0 and the running status to false by default
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    #in this second start function we check if the clock is not start or timer is running or not if the timer is not running it captures current time and sets runnig status as true
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    #in this stop fucntion it checks if the timer is running, if its running it captures the current time and adds it to the elasped time and sets the running status as false
    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    #it resests back the timer after the game 
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    #this fucntion gives us the elapsed time , if the timer is running it simply adds the time since start time to elapsed time, if timer is stopped it jist gives us elapsed time
    def get_elapsed_time(self):
        if self.running:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time

#this is a class which handles all the gui component and the user interface part
class UI:
    #here we initialise our class with init fucntion by creating out first window that is home page
    def __init__(self):
        #The Tk()initialises the window
        self.root = Tk()
        #here we are setting the window size to 1000x560 and its min and max size is also same 
        self.root.geometry("1000x560+150+90")
        self.root.minsize("1000", "560")
        self.root.maxsize("1000", "560")
        #here we are giving the title to our window
        self.root.title("Memory Game - Home Page")

        #here we are setting the background for that we use a label and by photo image we imported image and added it to tha label and thereby set the bg
        #actually its just a label but since the window and image size is same it is acting as background (actually is a label)
        self.bg = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\image.png")
        label2 = Label(self.root, image=self.bg)
        label2.place(x=0, y=0)

        #this is our games name label it has been given a different bg and fg colour and it is placed at the top center by pady we are setting it 75 pixel below the top 
        #of our scrren amd by ipadx and ipady we are setting internal padding that is the text will be 20 pixel away from the boundary in y axis 
        label1 = Label(self.root, text="Planetary Pairs", font="times 25 italic ", background="black", foreground="#00FF00")
        label1.pack(side="top", ipadx=50, ipady=20, pady=75)

        #here we are creating our first button that is new game button and the command  stored in it is new_game by clciking the button, the button
        #calls the new_game fucntion here expand =true allows the widget to expand and fill any extra space in parent container and fill=X allows to do so in x direction
        button1 = Button(self.root, text="New Game", font="Roboto", background="#B2E0E6", foreground="#005B5C", command=self.new_game)
        button1.pack(side="left", expand=True, fill=X, padx=100, ipadx=20, ipady=10)

        #here we are creating our second button that is view history button and the commnad stored in it is view_history
        button2 = Button(self.root, text="View History", font="Roboto", background="#B2E0E6", foreground="#005B5C", command=self.view_history)
        button2.pack(side="right", expand=True, fill=X, padx=80, ipadx=20, ipady=10)

       
        # this is the how_to_play_button which is having command show_instruction,i.e clicking this will call that fucntion
        #here we are placing the button because we want it in the middle but a little low
        #here in place if we want to add internal padding we will first set the width and height of widegt and then define the ipadx and ipady pixel amount 
        #which we want and combine them with width and height
        how_to_play_button = Button(self.root, text="How to Play", font=("Times New Roman", 14), background="#B2E0E6", foreground="#005B5C", command=self.show_instructions)
        ipadx=10
        ipady=5
        how_to_play_button.place(x=450, y=450,width=100+ipadx*2,height=50+ipady*2)

        

    #this starts the tkinter event loop and waits for user input or choice selection
    def run(self):
        self.root.mainloop()

    #this is the fucntion which is called in the how_to_play button 
    def show_instructions(self):
        #here it opens a new toplevel window for game instruction keeping the previous window and opening on it this is top level window
        instruction_window = Toplevel(self.root)
        #here we set its title and geometry of the new window and fix its size
        instruction_window.title("How to Play")
        instruction_window.geometry("800x500")
        instruction_window.minsize("800","500")
        instruction_window.maxsize("800","500")
        
        #here we import the image in which we have written the rules for how to play and place it by a label so it is shown in the page as per its size
        instruction_image = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\instruction.png")
        label = Label(instruction_window, image=instruction_image)
        label.image = instruction_image  # Keep a reference to avoid garbage collection
        label.pack()

        #here we are also keeping a close button to close this window since this is a toplevel window its command is to destroy the opened window
        close_button = Button(instruction_window, text="Close", command=instruction_window.destroy, font=("Times New Roman", 14), background="red", foreground="white")
        close_button.pack(pady=10)

    #this is the fucntion which is called when we clicked ont he button of the New Game
    def new_game(self):
        #here by global function we are making n,l1,l2,l3 accessible to this part of the code and setting n as 0 and emptying l1,l2,l3
        global n,l1,l2,l3
        n=0
        l1.clear()
        l2.clear()
        l3.clear()
        #reset the timer
        timer.reset()
        #timer calls the GameTimer class's function reset i.e reset the timer
        timer.reset()
        #it hides the main window
        self.root.withdraw()  
        #calls the function enter_name
        self.enter_name()

    #this is a function which is helpful in taking the name
    def enter_name(self):
        #it creates a new window on the hidden window root
        i2 = Toplevel(self.root)  
        #here we set the size of the new window i2 as 600x600 and also give it title
        i2.title("Memory Game - Enter Name")
        i2.geometry("600x600")
        i2.minsize("600", "600")
        i2.maxsize("600", "600")

        #here we are using the photoimage function import the png image and set it as a label but here since the size of the window and the image is same 
        #it acts as a background which we wanted to set so it is placed at 0,0
        self.bg1 = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\background2.png")
        label3 = Label(i2, image=self.bg1)
        label3.place(x=0, y=0)

        #this creates a frame with bg colour #00FF00 and bd ,frame is used to as a container to organise and group widgets here we have used it so that we 
        #show a border to our name label it is placed at a certain fixed position whcih is found by many trials
        frame = Frame(i2, bg="#00FF00", bd=1)
        frame.place(x=195, y=240)

        #the name is a label which we create inside the frame and we also give it a padx and pady which acts as the width of the border
        #this label shows us the msg to enter the name
        name = Label(frame, text="Enter your name", font=("Pacific", 20, "bold italic"), background="#E74C3C", foreground="#FFFFFF")
        name.pack(padx=1, pady=1)

        #it is a special variable class which provides us a way to manage string variables in a tkinter application here Name is the StringVar 
        #i.e. the name that the user enters is stored as a string variable in the program by it
        Name = StringVar(i2)
        #here we create a entry widget ,i.e the space where we can add the text and it has been placed at a certian place 
        e1 = Entry(i2, textvariable=Name, width=17, font=("Times New Roman", 13))
        e1.place(x=231, y=298)

        #here we define a new function z
        def submit_fun():
            #if Name.get tells is true if anything is entered that is the variable is not empty then this if statement runs
            if Name.get():
                #so if name is correct then we call another function start_game which starts our game 
                self.start_game(Name.get(), i2)
                #it deestroys the name window which was opened
                i2.destroy()
            #the other condition that is if the string is empty then this else statement's block of code runs
            else:
                #here we use the messagebox function of the tkinter to display the message to Enter the name
                messagebox.showinfo(title="Error", message="Please enter your name")
                #here we clear the entry field again
                e1.delete(0, END)  
                #focus_set selects the entry widget automatically and the cursor is on the entry widget 
                e1.focus_set()
        
        #here we are creating a new submit button and giving it a command submit_fun so clicking this button calls that function.
        submit = Button(i2, text="Submit", font=("Lobster", 17), command=submit_fun, background="yellow", foreground="#4B0082")
        submit.place(x=385, y=361)

        #here we are defining a new function go_back for back button 
        def go_back():
            #it closes the name entry window by destroy method
            i2.destroy() 
            #it calls back our home page window i.e root by deiconify method
            self.root.deiconify()

        #here we create a new back button and give it the command go_back so clicking this button will call that function
        back = Button(i2, text="Back", font=("Lobster", 17), command=go_back, background="yellow", foreground="#4B0082")
        back.place(x=143, y=361)

    #this is a function start_game it is called after we enter the non empty name and click on the submit button
    def start_game(self, player_name, name_window):
        #so it destroys the name entry window
        name_window.destroy()  

        #from the game timer class it is calling the start function as the game is strating so to start the timer of the game
        timer.start()
        #a new window is opened on the hidden window root
        i3 = Toplevel(self.root)  
        #we fix the size of our game screen as 696x696 this size is found by many trials 
        i3.geometry("696x696")
        i3.minsize("696", "696")
        i3.maxsize("696", "696")
        #we give the title to the game window as Memory Game
        i3.title("Memory Game")
        #here we change the cursor to a new style target
        i3.configure(cursor="target")

        #here we import a image bacbutton which is the image which is displayed on th back side of the button i.e whien button is not flipped
        backbutton = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\background.png")
        #here we import the images of the planets in a list Photoimage for it we have used list comprehension 
        planet_images = [PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\{}.png".format(planet)) for planet in
                         ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]]

        #here we create a new list l which is having each image twice as there are 8 pairs
        l = planet_images * 2
        #by random.shuffle we will shuffle the list
        random.shuffle(l)

        #here we are creating 16 buttons in i3 by list comprehension and giving each button the same backbutton image
        buttons = [Button(i3, image=backbutton) for _ in range(16)]

        #this is the class Memory_Game which contains the game logic 
        class Memory_Game:
            #here we are initialising the class and giving 2 things text and button here button is the hutton which will be clicked and text is image in it
            def __init__(self, button, text):
                self.text = text
                self.button = button
                pygame.init()
                self.match_sound = pygame.mixer.Sound(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\match.mp3")
            #here we are creating a new function f for the game logic and flipping
            def f(self):
                #here by global we are making l1,l2,l3 and n accessible to this class and this function
                global l1, l2, l3, n
                #here we are checking if the button is not in l2 that is the list for the selcted button
                if self.button not in l2:
                    #then we append the text that is image to l1 and the button to l2 list
                    l1.append(self.text)
                    l2.append(self.button)
                    #and we will configure the button as by showing the image on it so it is like flipping the button
                    self.button.configure(image=self.text)
                    #if the length of l2 is not equal to 0 then this code runs which means atleast one button is selected
                    if len(l2) != 0:
                        #if the length of l1 is 2 that is 2 buttons are selected then it runs the next if code of block
                        if len(l1) == 2:
                            #this calls the update_idletasks() to update the display immediately
                            self.button.update_idletasks()
                            #this introduces a delay of 0.8 seconds to allow user to see selected cards
                            time.sleep(0.8)
                            #here we check if the both the images selected are same or different ,if they are different then it runs this part
                            if l1[0] != l1[1]:
                                #so here we iterate through l2 , that is the list of buttons
                                for i in l2:
                                    #as they are diff so we change the image back to the backbutton
                                    i.configure(image=backbutton)

                                #here we clear both the lists as we need to check again as we need to choose only 2 cards at a time
                                l1.clear()
                                l2.clear()
                                #here we increment the no of move by 1
                                n += 1
                            #so the else statement will run when both images matches
                            else:
                                self.match_sound.play()
                                #so we are iterating through the list of buttons
                                for i in l2:
                                    #here we are disabling the buttons by command=labda:None so that they cant be selected again and they are kept displaying 
                                    i.configure(command=lambda: None)
                                    #here we are adding our matched buttons to the l3 which is the list to store the buttons which are matched
                                    l3.append(i)
                                #here we are again emptying the lists l1 and l2 as we need to compare only 2 cards at same time
                                l1.clear()
                                l2.clear()
                                #here we increment move by 1
                                n += 1
                #here we are checking if teh no of element in l3 is 16 that is all 16 buttons are matched then this block of code runs
                if len(l3) == 16:
                    #we are calling the game timer class function stop to stop the timer
                    timer.stop()
                    #after stopping the timer we are calling the class GameTimer function get_elapsed_time to know how much time is taken to complete
                    #the game and we store this in a variable total_time
                    total_time = timer.get_elapsed_time()
                    #now we are opening our csv file in read mode 
                    with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv","r") as A:
                        #we are making a reader for our csv files and iterate over records
                        csv_reader = csv.reader(A)
                        #instanicing 2 varibales k and w as 0
                        #k counts the no of moves
                        #w counts how many times the current score n is better than previous scores.
                        K=0
                        W=0
                        #here we are iterating through our csv
                        for i in csv_reader:
                            #incrementing k so next record comes
                            K+=1
                            #using the try execpt block to handle any kind of error
                            try:
                                #here we check if our this games score is better than previous games score
                                if n >= int(i[2]):
                                    #increments w by 1
                                    W = W + 1
                            except:
                                #if anything unusual happens we pass that part of the code and go ahead
                                pass
                    
                    #this time we are opening our csv file in the append mode 
                    with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "a") as A:
                        #incrementing our this games score in that file by formating
                        #here k 
                        A.write(f"{K},{player_name},{n},{str(datetime.timedelta(seconds=total_time))[2:7]}\n")
                    #after adding the data game has ended so we destroy that window 
                    i3.destroy()
                    #
                    Scoreboard(player_name, n, total_time).show_scoreboard()

        #here we are calling Memory_Game class by giving it each time a buttons index and a index from l 
        #now we are configuring the button and giving invoking function f for that button after we click it 
        #now we place these buttons at specific places by grid function and by sticky we control how widget stretch or align in their grid cell
        game_instance0 = Memory_Game(buttons[0], l[0])
        buttons[0].configure(command=game_instance0.f)
        buttons[0].grid(row=0, column=0, sticky=NSEW)

        game_instance1 = Memory_Game(buttons[1], l[1])
        buttons[1].configure(command=game_instance1.f)
        buttons[1].grid(row=0, column=1, sticky=NSEW)

        game_instance2 = Memory_Game(buttons[2], l[2])
        buttons[2].configure(command=game_instance2.f)
        buttons[2].grid(row=0, column=2, sticky=NSEW)

        game_instance3 = Memory_Game(buttons[3], l[3])
        buttons[3].configure(command=game_instance3.f)
        buttons[3].grid(row=0, column=3, sticky=NSEW)

        game_instance4 = Memory_Game(buttons[4], l[4])
        buttons[4].configure(command=game_instance4.f)
        buttons[4].grid(row=1, column=0, sticky=NSEW)

        game_instance5 = Memory_Game(buttons[5], l[5])
        buttons[5].configure(command=game_instance5.f)
        buttons[5].grid(row=1, column=1, sticky=NSEW)

        game_instance6 = Memory_Game(buttons[6], l[6])  
        buttons[6].configure(command=game_instance6.f)
        buttons[6].grid(row=1, column=2, sticky=NSEW)

        game_instance7 = Memory_Game(buttons[7], l[7])
        buttons[7].configure(command=game_instance7.f)
        buttons[7].grid(row=1, column=3, sticky=NSEW)

        game_instance8 = Memory_Game(buttons[8], l[8])
        buttons[8].configure(command=game_instance8.f)
        buttons[8].grid(row=2, column=0, sticky=NSEW)

        game_instance9 = Memory_Game(buttons[9], l[9])
        buttons[9].configure(command=game_instance9.f)
        buttons[9].grid(row=2, column=1, sticky=NSEW)

        game_instance10 = Memory_Game(buttons[10], l[10])
        buttons[10].configure(command=game_instance10.f)
        buttons[10].grid(row=2, column=2, sticky=NSEW)

        game_instance11 = Memory_Game(buttons[11], l[11])
        buttons[11].configure(command=game_instance11.f)
        buttons[11].grid(row=2, column=3, sticky=NSEW)

        game_instance12 = Memory_Game(buttons[12], l[12])
        buttons[12].configure(command=game_instance12.f)
        buttons[12].grid(row=3, column=0, sticky=NSEW)

        game_instance13 = Memory_Game(buttons[13], l[13])
        buttons[13].configure(command=game_instance13.f)
        buttons[13].grid(row=3, column=1, sticky=NSEW)

        game_instance14 = Memory_Game(buttons[14], l[14])
        buttons[14].configure(command=game_instance14.f)
        buttons[14].grid(row=3, column=2, sticky=NSEW)

        game_instance15 = Memory_Game(buttons[15], l[15])
        buttons[15].configure(command=game_instance15.f)
        buttons[15].grid(row=3, column=3, sticky=NSEW)

         # This starts the Tkinter main event loop for the i3 window, allowing it to respond to user interactions until it is closed
        i3.mainloop()

    #this is a functon defined for view_history
    def view_history(self):
        #this creates a new top level on the hidden root
        i5 = Toplevel(self.root)
        #this sets the background as black  
        i5.config(background="black")
        #here i am making a new label which is dispalying Scores
        s1 = Label(i5, text="Scores", font=("Comic Sans MS", 16), background="black", foreground="#00FF00")
        s1.pack(side="top")
        #here i am making a frame in which i will show the data stored in csv
        f1 = Frame(i5, height=0, background="red")
        #this frame is also added to the top of the window
        f1.pack(side="top")
        #Defines a tuple columns that specifies the headings for the Treeview
        columns = ("S.No","Name", "No.of Moves", "Time Taken")
        #This initializes a Treeview widget, setting the columns and the number of visible rows (height = 13)
        tree = ttk.Treeview(f1, columns=columns, show="headings", height=13)
        #here each column in the treeview is assigned a heading using the heading method
        tree.heading("S.No", text="S.No")
        tree.heading("Name", text="Name")
        tree.heading("No.of Moves", text="No.of Moves")
        tree.heading("Time Taken", text="Time Taken")

        #here we are opening the csv file in read mode
        with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "r") as B:
            #we are creating a reader for csv file
            csv_reader = csv.reader(B)
            #we use this to skip the reading of the header of the csv file
            next(csv_reader)
            #iterate through the csv file
            for i in csv_reader:
                #here if row is not empty then it inserts the given row values in treeview
                if len(i) != 0:
                    tree.insert("", END, values=i)

        #adds the treeview to the left side of the page with internal padding of 180
        tree.pack(side="left", ipadx=180)
        #configure the style of the scrollbar
        style = ttk.Style()
        style.configure("Vertical.TScrollbar", gripcolor="blue", background="red", troughcolor="gray", arrowcolor="white")

        #creates a vertical scrollbar for the treeview,set the scrollbar to vertical and command links it to the vertical view of the treeview
        scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=tree.yview, style="Vertical.TScrollbar")
        
        #connects the scrollbar to the treeview so that the scrolling works properly
        tree.configure(yscroll=scrollbar.set)
        #places the scrollbar on the left side of the frame
        scrollbar.pack(side="left", fill="y")

        #here we create a label below showing high score as text in it and we put it on the top after the treeview
        s2 = Label(i5, text="High Score", font="times 40", background="black", foreground="#FF10F0")
        s2.pack(side="top")
        #creates 2 empty lines M and T to hold no of counts and time
        M = []
        T = []
        #here we are again opening the csv file in read mode
        with open(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\record.csv", "r") as B:
            #we are creating its reader
            csv_reader = csv.reader(B)
            #we skip the first line that is heading of the  csv file
            next(csv_reader)
            #we iterate through rest of the rows
            for i in csv_reader:
                #we append the no of moves after converting it to integer
                M.append(int(i[2]))
                #we append the time taken as string in T
                T.append(i[3])

            #we create a new label which tells us the least no of move and least time taken we can get the min of both the list
            s3 = Label(i5, text=f"Least No. of Moves Achieved : {min(M)}\n Least Time Taken : {min(T)}", font="times 25", background="black", foreground="#00FF00")
            s3.pack()

            #we create a back button to get back to the home page
            bb = Button(i5, text="Back", font="times 25", command=i5.destroy, background="black", foreground="#FF073A")
            bb.pack()

#here we are creating a new class Scoreboard which handles all the file 
class Scoreboard:
    #This is the constructor method that initializes a new instance of the Scoreboard class. It takes three parameters: name, moves, and time_taken.
    def __init__(self, name, moves, time_taken):
        self.name = name
        self.moves = moves
        self.time_taken = time_taken
        #here we are initialsiing the pygame
        pygame.init()
        #we are importing the game sound which we want to use
        self.victory_sound = pygame.mixer.Sound(r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\congo.mp3")
    #here we create a new function show_scoreboard to display the scoreboard
    def show_scoreboard(self):
        #here we create a new window on the previous window that is root
        i4 = Toplevel()  
        #we set the size of this window and this is found by trials
        i4.geometry("630x350")
        i4.minsize("630", "350")
        i4.maxsize("630", "350")
        #we have aslo given title to our window to make it lookm asethetic
        i4.title("Exit:Space Traveler's Departure")
        #now we are importing a image by PhotoImage and using it as bg as image and window size is same so this label becomes bg
        bg3 = PhotoImage(file=r"C:\Users\patel\Downloads\keyur-20241017T192053Z-001\keyur\1234.png")
        label2 = Label(i4, image=bg3)
        label2.place(x=0, y=0)

        #this is a label created which congratulates the player after completion of game 
        p1 = Label(i4, text="Well Done!\nSpace Explorer!", font=("Times New Roman", 25), bg="#001F3F", fg="#FF007F")
        p1.place(x=220, y=5)
        #This creates a label (p2) that displays the player's score, number of moves taken, and time taken formatted as a string.
        p2 = Label(i4, text=f"Score\n Number of moves taken : {self.moves}\n Time taken : {str(datetime.timedelta(seconds=self.time_taken))[2:7]}",
                   font="times 15", bg="#73FE1F", fg="#001F3F")
        #now we place the label below the congratulation label
        p2.place(x=210, y=95)

        #here we are playing the sound when the screen is opened.
        self.victory_sound.play()
        #we are creating a new label replay 
        def replay():
            #making the varibale global so that we can access them here and making n zero and emptying the list and restting the timer
            global n,l1,l2,l3
            n=0
            l1.clear()
            l2.clear()
            l3.clear()
            timer.reset()
            #so when we call this function it destroys the window
            i4.destroy()
            #ui.new_game will open the game again
            ui.new_game()

        #we are adding a new button in this and giving it the command replay so that we get back again to game 
        c1 = Button(i4, text="Replay", font="times 20", bg="#73FE1F", fg="#001F3F", command=replay)
        c1.place(x=100, y=230)

        #here we have created a new fucntion home to get back to home page
        def home():
            #it destroys the exit window
            i4.destroy()  
            #it displays us the root that is home page again as it was hidden
            ui.root.deiconify()  

        #here we are creating a new button Home which is given command home to get back to main home page
        c2 = Button(i4, text="Home", font="times 20", bg="#73FE1F", fg="#001F3F", command=home)
        c2.place(x=457, y=230)
        
        # This starts the Tkinter main event loop for the i4 window, allowing it to respond to user interactions until it is closed.
        i4.mainloop()

# Initialize the game timer
timer = GameTimer()

# Initialize and run the UI
ui = UI()
ui.run()