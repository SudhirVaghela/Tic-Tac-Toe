from tkinter import *
import tkinter.messagebox


window = Tk()
window.geometry("1800x700+0+0")
window.title("Tic Tac Toe")
window.configure(background="steelblue4")
print('hekko')
Tops = Frame(window, bg="paleTurquoise4", height=100, bd=18, width=1800, pady=8, padx=8, relief=RAISED)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=("arial", 50, "bold"), text=" Let`s Play Tic Tac Toe", bd=21, bg="cadet blue2",
                 fg="magenta4",
                 justify=CENTER)
lblTitle.grid(row=0, column=0)

mainframe = Frame(window, bg="aquamarine", bd=10, width=1800, height=500, relief=RIDGE)
mainframe.grid(row=1, column=0)

leftframe = Frame(mainframe, bd=21, width=790, height=500, bg="lavender", relief=RIDGE, pady=3, padx=10)
leftframe.pack(side=RIGHT)

rightframe = Frame(mainframe, bd=21, width=790, height=500, bg="lavender", relief=RIDGE, padx=3, pady=10)
rightframe.pack(side=LEFT)

rightframe1 = Frame(rightframe, bd=15, padx=10, pady=2, height=200, bg="gray69", width=200, relief=RIDGE)
rightframe1.grid(row=0, column=0, sticky=N + E + S + W)

rightframe2 = Frame(rightframe, bd=15, padx=10, pady=2, height=200, width=200, bg="gray69", relief=RIDGE)
rightframe2.grid(row=1, column=0, sticky=N + E + S + W)

player_1_name = StringVar()
player_2_name = StringVar()

playerX = IntVar()
playerO = IntVar()

btns = StringVar()
pl1 = StringVar()
pl2 = StringVar()

p1 = Label(rightframe1, font=("sans serif", 15, "bold"), text="First Player : X", bd=10, bg="cadet blue2",
           fg="magenta4", justify=LEFT, relief=FLAT).grid(row=0, column=0, sticky=N + E + S + W)

player1 = Entry(rightframe1, font=("arial", 20, "bold"), textvariable=player_1_name)

player1.grid(row=0, column=1, sticky=N + E + S + W)

textplayer1 = Entry(rightframe1, font=("sans serif", 20, "bold"), textvariable=playerX, width=20, bd=2,
                    state="disabled").grid(row=0, column=2, sticky=N + E + S + W, padx=2)

p2 = Label(rightframe1, font=("sans serif", 15, "bold"), text="Second Player : O", bd=10, bg="cadet blue2",
           fg="magenta4", justify=LEFT, relief=FLAT).grid(row=1, column=0, sticky=N + E + S + W)

player2 = Entry(rightframe1, font=("arial", 20, "bold"), textvariable=player_2_name)

player2.grid(row=1, column=1, sticky=N + E + S + W)

textplayer2 = Entry(rightframe1, font=("sans serif", 20, "bold"), textvariable=playerO, width=20, bd=2
                    , state="disabled").grid(row=1, column=2, sticky=N + E + S + W, padx=2)

clk = False
tie = 0


def check(btns):
    global clk, pl1, pl2, tie
    if btns["text"] == " " and clk == False:
        btns["text"] = "X"
        clk = True
        pl1 = player1.get() + " Congratulations you won this game........."
        scoreboard()
        tie += 1

    elif btns["text"] == " " and clk == True:
        btns["text"] = "O"
        clk = False
        pl2 = player2.get() + " Congratulations you won this game........."
        scoreboard()
        tie += 1


def disablebtn():
    btn1.configure(state="disabled")
    btn2.configure(state="disabled")
    btn3.configure(state="disabled")
    btn4.configure(state="disabled")
    btn5.configure(state="disabled")
    btn6.configure(state="disabled")
    btn7.configure(state="disabled")
    btn8.configure(state="disabled")
    btn9.configure(state="disabled")


