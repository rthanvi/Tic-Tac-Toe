
from pydoc import text
from tkinter import*
import tkinter.messagebox as msg
root=Tk()
root.title("Tiktacto")

Label(root,text="player 1: X",font="times 15" ).grid(row=0,column=1)
Label(root,text="player 2: O",font="times 15" ).grid(row=0,column=2) 

digits=[1,2,3,4,5,6,7,8,9]

mark=""
count=0
panel=["panels"]*10


def win(panel,sign):
    return ((panel[1]==panel[2]==panel[3]==sign)
    or (panel[1]==panel[4]==panel[7]==sign)
    or(panel[1]==panel[5]==panel[9]==sign)
    or (panel[2]==panel[5]==panel[8]==sign)
    or (panel[3]==panel[6]==panel[9]==sign)
    or (panel[3]==panel[5]==panel[7]==sign)
    or(panel[4]==panel[5]==panel[6]==sign)
    or (panel[7]==panel[8]==panel[9]==sign))


def checker(digit):
  global count,mark,digits


  if digit==1 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button1.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
  if digit==2 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button2.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==3 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button3.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==4 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button4.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==5 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button5.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==6 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button6.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==7 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button7.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==8 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button8.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    if digit==9 and digit in digits:
      digits.remove(digit)

      if count%2==0:
          mark='X'
          panel[digit]=mark
      elif count%2!=0:
          mark='O'
          panel[digit]=mark


        button9.config(text=mark)
        count=count+1
        sign=mark

        if (win(panel,sign) and sign=='X'):
            msg.showinfo('result','player1 wins')



            root.destroy()

        elif(win(panel,sign) and sign=='O'):
            msg.showinfo('result','player2 wins')

            root.destroy()
    

    
    


  



    
    


  



    
    


  



    
    


  



    
    


  



    
    


  



    
    


  



    
    


  


    

    
    


  



    
       

  









root.mainloop()