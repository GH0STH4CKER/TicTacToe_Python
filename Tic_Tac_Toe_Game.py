from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk

root=Tk()
root.title("Tic Tac Toe")
#root.geometry("487x544")

img1 = Image.open(r"C:\Users\Dimuth De Zoysa\Desktop\Python_projects\ticcircle1.png")
img1 = img1.resize((140,139), Image.ANTIALIAS)
tick_circle = ImageTk.PhotoImage(img1)

img2 = Image.open(r"C:\Users\Dimuth De Zoysa\Desktop\Python_projects\ticcross1.png")
img2 = img2.resize((146,145), Image.ANTIALIAS)
tick_cross = ImageTk.PhotoImage(img2)

img3 = Image.open(r"C:\Users\Dimuth De Zoysa\Desktop\Python_projects\ticempty.png")
img3 = img3.resize((150,150), Image.ANTIALIAS)
tick_none = ImageTk.PhotoImage(img3)

img4 = Image.open(r"C:\Users\Dimuth De Zoysa\Desktop\Python_projects\refresh.png")
img4 = img4.resize((30,30), Image.ANTIALIAS)
restart_img = ImageTk.PhotoImage(img4)

# Buttons
btn1=Button(root,text=' ',image=tick_none,width=150,height=150)
btn1.grid(row=0,column=0,padx=0,pady=0)
btn1.config(command=lambda: ButtonClick(1))

btn2=Button(root,text=' ',image=tick_none,width=150,height=150)
btn2.grid(row=0,column=1,sticky='snew',padx=0,pady=0)
btn2.config(command=lambda: ButtonClick(2))

btn3=Button(root,text=' ',image=tick_none,width=150,height=150)
btn3.grid(row=0,column=2,sticky='snew',padx=0,pady=0)
btn3.config(command=lambda: ButtonClick(3))

btn4=Button(root,text=' ',image=tick_none,width=150,height=150)
btn4.grid(row=1,column=0,sticky='snew',padx=0,pady=0)
btn4.config(command=lambda: ButtonClick(4))

btn5=Button(root,text=' ',image=tick_none,width=150,height=150)
btn5.grid(row=1,column=1,sticky='snew',padx=0,pady=0)
btn5.config(command=lambda: ButtonClick(5))

btn6=Button(root,text=' ',image=tick_none,width=150,height=150)
btn6.grid(row=1,column=2,sticky='snew',padx=0,pady=0)
btn6.config(command=lambda: ButtonClick(6))

btn7=Button(root,text=' ',image=tick_none,width=150,height=150)
btn7.grid(row=2,column=0,sticky='snew',padx=0,pady=0)
btn7.config(command=lambda: ButtonClick(7))

btn8=Button(root,text=' ',image=tick_none,width=150,height=150)
btn8.grid(row=2,column=1,sticky='snew',padx=0,pady=0)
btn8.config(command=lambda: ButtonClick(8))

btn9=Button(root,text=' ',image=tick_none,width=150,height=150)
btn9.grid(row=2,column=2,sticky='snew',padx=0,pady=0)
btn9.config(command=lambda: ButtonClick(9))

playerturn=Label(root,text="   Player 1 turn!  ",font=("Cambria 15 normal"))
playerturn.grid(row=3,column=0,sticky='snew',padx=0,pady=0)

playerdetails=Label(root,text="    Player 1 is ✖\n    Player 2 is Ｏ",font=("Cambria 15 normal"))
playerdetails.grid(row=3,column=2,sticky='snew',padx=0,pady=0)

res=Button(root,text='Restart',image=restart_img,compound=LEFT,font=("Cambria 17 normal"))
res.grid(row=3,column=1,sticky='snew',padx=0,pady=0)
res.config(command=lambda: restartbutton())

a=1
b=0
c=0

# Restart function
def restartbutton():
    global a,b,c
    a=1
    b=0
    c=0
    #clear Selections/Text
    playerturn['text']="   Player 1 turn!   "
    btn1['text']=' '
    btn2['text']=' '
    btn3['text']=' '
    btn4['text']=' '
    btn5['text']=' '
    btn6['text']=' '
    btn7['text']=' '
    btn8['text']=' '
    btn9['text']=' '
    btn1.config(command=lambda: ButtonClick(1),relief='raised')
    btn2.config(command=lambda: ButtonClick(2),relief='raised')
    btn3.config(command=lambda: ButtonClick(3),relief='raised')
    btn4.config(command=lambda: ButtonClick(4),relief='raised')
    btn5.config(command=lambda: ButtonClick(5),relief='raised')
    btn6.config(command=lambda: ButtonClick(6),relief='raised')
    btn7.config(command=lambda: ButtonClick(7),relief='raised')
    btn8.config(command=lambda: ButtonClick(8),relief='raised')
    btn9.config(command=lambda: ButtonClick(9),relief='raised')
    btn1.configure(image=tick_none)
    btn2.configure(image=tick_none)
    btn3.configure(image=tick_none)
    btn4.configure(image=tick_none)
    btn5.configure(image=tick_none)
    btn6.configure(image=tick_none)
    btn7.configure(image=tick_none)
    btn8.configure(image=tick_none)
    btn9.configure(image=tick_none)
    btn1.configure(bg='#f0f0ed')
    btn2.configure(bg='#f0f0ed')
    btn3.configure(bg='#f0f0ed')
    btn4.configure(bg='#f0f0ed')
    btn5.configure(bg='#f0f0ed')
    btn6.configure(bg='#f0f0ed')
    btn7.configure(bg='#f0f0ed')
    btn8.configure(bg='#f0f0ed')
    btn9.configure(bg='#f0f0ed')
    
    
