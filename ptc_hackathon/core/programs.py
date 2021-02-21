from tkinter import *
from tkinter import PhotoImage


def openhelp():
    exec(open("Help.py").read())


def opengame():
    global buttonMainQuit, buttonPlay, buttonHow, canvas, buttonPlayAgain, buttonQuit, topLeft, topMid, topRight, \
        midLeft, midMid, midRight, botLeft, botMid, botRight, tieText, count

    buttonMainQuit.place_forget()
    buttonPlay.place_forget()
    buttonHow.place_forget()
    buttonQuit.place_forget()
    buttonPlayAgain.place_forget()

    xwinText.pack_forget()
    owinText.pack_forget()
    tieText.pack_forget()

    canvas.delete("all")

    canvas = Canvas(root, width=600, height=600)
    canvas.create_line(200, 0, 200, 600)
    canvas.create_line(400, 0, 400, 600)
    canvas.create_line(0, 200, 600, 200)
    canvas.create_line(0, 400, 600, 400)
    canvas.bind('<Button-1>', userinput)
    canvas.pack()
    root.geometry("600x600+330+30")

    topLeft = 0
    topMid = 0
    topRight = 0
    midLeft = 0
    midMid = 0
    midRight = 0
    botLeft = 0
    botMid = 0
    botRight = 0

    count = 1