def scoreboard():
    global tie, btns
    if btn1['text'] == btn2['text'] and btn1['text'] == btn3['text'] and btn1["text"] == "X":
        btn1.configure(bg="PeachPuff4")
        btn2.configure(bg="PeachPuff4")
        btn3.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn4['text'] == btn5['text'] and btn4['text'] == btn6['text'] and btn4["text"] == "X":
        btn4.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn6.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn7['text'] == btn8['text'] and btn7['text'] == btn9['text'] and btn7["text"] == "X":
        btn7.configure(bg="PeachPuff4")
        btn8.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn1['text'] == btn4['text'] and btn1['text'] == btn7['text'] and btn1["text"] == "X":
        btn1.configure(bg="PeachPuff4")
        btn4.configure(bg="PeachPuff4")
        btn7.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn2['text'] == btn5['text'] and btn2['text'] == btn8['text'] and btn2["text"] == "X":
        btn2.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn8.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn3['text'] == btn6['text'] and btn3['text'] == btn9['text'] and btn3["text"] == "X":
        btn3.configure(bg="PeachPuff4")
        btn6.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn1['text'] == btn5['text'] and btn1['text'] == btn9['text'] and btn1["text"] == "X":
        btn1.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn3['text'] == btn5['text'] and btn3['text'] == btn7['text'] and btn3["text"] == "X":
        btn3.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn7.configure(bg="PeachPuff4")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X", pl1)

        reset()
        check(btns)

    elif btn1['text'] == btn2['text'] and btn1['text'] == btn3['text'] and btn1["text"] == "O":
        btn1.configure(bg="PeachPuff4")
        btn2.configure(bg="PeachPuff4")
        btn3.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn4['text'] == btn5['text'] and btn4['text'] == btn6['text'] and btn4["text"] == "O":
        btn4.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn6.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn7['text'] == btn8['text'] and btn7['text'] == btn9['text'] and btn7["text"] == "O":
        btn7.configure(bg="PeachPuff4")
        btn8.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn1['text'] == btn4['text'] and btn1['text'] == btn7['text'] and btn1["text"] == "O":
        btn1.configure(bg="PeachPuff4")
        btn4.configure(bg="PeachPuff4")
        btn7.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn2['text'] == btn5['text'] and btn2['text'] == btn8['text'] and btn2["text"] == "O":
        btn2.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn8.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn3['text'] == btn6['text'] and btn3['text'] == btn9['text'] and btn3["text"] == "O":
        btn3.configure(bg="PeachPuff4")
        btn6.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn1['text'] == btn5['text'] and btn1['text'] == btn9['text'] and btn1["text"] == "O":
        btn1.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn9.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif btn3['text'] == btn5['text'] and btn3['text'] == btn7['text'] and btn3["text"] == "O":
        btn3.configure(bg="PeachPuff4")
        btn5.configure(bg="PeachPuff4")
        btn7.configure(bg="PeachPuff4")
        m = float(playerO.get())
        score = m + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("winner O", pl2)

        reset()
        check(btns)

    elif tie == 8:
        tkinter.messagebox.showinfo("Tie game", "This game is tie....")
        reset()
        check(btns)



def reset():
    global tie
    tie = 0
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "

    btn1.configure(bg="medium aquamarine")
    btn2.configure(bg="medium aquamarine")
    btn3.configure(bg="medium aquamarine")
    btn4.configure(bg="medium aquamarine")
    btn5.configure(bg="medium aquamarine")
    btn6.configure(bg="medium aquamarine")
    btn7.configure(bg="medium aquamarine")
    btn8.configure(bg="medium aquamarine")
    btn9.configure(bg="medium aquamarine")


def New_Game():
    global tie
    global player1
    global player2

    player1 = Entry(rightframe1, font=("arial", 20, "bold"), text="None")
    player1.grid(row=0, column=1, sticky=N + E + S + W)

    player2 = Entry(rightframe1, font=("arial", 20, "bold"), text="None")
    player2.grid(row=1, column=1, sticky=N + E + S + W)

    reset()
    Clear()

    btn1.configure(bg="CadetBlue3")
    btn2.configure(bg="CadetBlue3")
    btn3.configure(bg="CadetBlue3")
    btn4.configure(bg="CadetBlue3")
    btn5.configure(bg="CadetBlue3")
    btn6.configure(bg="CadetBlue3")
    btn7.configure(bg="CadetBlue3")
    btn8.configure(bg="CadetBlue3")
    btn9.configure(bg="CadetBlue3")


def Clear():
    playerX.set(0)
    playerO.set(0)


btnclr = Button(rightframe2, text="clear score", bd=5, font=("arial", 30, "bold"), height=5, width=12,
                bg="medium aquamarine", command=Clear)
btnclr.grid(row=0, column=1, sticky=N + E + S + W, rowspan=2, columnspan=1)

btnreset = Button(rightframe2, text="RESTART", bd=5, font=("arial", 30, "bold"), height=1, width=20,
                  bg="medium aquamarine",
                  command=reset)
btnreset.grid(row=0, column=0, sticky=N + E + S + W, padx=5, pady=5)

btnnew = Button(rightframe2, text="NEW GAME", bd=5, font=("arial", 30, "bold"), height=1, width=20, bg="CadetBlue3",
                command=New_Game)
btnnew.grid(row=1, column=0, sticky=N + E + S + W, padx=5, pady=5)

btn1 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn1))
btn1.grid(row=0, column=0, sticky=N + E + S + W)

btn2 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn2))
btn2.grid(row=0, column=1, sticky=N + E + S + W)

btn3 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn3))
btn3.grid(row=0, column=2, sticky=N + E + S + W)

btn4 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn4))
btn4.grid(row=1, column=0, sticky=N + E + S + W)

btn5 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn5))
btn5.grid(row=1, column=1, sticky=N + E + S + W)

btn6 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn6))
btn6.grid(row=1, column=2, sticky=N + E + S + W)

btn7 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn7))
btn7.grid(row=2, column=0, sticky=N + E + S + W)

btn8 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn8))
btn8.grid(row=2, column=1, sticky=N + E + S + W)

btn9 = Button(leftframe, text=" ", font=("arial", 50, "bold"), height=1, width=3, bg="CadetBlue3",
              command=lambda: check(btn9))
btn9.grid(row=2, column=2, sticky=N + E + S + W)

window.mainloop()
