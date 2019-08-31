import tkinter
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import index

def playsong(m):
    m.config(text = 'You pressed the button!')
    print("I am here")
    index.play_song( "/Users/vishal/Desktop/Coding B/DevClub/SyncAudio/SyncLyrics/Ed Sheeran - Shape of You [Official Video].mp3", m)

def main():
    # tkinter.Tk().withdraw()
    # filename = askopenfilename()
    # print(filename)

    # m is the main/master window
    m = tkinter.Tk(screenName="SyncLyrics", className="SyncLyrics")

    MyLabel = ttk.Label(m, text = 'The button has not been pressed.')
    MyLabel.pack()
    MyButton = ttk.Button(m, cursor="cross", text='Play', width=25, command=lambda: playsong(MyLabel))
    MyButton.pack()
    # w = ttk.Button(m, cursor="cross", text='Close', width=25, command=m.destroy)
    # w.grid(row=2)




    # w = tkinter.Canvas(m, width=40, height=60)
    # w.grid(row=1)
    # canvas_height = 20
    # canvas_width = 200
    # y = int(canvas_height / 2)
    # w.create_line(0, y, canvas_width, 100)

    # var1 = tkinter.IntVar()
    # checkbox1 = tkinter.Checkbutton(m, text='male', variable=var1).grid(row=2, sticky=tkinter.W)
    # var2 = tkinter.IntVar()
    # checkbox2 = tkinter.Checkbutton(m, text='female', variable=var2).grid(row=3, sticky=tkinter.W)

    # frame = tkinter.Frame(m)
    # frame.grid(row=4, sticky=tkinter.W)
    # tkinter.Label(frame, text='First Name').grid(row=4, column=0, sticky=tkinter.W)
    # tkinter.Label(frame, text='Last Name').grid(row=5, column=0, sticky=tkinter.W)
    # e1 = tkinter.Entry(frame)
    # e2 = tkinter.Entry(frame)
    # e1.grid(row=4, column=1)
    # e2.grid(row=5, column=1)

    menu = tkinter.Menu(m)
    m.config(menu=menu)

    filemenu = tkinter.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=m.quit)
    helpmenu = tkinter.Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')

    m.mainloop()

if __name__ == "__main__":
  main()