# Disable buttons when game is over
def disableButton():
    btn2.config(command=0,relief='sunken')
    btn3.config(command=0,relief='sunken')
    btn4.config(command=0,relief='sunken')
    btn1.config(command=0,relief='sunken')
    btn5.config(command=0,relief='sunken')
    btn6.config(command=0,relief='sunken')
    btn7.config(command=0,relief='sunken')
    btn8.config(command=0,relief='sunken')
    btn9.config(command=0,relief='sunken')

def ButtonClick(id):
    global a,b,c
    print("Box {} Pressed.".format(id))

    # Player 1 turn
    if id==1 and btn1['text']==' ' and a==1:
        btn1['text']="X"
        btn1.config(image=tick_cross)
        a=0
        b+=1
    if id==2 and btn2['text']==' ' and a==1:
        btn2['text']="X"
        btn2.config(image=tick_cross)
        a=0
        b+=1
    if id==3 and btn3['text']==' ' and a==1:
        btn3['text']="X"
        btn3.config(image=tick_cross)
        a=0
        b+=1
    if id==4 and btn4['text']==' ' and a==1:
        btn4['text']="X"
        btn4.config(image=tick_cross)
        a=0
        b+=1
    if id==5 and btn5['text']==' ' and a==1:
        btn5['text']="X"
        btn5.config(image=tick_cross)
        a=0
        b+=1
    if id==6 and btn6['text']==' ' and a==1:
        btn6['text']="X"
        btn6.config(image=tick_cross)
        a=0
        b+=1
    if id==7 and btn7['text']==' ' and a==1:
        btn7['text']="X"
        btn7.config(image=tick_cross)
        a=0
        b+=1
    if id==8 and btn8['text']==' ' and a==1:
        btn8['text']="X"
        btn8.config(image=tick_cross)
        a=0
        b+=1
    if id==9 and btn9['text']==' ' and a==1:
        btn9['text']="X"
        btn9.config(image=tick_cross)
        a=0
        b+=1
    # Player 2 turn
    if id==1 and btn1['text']==' ' and a==0:
        btn1['text']="O"
        btn1.config(image=tick_circle)
        a=1
        b+=1
    if id==2 and btn2['text']==' ' and a==0:
        btn2['text']="O"
        btn2.config(image=tick_circle)
        a=1
        b+=1
    if id==3 and btn3['text']==' ' and a==0:
        btn3['text']="O"
        btn3.config(image=tick_circle)
        a=1
        b+=1
    if id==4 and btn4['text']==' ' and a==0:
        btn4['text']="O"
        btn4.config(image=tick_circle)
        a=1
        b+=1
    if id==5 and btn5['text']==' ' and a==0:
        btn5['text']="O"
        btn5.config(image=tick_circle)
        a=1
        b+=1
    if id==6 and btn6['text']==' ' and a==0:
        btn6['text']="O"
        btn6.config(image=tick_circle)
        a=1
        b+=1
    if id==7 and btn7['text']==' ' and a==0:
        btn7['text']="O"
        btn7.config(image=tick_circle)
        a=1
        b+=1
    if id==8 and btn8['text']==' ' and a==0:
        btn8['text']="O"
        btn8.config(image=tick_circle)
        a=1
        b+=1
    if id==9 and btn9['text']==' ' and a==0:
        btn9['text']="O"
        btn9.config(image=tick_circle)
        a=1
        b+=1
        
    # Checking if player 1 wins
    if btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' :
        btn1.config(bg='#db0f0f')
        btn2.config(bg='#db0f0f')
        btn3.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' :
        btn4.config(bg='#db0f0f')
        btn5.config(bg='#db0f0f')
        btn6.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' :
        btn7.config(bg='#db0f0f')
        btn8.config(bg='#db0f0f')
        btn9.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' :
        btn1.config(bg='#db0f0f')
        btn4.config(bg='#db0f0f')
        btn7.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' :
        btn2.config(bg='#db0f0f')
        btn5.config(bg='#db0f0f')
        btn8.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' :
        btn3.config(bg='#db0f0f')
        btn6.config(bg='#db0f0f')
        btn9.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' :
        btn1.config(bg='#db0f0f')
        btn5.config(bg='#db0f0f')
        btn9.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")
    
    elif btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X' :
        btn3.config(bg='#db0f0f')
        btn5.config(bg='#db0f0f')
        btn7.config(bg='#db0f0f')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 1")

    # Checking for Player 2 wins 
    elif btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' :
        btn1.config(bg='cyan')
        btn2.config(bg='cyan')
        btn3.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' :
        btn4.config(bg='cyan')
        btn5.config(bg='cyan')
        btn6.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' :
        btn7.config(bg='cyan')
        btn8.config(bg='cyan')
        btn9.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' :
        btn1.config(bg='cyan')
        btn4.config(bg='cyan')
        btn7.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O' :
        btn2.config(bg='cyan')
        btn5.config(bg='cyan')
        btn8.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' :
        btn3.config(bg='cyan')
        btn6.config(bg='cyan')
        btn9.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' :
        btn1.config(bg='cyan')
        btn5.config(bg='cyan')
        btn9.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")
    
    elif btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O' :
        btn3.config(bg='cyan')
        btn5.config(bg='cyan')
        btn7.config(bg='cyan')
        disableButton()
        c=1
        tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Player 2")

    # Checks for match draw
    elif b==9:
            disableButton()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    if a==1 and c==0:
        playerturn['text']="   Player 1 turn!   "
    elif a==0 and c==0:
        playerturn['text']="   Player 2 turn!   "
            
root.mainloop()

