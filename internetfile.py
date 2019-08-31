#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import index

def ChangeLabelText(m):
    m.config(text = 'You pressed the button!')
    index.play_song("/Users/vishal/Desktop/Coding B/DevClub/SyncAudio/SyncLyrics/Ed Sheeran - Shape of You [Official Video].mp3", m)

def main():
    Root = Tk()
    MyLabel = ttk.Label(Root, text = 'The button has not been pressed.')
    MyLabel.pack()
    MyButton = ttk.Button(Root, text = 'Press Me', command = lambda: ChangeLabelText(MyLabel))
    MyButton.pack()
    Root.mainloop()

if __name__ == "__main__":
  main()