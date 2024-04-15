import tkinter as tk
import os
try:
  from random_word import RandomWords
except:
  os.system("pip install Random-Word")
from random_word import RandomWords

r = RandomWords()
ans = ""
while len(ans) != 5:
  ans = r.get_random_word()

from tkinter import messagebox

root = tk.Tk()
root.title("Wordle (Relaunch to replay)")
root.config(bg="white")
root.geometry("700x600")
title = tk.Label(root,
                 text="WORDLE",
                 font=("Arial Bold", 15),
                 bg="white",
                 fg="black").pack()
separator = tk.Label(
    root,
    text=
    "_____________________________________________________________________________________________________________________",
    bg="white",
    fg="black").pack()
frame1 = tk.Frame(root, bg="white")
frame1.pack()
row1_1 = tk.Label(frame1, bg="grey", width=5, height=3, fg="white")
row1_1.pack(side=tk.LEFT, padx=4, pady=4)
row1_2 = tk.Label(frame1, bg="grey", width=5, height=3, fg="white")
row1_2.pack(side=tk.LEFT, padx=4, pady=4)
row1_3 = tk.Label(frame1, bg="grey", width=5, height=3, fg="white")
row1_3.pack(side=tk.LEFT, padx=4, pady=4)
row1_4 = tk.Label(frame1, bg="grey", width=5, height=3, fg="white")
row1_4.pack(side=tk.LEFT, padx=4, pady=4)
row1_5 = tk.Label(frame1, bg="grey", width=5, height=3, fg="white")
row1_5.pack(side=tk.LEFT, padx=4, pady=4)
frame2 = tk.Frame(root, bg="white")
frame2.pack()
row2_1 = tk.Label(frame2, bg="grey", width=5, height=3, fg="white")
row2_1.pack(side=tk.LEFT, padx=4, pady=4)
row2_2 = tk.Label(frame2, bg="grey", width=5, height=3, fg="white")
row2_2.pack(side=tk.LEFT, padx=4, pady=4)
row2_3 = tk.Label(frame2, bg="grey", width=5, height=3, fg="white")
row2_3.pack(side=tk.LEFT, padx=4, pady=4)
row2_4 = tk.Label(frame2, bg="grey", width=5, height=3, fg="white")
row2_4.pack(side=tk.LEFT, padx=4, pady=4)
row2_5 = tk.Label(frame2, bg="grey", width=5, height=3, fg="white")
row2_5.pack(side=tk.LEFT, padx=4, pady=4)
frame3 = tk.Frame(root, bg="white")
frame3.pack()
row3_1 = tk.Label(frame3, bg="grey", width=5, height=3, fg="white")
row3_1.pack(side=tk.LEFT, padx=4, pady=4)
row3_2 = tk.Label(frame3, bg="grey", width=5, height=3, fg="white")
row3_2.pack(side=tk.LEFT, padx=4, pady=4)
row3_3 = tk.Label(frame3, bg="grey", width=5, height=3, fg="white")
row3_3.pack(side=tk.LEFT, padx=4, pady=4)
row3_4 = tk.Label(frame3, bg="grey", width=5, height=3, fg="white")
row3_4.pack(side=tk.LEFT, padx=4, pady=4)
row3_5 = tk.Label(frame3, bg="grey", width=5, height=3, fg="white")
row3_5.pack(side=tk.LEFT, padx=4, pady=4)
frame4 = tk.Frame(root, bg="white")
frame4.pack()
row4_1 = tk.Label(frame4, bg="grey", width=5, height=3, fg="white")
row4_1.pack(side=tk.LEFT, padx=4, pady=4)
row4_2 = tk.Label(frame4, bg="grey", width=5, height=3, fg="white")
row4_2.pack(side=tk.LEFT, padx=4, pady=4)
row4_3 = tk.Label(frame4, bg="grey", width=5, height=3, fg="white")
row4_3.pack(side=tk.LEFT, padx=4, pady=4)
row4_4 = tk.Label(frame4, bg="grey", width=5, height=3, fg="white")
row4_4.pack(side=tk.LEFT, padx=4, pady=4)
row4_5 = tk.Label(frame4, bg="grey", width=5, height=3, fg="white")
row4_5.pack(side=tk.LEFT, padx=4, pady=4)
frame5 = tk.Frame(root, bg="white")
frame5.pack()
row5_1 = tk.Label(frame5, bg="grey", width=5, height=3, fg="white")
row5_1.pack(side=tk.LEFT, padx=4, pady=4)
row5_2 = tk.Label(frame5, bg="grey", width=5, height=3, fg="white")
row5_2.pack(side=tk.LEFT, padx=4, pady=4)
row5_3 = tk.Label(frame5, bg="grey", width=5, height=3, fg="white")
row5_3.pack(side=tk.LEFT, padx=4, pady=4)
row5_4 = tk.Label(frame5, bg="grey", width=5, height=3, fg="white")
row5_4.pack(side=tk.LEFT, padx=4, pady=4)
row5_5 = tk.Label(frame5, bg="grey", width=5, height=3, fg="white")
row5_5.pack(side=tk.LEFT, padx=4, pady=4)
frame6 = tk.Frame(root, bg="white")
frame6.pack()
row6_1 = tk.Label(frame6, bg="grey", width=5, height=3, fg="white")
row6_1.pack(side=tk.LEFT, padx=4, pady=4)
row6_2 = tk.Label(frame6, bg="grey", width=5, height=3, fg="white")
row6_2.pack(side=tk.LEFT, padx=4, pady=4)
row6_3 = tk.Label(frame6, bg="grey", width=5, height=3, fg="white")
row6_3.pack(side=tk.LEFT, padx=4, pady=4)
row6_4 = tk.Label(frame6, bg="grey", width=5, height=3, fg="white")
row6_4.pack(side=tk.LEFT, padx=4, pady=4)
row6_5 = tk.Label(frame6, bg="grey", width=5, height=3, fg="white")
row6_5.pack(side=tk.LEFT, padx=4, pady=4)
label1 = tk.Label(root, text="Input your guess here:", bg="white",
                  fg="black").pack()
