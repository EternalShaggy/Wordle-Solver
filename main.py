from tkinter import PhotoImage, StringVar, Label, Text, Button, END, Tk
from random import choice

"""
Created by: Dagmawi Yimam 
Github Profile Link: https://github.com/EternalShaggy

The following program is a Wordle Solver that allows a user to solve a Wordle puzzle by using a sorting algorithm 
on a text file containing every 5 letter word in the Enlglish Dictionary. 

Instructions: Video
"""

#This class contains the main and only window in which the tkinter program will run in.
class Wordle_Help():
    def __init__(self, root):

        self.root = root
        self.root.geometry("700x400")
        self.root.resizable(False, False)
        self.root.title("Wordle Help")

        self.root.configure(bg="#6fc7c9")

    #The "guesses" attribute holds the number of guesses the user has left
        self.guesses = 6
    #The "previous" attribute holds the users previous wordle guess
        self.previous = ""

        self.header = Label(self.root, text="WORDLE HELPER", bg="#6fc7c9", font=("Comic Sans MS", 20, "bold"), fg="#373d82")
        self.header.place(x=230,y=3)

        self.textbox1 = Text(self.root, width=8, height=1, font=("Comic Sans MS", 20, "bold"), bg="#b2eced")
        self.textbox1.place(x=280, y=50)
        
    #The following lines create Tkinter String Variables to hold the color values of the 5 squares. 
    #They are originally all set to grey
        self.square1val = StringVar()
        self.square1val.set("Grey")
        self.square2val = StringVar()
        self.square2val.set("Grey")
        self.square3val = StringVar()
        self.square3val.set("Grey")
        self.square4val = StringVar()
        self.square4val.set("Grey")
        self.square5val = StringVar()
        self.square5val.set("Grey")

    #The square1-5 labels are the square objects that display the state of the square1-5 values.
        self.square1 = Label(self.root, bg="grey", height=3, width=6)
        self.square1.place(x=225,y=100)

        self.square2 = Label(self.root, bg="grey", height=3, width=6)
        self.square2.place(x=275,y=100)

        self.square3 = Label(self.root, bg="grey", height=3, width=6)
        self.square3.place(x=325,y=100)

        self.square4 = Label(self.root, bg="grey", height=3, width=6)
        self.square4.place(x=375,y=100)

        self.square5 = Label(self.root, bg="grey", height=3, width=6)
        self.square5.place(x=425,y=100)

    #This button sets all the squares back to their default color, grey.
        self.color_reset = Button(self.root, text="Cls", height=2,width=5, command=self.reset_color, bg="#81abdb", border=0)
        self.color_reset.place(x=170, y=125)

    #The following buttons change the color value of their corresponding square. E.G "button1y" sets square1 to yellow.
        self.button1n = Button(self.root, text="n", height=1, width=1, bg="grey", command=lambda: self.change_square1("Grey"))
        self.button1y = Button(self.root, text="y", height=1, width=1, bg="yellow", command=lambda: self.change_square1("Yellow"))
        self.button1g = Button(self.root, text="g", height=1, width=1, bg="green", command=lambda: self.change_square1("Green"))

        self.button1n.place(x=225,y=150)
        self.button1y.place(x=240,y=150)
        self.button1g.place(x=255,y=150)

        self.button2n = Button(self.root, text="n", height=1, width=1, bg="grey", command=lambda: self.change_square2("Grey"))
        self.button2y = Button(self.root, text="y", height=1, width=1, bg="yellow", command=lambda: self.change_square2("Yellow"))
        self.button2g = Button(self.root, text="g", height=1, width=1, bg="green", command=lambda: self.change_square2("Green"))

        self.button2n.place(x=275,y=150)
        self.button2y.place(x=290,y=150)
        self.button2g.place(x=305,y=150)
        
        self.button3n = Button(self.root, text="n", height=1, width=1, bg="grey", command=lambda: self.change_square3("Grey"))
        self.button3y = Button(self.root, text="y", height=1, width=1, bg="yellow", command=lambda: self.change_square3("Yellow"))
        self.button3g = Button(self.root, text="g", height=1, width=1, bg="green", command=lambda: self.change_square3("Green"))

        self.button3n.place(x=325,y=150)
        self.button3y.place(x=340,y=150)
        self.button3g.place(x=355,y=150)

        self.button4n = Button(self.root, text="n", height=1, width=1, bg="grey", command=lambda: self.change_square4("Grey"))
        self.button4y = Button(self.root, text="y", height=1, width=1, bg="yellow", command=lambda: self.change_square4("Yellow"))
        self.button4g = Button(self.root, text="g", height=1, width=1, bg="green", command=lambda: self.change_square4("Green"))

        self.button4n.place(x=375,y=150)
        self.button4y.place(x=390,y=150)
        self.button4g.place(x=405,y=150)
        
        self.button5n = Button(self.root, text="n", height=1, width=1, bg="grey", command=lambda: self.change_square5("Grey"))
        self.button5y = Button(self.root, text="y", height=1, width=1, bg="yellow", command=lambda: self.change_square5("Yellow"))
        self.button5g = Button(self.root, text="g", height=1, width=1, bg="green", command=lambda: self.change_square5("Green"))

        self.button5n.place(x=425,y=150)
        self.button5y.place(x=440,y=150)
        self.button5g.place(x=455,y=150)


        self.filter = Button(self.root, text="FILTER", command=self.main, bg="#81abdb", width=7, height=2, border=0)
        self.filter.place(x=100,y=220)

        self.random = Button(self.root, text="RANDOM", command=self.ran, bg="#81abdb", width=7, height=2, border=0)
        self.random.place(x=100, y=270)

        self.reset = Button(self.root, text="RESET", command=self.reset, bg="#81abdb", width=7, height=2, border=0)
        self.reset.place(x=100,y=320)

        self.rectextbox = Text(self.root, width=50,height=10, bg="#b2eced", border=0)
        self.rectextbox.place(x=185,y=210)

    
    """This function uses a character array generated from the self.charr_array to filter through the main.txt file containing all the text files.  
    The array generated must meet length and repetition requirements. The function then writes a randomly generated list of 5 words from the main.txt file to reccomend to the user to the dialog box.
    """
    def main(self):
        wordl = self.char_array()
        if not (len(wordl)==5):
            self.write_rectextbox("Please make sure you enter a 5 letter word!")
            return 0
        if(wordl==self.previous):
            self.write_rectextbox("You already tried that guess earlier. You have {self.guesses} guesses left!")
            return 0
        

        colorl = self.color_key()
        text = self.read_text()
        text = self.filterfunc(text, wordl, colorl)
        self.write_text("\n".join(text))
        
        num = len(text)
        if(num>=5):
            temp = self.ran(text)
            s=f"There are {num} words left that are possible\nWe've selected 5 randomly below.\nPress random to retrieve another 5 words at random\n"+f"1.{temp[0]}\n2.{temp[1]}\n3.{temp[2]}\n4.{temp[3]}\n5.{temp[4]}"
        else:
            s=f"There are only {num} words that are possible\nWe've displayed them below.\n"+"\n".join([f"{i+1}."+text[i] for i in range(num)])


        self.write_rectextbox(s)
        self.guesses-=1
        return 0


    """The following functions filters the text list fed to it by using the wordle rules, and the two arrays fed to it and returns the filtered test list.
    E.G If the word list ['D', 'R', 'E', 'A', 'M'] and the color array list ["Green", "Grey", "Grey", "Grey", "Grey"] are passed through the function, all the words not starting with the letter D will be removed from the sauce list.
    """
    def filterfunc(self, text, warray, carray):
        sauce = text
        for i in range(5):
            if(carray[i][0:-1]=="Grey"):
                if(warray.count(warray[i])==1):
                    sauce = self.none_remover(sauce, warray[i])
                else:
                    sauce = self.yellow_remover(sauce, i, warray[i])
            elif(carray[i][0:-1]=="Green"):
                sauce = self.green_remover(sauce, i, warray[i])
            elif(carray[i][0:-1]=="Yellow"):
                sauce = self.yellow_remover(sauce, i, warray[i])
        return sauce

    #Removes all words in a list that contain the forbidden character passed through it.
    def none_remover(self, lis, char):
        l=[]
        for i in lis:
            if (char not in i):
                l.append(i)
        return l


    def green_remover(self, lis, index, char):
        l=[]
        for i in lis:
            if(i[index]==char):
                l.append(i)
        return l

    def yellow_remover(self, lis, index, char):
        l=[]
        for i in lis:
            if (char in i) and (i[index]!=char):
                l.append(i)
        return l
    
    def ran(self, lis):
        l=[]
        num=len(lis)
        if(num>5):
            for i in range(5):
                l.append(choice(lis))
            return l
        elif(num==5):
            return lis
        
        elif(num<5 and num>1):
            return l[0:num-1]+["NA" for i in range(5-num)]
        else:
            return ["NA" for i in range(5)]

    def reset(self):
        self.guesses = 6

        self.change_square1("Grey")
        self.change_square2("Grey")
        self.change_square3("Grey")
        self.change_square4("Grey")
        self.change_square5("Grey")

        self.textbox1.delete("1.0", END)
        self.rectextbox.delete("1.0", END)

        file = open("manip.txt","r+")
        file.truncate(0)
        file.close()

