from tkinter import*
import random

attempts = 20

answer = random.randrange(0, 21)

def check_answer():
    global attempts
    global text

    attempts -=1

    guess = int(entry_window.get())

    if guess > 21:
        text.set("Please Type A Number Smaller Than 21")
    elif answer == guess:
        text.set("You Win! Comngrats!!")
        btn_check.pack_forget()
    
    elif attempts == 0:
        text.set("You Are Out Of Attempts!")
        btn_check.pack_forget()
    
    elif guess < answer:
        text.set("Please Type a Bigger Number! You Have" + str(attempts) + "Attempts Rremaining")
    
    elif guess > answer:
        text.set("Please Type a Smaller Number! Tou Have" + str(attempts) + "Attempts Remaining")


root = Tk()

root.title("Guess The Number")

root.geometry('588x188')

label = Label(root, text="Guess The Number Between 0 and 21")
label.pack()

entry_window = Entry(root,width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="CHECK", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="QUIT", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You Have 20 Attempts Remaining! Goood Luck!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()