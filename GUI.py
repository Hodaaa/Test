from Tkinter import *
from PIL import Image, ImageTk
from play import run

buttons =''

class GUI:
    background = None

    def __init__(self, root):
        self.root = root
        root.title("Reversi Game")
        root.configure(background="#CFFFBF")

        self.background_image = PhotoImage(file="Media/Background.png")
        self.txt = """REVERSI GAME"""

        self.background = Button(root, compound=CENTER, text=self.txt, fg="#FF8200", font="Helvetica 50 bold",
                                 image=self.background_image)
        self.background.pack()

        self.remaining = 0
        self.countdown(2.5)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.openFrame()
        else:
            self.remaining = self.remaining - 1
            self.root.after(1000, self.countdown)

    def openFrame(self):
        if self.background:
            self.background.destroy()
            self.MenuPage = MenuPage(self.root)
        else:
            print("ERROR !!!!!!!!!!!!!   Can't Destroy Image")

class MenuPage:
    def __init__(self, root):
        self.root = root

        self.small1 = ImageTk.PhotoImage(Image.open('Media/5.jpg'))
        self.label1 = Label(root, image=self.small1)
        self.label1.place(x=20, y=20)

        self.small2 = ImageTk.PhotoImage(Image.open('Media/00.jpg'))
        self.label2 = Label(root, image=self.small2)
        self.label2.place(x=40, y=160)

        self.small3 = ImageTk.PhotoImage(Image.open('Media/7.jpg'))
        self.label3 = Label(root, image=self.small3)
        self.label3.place(x=160, y=50)

        self.small4 = ImageTk.PhotoImage(Image.open('Media/5.jpg'))
        self.label4 = Label(root, image=self.small4)
        self.label4.place(x=1200, y=595)

        self.small5 = ImageTk.PhotoImage(Image.open('Media/00.jpg'))
        self.label5 = Label(root, image=self.small5)
        self.label5.place(x=920, y=595)

        self.small6 = ImageTk.PhotoImage(Image.open('Media/7.jpg'))
        self.label6 = Label(root, image=self.small6)
        self.label6.place(x=1030, y=470)

        self.a = Button(root, text="START", fg="#134611", font="Helvetica 20 bold", bg="#F9E8B1", padx=80, pady=8,
                        command=lambda: [self.hide(), PlayPage(self.root)])
        self.a.place(x=580, y=100)

        self.b = Button(root, text="HELP", font="Helvetica 20 bold", padx=90, pady=8,
                        command=lambda: [self.hide(), HelpPage(self.root)])
        self.b.place(x=580, y=180)

        self.c = Button(root, text="ABOUT US", fg="#134611", font="Helvetica 20 bold", bg="#F9E8B1", padx=55, pady=8,
                        command=lambda: [self.hide(), AboutPage(self.root)])
        self.c.place(x=580, y=260)

        self.d = Button(root, text="EXIT", font="Helvetica 20 bold", padx=95, pady=8, command=root.destroy)
        self.d.place(x=580, y=340)

    def hide(self):
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()
        self.label5.place_forget()
        self.label6.place_forget()
        self.a.destroy()
        self.b.destroy()
        self.c.destroy()
        self.d.destroy()

class PlayPage:

    def UPDATE_GUI(self , state , states):
        '''DO FLIPPING HERE'''
        self.state  = ''
        self.states = ''

    def getText(self,text):
        index = text.split(",")
        i = int(index[0])
        j = int(index[1])
        self.state , self.states = run(i , j)
        self.UPDATE_GUI(self.state, self.states)

    def __init__(self, root):
        self.state = ''
        self.states = ''
        self.root = root
        self.black = PhotoImage(file="Media/2.gif")
        self.white = PhotoImage(file="Media/3.gif")
        self.Empty = PhotoImage(file="Media/E.gif")
        self.height = 8
        self.width = 8
        buttons = [[0 for x in range(self.height)] for y in range(self.width)]

        for i in range(14):
            Label(width=5, height=2, bg="#CFFFBF", activebackground="#CFFFBF").grid(row=i, column=i)
        for i in range(self.height):  # Rows
            for j in range(self.width):  # Columns
                buttons[i][j] = Button(root, image=self.Empty, relief=FLAT, height=40, width=40, bg="#75af66" , text = str(i) + "," + str(j))
                buttons[i][j].grid(row=i + 1, column=j + 14)
                buttons[i][j].configure(command=lambda t = str(i) + "," + str(j),: self.getText(t))

        buttons[3][3].configure(image=self.black)
        buttons[4][4].configure(image=self.black)
        buttons[3][4].configure(image=self.white)
        buttons[4][3].configure(image=self.white)

        self.btn = Button(self.root, text="Back To Menu", fg="#134611", font="Helvetica 20 bold", bg="#F9E8B1", padx=30,
                          pady=10, command=lambda: [self.hide2(), MenuPage(self.root)])
        self.btn.place(x=40, y=600)

        self.player = Label(self.root, image=self.black)
        self.player.place(x=555, y=515)
        self.root.wintxt1 = Label(self.root, text="YOU ", fg="#44241A", bg="#E2D8BF", font="Helvetica 15 bold", padx=10,
                                  pady=25)
        self.root.wintxt1.place(x=540, y=425)
        self.root.wintxt2 = Label(self.root, text="Total : 0 ", bg="#E2D8BF", font="Helvetica 15 bold", padx=10,
                                  pady=25)
        self.root.wintxt2.place(x=540, y=565)

        self.player2 = Label(self.root, image=self.white)
        self.player2.place(x=810, y=515)
        self.root.wintxt3 = Label(self.root, text="COMPUTER ", bg="#E2D8BF", fg="#C26D1A", font="Helvetica 15 bold",
                                  padx=10, pady=25)
        self.root.wintxt3.place(x=770, y=425)
        self.root.wintxt4 = Label(self.root, text="Total : 0 ", bg="#E2D8BF", font="Helvetica 15 bold", padx=10,
                                  pady=25)
        self.root.wintxt4.place(x=790, y=565)

    def hide2(self):
        self.btn.place_forget()
        self.player.destroy()
        self.player2.destroy()
        self.root.wintxt1.destroy()
        self.root.wintxt2.destroy()
        self.root.wintxt3.destroy()
        self.root.wintxt4.destroy()
        for i in range(self.height):  # Rows
            for j in range(self.width):  # Columns
                self.buttons[i][j].grid_forget()