class Game:
    def __init__(self):
        pass

    def launch():

        root = Tk()

        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()

        midWidth = screenWidth / 2
        midHeight = screenHeight / 2

        print(midHeight, midWidth)

        # wow 9 different variables
        count = 1
        topLeft = 0
        topMid = 0
        topRight = 0
        midLeft = 0
        midMid = 0
        midRight = 0
        botLeft = 0
        botMid = 0
        botRight = 0
        owinText = Label(root, font="Calibri 30", text="Player two wins!",
                         anchor="center", wraplength=500, justify=CENTER)
        xwinText = Label(root, font="Calibri 30", text="Player one wins!",
                         anchor="center", wraplength=500, justify=CENTER)
        tieText = Label(root, font="Calibri 30", text="Tie!",
                        anchor="center", wraplength=500, justify=CENTER)

        def getxy(event):
            print("Position = ({0},{1})".format(event.x, event.y))

        def userinput(event):
            global count, topLeft, topMid, topRight, midLeft, midMid, midRight, botLeft, botMid, botRight, xwinText, owinText

            result = 0

            if event.x <= 200 and event.y <= 200:
                if topLeft == 0:
                    if count % 2 == 0:
                        topLeft = 2
                        canvas.create_oval(50, 50, 150, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

                    else:
                        topLeft = 1
                        canvas.create_line(50, 50, 150, 150, width=2)
                        canvas.create_line(150, 50, 50, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 400 >= event.x >= 201 and event.y <= 200:
                if topMid == 0:
                    if count % 2 == 0:
                        topMid = 2
                        canvas.create_oval(250, 50, 350, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        topMid = 1
                        canvas.create_line(250, 50, 350, 150, width=2)
                        canvas.create_line(350, 50, 250, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 600 >= event.x >= 401 and event.y <= 200:
                if topRight == 0:
                    if count % 2 == 0:
                        topRight = 2
                        canvas.create_oval(450, 50, 550, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        topRight = 1
                        canvas.create_line(450, 50, 550, 150, width=2)
                        canvas.create_line(550, 50, 450, 150, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if event.x <= 200 and 400 >= event.y >= 201:
                if midLeft == 0:
                    if count % 2 == 0:
                        midLeft = 2
                        canvas.create_oval(50, 250, 150, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        midLeft = 1
                        canvas.create_line(50, 250, 150, 350, width=2)
                        canvas.create_line(150, 250, 50, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 400 >= event.x >= 201 and 400 >= event.y >= 201:
                if midMid == 0:
                    if count % 2 == 0:
                        midMid = 2
                        canvas.create_oval(250, 250, 350, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        midMid = 1
                        canvas.create_line(250, 250, 350, 350, width=2)
                        canvas.create_line(350, 250, 250, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 600 >= event.x >= 401 and 400 >= event.y >= 201:
                if midRight == 0:
                    if count % 2 == 0:
                        midRight = 2
                        canvas.create_oval(450, 250, 550, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        midRight = 1
                        canvas.create_line(450, 250, 550, 350, width=2)
                        canvas.create_line(550, 250, 450, 350, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if event.x <= 200 and 600 >= event.y >= 401:
                if botLeft == 0:
                    if count % 2 == 0:
                        botLeft = 2
                        canvas.create_oval(50, 450, 150, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        botLeft = 1
                        canvas.create_line(50, 450, 150, 550, width=2)
                        canvas.create_line(150, 450, 50, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 400 >= event.x >= 201 and 600 >= event.y >= 401:
                if botMid == 0:
                    if count % 2 == 0:
                        botMid = 2
                        canvas.create_oval(250, 450, 350, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

                    else:
                        botMid = 1
                        canvas.create_line(250, 450, 350, 550, width=2)
                        canvas.create_line(350, 450, 250, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if 600 >= event.x >= 401 and 600 >= event.y >= 401:
                if botRight == 0:

                    if count % 2 == 0:
                        botRight = 2
                        canvas.create_oval(450, 450, 550, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()
                    else:
                        botRight = 1
                        canvas.create_line(450, 450, 550, 550, width=2)
                        canvas.create_line(550, 450, 450, 550, width=2)
                        count += 1
                        print(count)
                        result = checkwinner()
                        if count == 10:
                            tie()

            if result == 1:
                canvas.pack_forget()
                xwinText = Label(root, font="Calibri 30", text="X wins!",
                                 anchor="s", justify=CENTER, fg="green", bg="white")
                xwinText.pack()
                root.geometry("400x400+410+100")
                buttonQuit.place(x=145, y=260)
                buttonPlayAgain.place(x=100, y=150)

            elif result == 2:
                canvas.pack_forget()
                owinText = Label(root, font="Calibri 30", text="O wins!",
                                 anchor="s", fg="green", bg="white", justify=CENTER)
                owinText.pack()
                root.geometry("400x400+410+100")
                buttonQuit.place(x=145, y=260)
                buttonPlayAgain.place(x=100, y=150)

        def tie():
            canvas.pack_forget()
            tieText.pack()
            root.geometry("400x400+410+100")
            buttonQuit.place(x=145, y=260)
            buttonPlayAgain.place(x=100, y=150)

        def checkwinner():
            if topLeft == topMid and topLeft == topRight and topLeft != 0:
                return topLeft

            elif midLeft == midMid and midLeft == midRight and midLeft != 0:
                return midLeft

            elif botLeft == botMid and botLeft == botRight and botLeft != 0:
                return botLeft

            elif topLeft == midLeft and topLeft == botLeft and topLeft != 0:
                return topLeft

            elif topMid == midMid and topMid == botMid and topMid != 0:
                return topMid

            elif topRight == midRight and topRight == botRight and topRight != 0:
                return topRight

            elif topLeft == midMid and topLeft == botRight and topLeft != 0:
                return topLeft

            elif topRight == midMid and topRight == botLeft and topRight != 0:
                return topRight

        root.title("TicTacToe")
        question = PhotoImage(file="static/img/mark.png")

        buttonPlayAgain = Button(root, font="Calibri 30",
                                 text="Play again", fg="black", command=opengame)

        buttonQuit = Button(root, font="Calibri 30", text="Quit",
                            fg="red", command=root.destroy, height=-30)

        buttonMainQuit = Button(root, font="Calibri 30",
                                text="QUIT", fg="red", command=quit)
        buttonMainQuit.place(x=174, y=220)

        buttonPlay = Button(root, font="Calibri 30", text="PLAY",
                            fg="green", command=opengame)
        buttonPlay.place(x=175, y=125)

        buttonHow = Button(root, image=question, command=openhelp)
        buttonHow.place(x=350, y=50)

        root.title("Tic Tac Toe")
        root.resizable(0, 0)
        root.geometry("450x450+750+450")
        root.configure(bg="white")

        canvas = Canvas(root, width=600, height=600)
        canvas.create_line(200, 0, 200, 600)
        canvas.create_line(400, 0, 400, 600)
        canvas.create_line(0, 200, 600, 200)
        canvas.create_line(0, 400, 600, 400)
        canvas.bind('<Button-1>', userinput)

        root.mainloop()