guess = tk.StringVar()
user = tk.Entry(root, textvariable=guess)
user.pack(pady=4)


def enter_from_console():
  guess1 = input("Input your guess:")
  user.insert(tk.END, guess1)


def bs():
  user.delete(len(guess.get()) - 1, tk.END)


frame7 = tk.Frame(root, bg="white")
frame7.pack()

button2 = tk.Button(frame7,
                    bg="grey",
                    fg="white",
                    text="Backspace",
                    command=bs)
button2.pack(side=tk.LEFT, padx=4, pady=4)
g = 1


def enter():
  global g
  captialized = guess.get().upper()
  if len(guess.get()) != 5:
    messagebox.showerror("Error", "Please input a 5-letter word!")
  else:
    if guess.get() == ans and g == 1:
      row1_1.config(bg="green",text=captialized[0])
      row1_2.config(bg="green",text=captialized[1])
      row1_3.config(bg="green",text=captialized[2])
      row1_4.config(bg="green",text=captialized[3])
      row1_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "You are a genius!")
    elif guess.get() == ans and g == 2:
      row2_1.config(bg="green",text=captialized[0])
      row2_2.config(bg="green",text=captialized[1])
      row2_3.config(bg="green",text=captialized[2])
      row2_4.config(bg="green",text=captialized[3])
      row2_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "Magnificient!")
    elif guess.get() == ans and g == 3:
      row3_1.config(bg="green",text=captialized[0])
      row3_2.config(bg="green",text=captialized[1])
      row3_3.config(bg="green",text=captialized[2])
      row3_4.config(bg="green",text=captialized[3])
      row3_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "Impressive!")
    elif guess.get() == ans and g == 4:
      row4_1.config(bg="green",text=captialized[0])
      row4_2.config(bg="green",text=captialized[1])
      row4_3.config(bg="green",text=captialized[2])
      row4_4.config(bg="green",text=captialized[3])
      row4_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "Splendid!")
    elif guess.get() == ans and g == 5:
      row5_1.config(bg="green",text=captialized[0])
      row5_2.config(bg="green",text=captialized[1])
      row5_3.config(bg="green",text=captialized[2])
      row5_4.config(bg="green",text=captialized[3])
      row5_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "Great!")
    elif guess.get() == ans and g == 6:
      row6_1.config(bg="green",text=captialized[0])
      row6_2.config(bg="green",text=captialized[1])
      row6_3.config(bg="green",text=captialized[2])
      row6_4.config(bg="green",text=captialized[3])
      row6_5.config(bg="green",text=captialized[4])
      messagebox.showinfo("You win!", "Phew!")
    elif g > 6:
      messagebox.showerror("You lose!",
                           f"The correct answer is {ans.upper()}.")
    elif g == 6 and guess.get() != ans:
      messagebox.showerror("You lose!",
                           f"The correct answer is {ans.upper()}.")
    else:
      guessed = guess.get().upper()
      gussr = guess.get()
      if g == 1:
        row1_1.config(text=guessed[0])
        row1_2.config(text=guessed[1])
        row1_3.config(text=guessed[2])
        row1_4.config(text=guessed[3])
        row1_5.config(text=guessed[4])
      elif g == 2:
        row2_1.config(text=guessed[0])
        row2_2.config(text=guessed[1])
        row2_3.config(text=guessed[2])
        row2_4.config(text=guessed[3])
        row2_5.config(text=guessed[4])
      elif g == 3:
        row3_1.config(text=guessed[0])
        row3_2.config(text=guessed[1])
        row3_3.config(text=guessed[2])
        row3_4.config(text=guessed[3])
        row3_5.config(text=guessed[4])
      elif g == 4:
        row4_1.config(text=guessed[0])
        row4_2.config(text=guessed[1])
        row4_3.config(text=guessed[2])
        row4_4.config(text=guessed[3])
        row4_5.config(text=guessed[4])
      elif g == 5:
        row5_1.config(text=guessed[0])
        row5_2.config(text=guessed[1])
        row5_3.config(text=guessed[2])
        row5_4.config(text=guessed[3])
        row5_5.config(text=guessed[4])
      elif g == 6:
        row6_1.config(text=guessed[0])
        row6_2.config(text=guessed[1])
        row6_3.config(text=guessed[2])
        row6_4.config(text=guessed[3])
        row6_5.config(text=guessed[4])
      for i in range(0, 5):
        if gussr[i] == ans[i]:
          if g == 1 and i == 0:
            row1_1.config(bg="green")
          elif g == 2 and i == 0:
            row2_1.config(bg="green")
          elif g == 3 and i == 0:
            row3_1.config(bg="green")
          elif g == 4 and i == 0:
            row4_1.config(bg="green")
          elif g == 5 and i == 0:
            row5_1.config(bg="green")
          elif g == 6 and i == 0:
            row6_2.config(bg="green")
          elif g == 1 and i == 1:
            row1_2.config(bg="green")
          elif g == 2 and i == 1:
            row2_2.config(bg="green")
          elif g == 3 and i == 1:
            row3_2.config(bg="green")
          elif g == 4 and i == 1:
            row4_2.config(bg="green")
          elif g == 5 and i == 1:
            row5_2.config(bg="green")
          elif g == 6 and i == 1:
            row6_2.config(bg="green")
          elif g == 1 and i == 2:
            row1_3.config(bg="green")
          elif g == 2 and i == 2:
            row2_3.config(bg="green")
          elif g == 3 and i == 2:
            row3_3.config(bg="green")
          elif g == 4 and i == 2:
            row4_3.config(bg="green")
          elif g == 5 and i == 2:
            row5_3.config(bg="green")
          elif g == 6 and i == 2:
            row6_3.config(bg="green")
          elif g == 1 and i == 3:
            row1_4.config(bg="green")
          elif g == 2 and i == 3:
            row2_4.config(bg="green")
          elif g == 3 and i == 3:
            row3_4.config(bg="green")
          elif g == 4 and i == 3:
            row4_4.config(bg="green")
          elif g == 5 and i == 3:
            row5_4.config(bg="green")
          elif g == 6 and i == 3:
            row6_4.config(bg="green")
          elif g == 1 and i == 4:
            row1_5.config(bg="green")
          elif g == 2 and i == 4:
            row2_5.config(bg="green")
          elif g == 3 and i == 4:
            row3_5.config(bg="green")
          elif g == 4 and i == 4:
            row4_5.config(bg="green")
          elif g == 5 and i == 4:
            row5_5.config(bg="green")
          elif g == 6 and i == 4:
            row6_5.config(bg="green")
        elif gussr[i] in ans and gussr[i]!=ans[i]:
          if g == 1 and i == 0:
            row1_1.config(bg="orange")
          elif g == 2 and i == 0:
            row2_1.config(bg="orange")
          elif g == 3 and i == 0:
            row3_1.config(bg="orange")
          elif g == 4 and i == 0:
            row4_1.config(bg="orange")
          elif g == 5 and i == 0:
            row5_1.config(bg="orange")
          elif g == 6 and i == 0:
            row6_2.config(bg="orange")
          elif g == 1 and i == 1:
            row1_2.config(bg="orange")
          elif g == 2 and i == 1:
            row2_2.config(bg="orange")
          elif g == 3 and i == 1:
            row3_2.config(bg="orange")
          elif g == 4 and i == 1:
            row4_2.config(bg="orange")
          elif g == 5 and i == 1:
            row5_2.config(bg="orange")
          elif g == 6 and i == 1:
            row6_2.config(bg="orange")
          elif g == 1 and i == 2:
            row1_3.config(bg="orange")
          elif g == 2 and i == 2:
            row2_3.config(bg="orange")
          elif g == 3 and i == 2:
            row3_3.config(bg="orange")
          elif g == 4 and i == 2:
            row4_3.config(bg="orange")
          elif g == 5 and i == 2:
            row5_3.config(bg="orange")
          elif g == 6 and i == 2:
            row6_3.config(bg="orange")
          elif g == 1 and i == 3:
            row1_4.config(bg="orange")
          elif g == 2 and i == 3:
            row2_4.config(bg="orange")
          elif g == 3 and i == 3:
            row3_4.config(bg="orange")
          elif g == 4 and i == 3:
            row4_4.config(bg="orange")
          elif g == 5 and i == 3:
            row5_4.config(bg="orange")
          elif g == 6 and i == 3:
            row6_4.config(bg="orange")
          elif g == 1 and i == 4:
            row1_5.config(bg="orange")
          elif g == 2 and i == 4:
            row2_5.config(bg="orange")
          elif g == 3 and i == 4:
            row3_5.config(bg="orange")
          elif g == 4 and i == 4:
            row4_5.config(bg="orange")
          elif g == 5 and i == 4:
            row5_5.config(bg="orange")
          elif g == 6 and i == 4:
            row6_5.config(bg="orange")
      g = g + 1
def clear():
  user.delete(0,tk.END)
button3 = tk.Button(frame7,bg="grey",fg="white",text="Enter",command=enter)
button3.pack(side = tk.LEFT,padx=4,pady=4)
button4 = tk.Button(frame7,bg="grey",fg="white",text="Clear",command=clear)
button4.pack(side = tk.LEFT,padx=4,pady=4)

root.mainloop()