class HelpPage:
    def __init__(self, root):
        self.root = root

        self.root.img1 = ImageTk.PhotoImage(Image.open('Media/13.jpg'))
        self.root.panel = Label(self.root, image=self.root.img1)
        self.root.panel.place(x=1100, y=500)

        self.help1 = """
                   Instruction To Play Reversi Game

                   Each reversi piece has a white side and a black side.
                   You play the black pieces and the computer plays the white pieces.
                   On your turn, you place one black piece on the board.
                   You must place the piece so that a white piece is flanked by your pieces.
                   All of the white pieces between your pieces are then turned over to become black.
                   In its turn, the computer plays in the manner with the white pieces.
                   The game ends when there are no more legal moves and the winner is the player that have more pieces on the board.
                 """
        self.root.textt = Label(self.root, text=self.help1, font="Helvetica 15 bold", bg="#CFFFBF")
        self.root.textt.place(x=50, y=100)

        self.root.img2 = ImageTk.PhotoImage(Image.open('Media/1.jpg'))
        self.root.panel2 = Label(self.root, image=self.root.img2)
        self.root.panel2.place(x=20, y=10)

        self.btn = Button(self.root, text="Back To Menu", fg="#134611", font="Helvetica 20 bold", bg="#F9E8B1", padx=30,
                          pady=10, command=lambda: [self.hide3(), MenuPage(self.root)])
        self.btn.place(x=550, y=600)

    def hide3(self):
        self.btn.place_forget()
        self.root.panel.destroy()
        self.root.textt.destroy()
        self.root.panel2.destroy()

class AboutPage:
    def __init__(self, root):
        self.root = root

        self.root.img = ImageTk.PhotoImage(Image.open('Media/uss.jpg'))
        self.root.panel = Label(self.root, image=self.root.img)
        self.root.panel.place(x=0, y=90)

        self.root.name1 = "Eman Hesham"
        self.root.name2 = "Fatma El Zhraa Samir"
        self.root.name3 = "Hoda Mahmoud"
        self.root.name4 = "Hossam Ahmed"
        self.root.name5 = "Menna Khaled"

        self.root.text1 = Label(self.root, text=self.root.name1, font="Helvetica 20 bold", padx=10, pady=25)
        self.root.text1.place(x=770, y=100)
        self.root.text2 = Label(self.root, text=self.root.name2, font="Helvetica 20 bold", padx=10, pady=25)
        self.root.text2.place(x=970, y=180)
        self.root.text3 = Label(self.root, text=self.root.name3, font="Helvetica 20 bold", padx=10, pady=25)
        self.root.text3.place(x=770, y=260)
        self.root.text4 = Label(self.root, text=self.root.name4, font="Helvetica 20 bold", padx=10, pady=25)
        self.root.text4.place(x=950, y=340)
        self.root.text5 = Label(self.root, text=self.root.name5, font="Helvetica 20 bold", padx=10, pady=25)
        self.root.text5.place(x=770, y=410)

        self.v = Button(root, text="Back To Menu", fg="#134611", font="Helvetica 20 bold", bg="#F9E8B1", padx=30,
                        pady=10, command=lambda: [self.hide1(), MenuPage(self.root)])
        self.v.place(x=520, y=610)

    def hide1(self):
        self.root.panel.destroy()
        self.root.text1.place_forget()
        self.root.text2.place_forget()
        self.root.text3.place_forget()
        self.root.text4.place_forget()
        self.root.text5.place_forget()
        self.v.place_forget()

def main():
    root = Tk()
    root.geometry("1050x700")
    # root.iconbitmap('Media/12.ico')
    app = GUI(root)
    root.mainloop()

# if __name__ == "__main__":
main()