#This function resets all the square1-5 attributes back to their default if they are not Green.
    def reset_color(self):
        if(self.square1val.get()!="Green"):
            self.change_square1("Grey")
        if(self.square2val.get()!="Green"):
            self.change_square2("Grey") 
        if(self.square3val.get()!="Green"):
            self.change_square3("Grey") 
        if(self.square4val.get()!="Green"):
            self.change_square4("Grey") 
        if(self.square5val.get()!="Green"):
            self.change_square5("Grey")  
            

    def write_text(self, text):
        with open("manip.txt", "w") as f:
            f.write(text)
        f.close()

    def read_text(self):
        if(self.guesses==6):
            with open("main.txt", 'r') as f:
                text = f.readlines()
            f.close()
            return [i.strip() for i in text]
        else:
            with open("manip.txt", 'r') as f:
                text = f.readlines()
            f.close()
            return [i.strip() for i in text]

    #The following functions generates a character array containing the values of the textboxes containing a single character. The array generated looks like ()
    def char_array(self):
        return [i for i in self.textbox1.get("1.0",END).strip()]

    #The following function generates a character array using the field values of the drop down menus. The index of each value is stored at the end of each element
    def color_key(self):
        return [self.square1val.get()+"0", self.square2val.get()+"1", self.square3val.get()+"2", self.square4val.get()+"3", self.square5val.get()+"5"]

    def write_rectextbox(self, text):
        self.rectextbox.delete("1.0", END)
        self.rectextbox.insert("1.0", text)
    
    def change_square1(self, color):
        self.square1.configure(bg=color)
        self.square1val.set(color)
        
    def change_square2(self, color):
        self.square2.configure(bg=color)
        self.square2val.set(color)
    
    def change_square3(self, color):
        self.square3.configure(bg=color)
        self.square3val.set(color)
    
    def change_square4(self, color):
        self.square4.configure(bg=color)
        self.square4val.set(color)
    
    def change_square5(self, color):
        self.square5.configure(bg=color)
        self.square5val.set(color)
            
window = Tk()
Wordle_Help(window)
window.mainloop()

