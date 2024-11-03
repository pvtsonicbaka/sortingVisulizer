from tkinter import *
from random import *
from tkinter import ttk
root=Tk()
root.title("Sorting some alogorithms")
root.geometry("1500x1000")
root.config(background="black")

algo=StringVar()

AlgortithmMenu = Label(root,text="Algortihm",font="Arial 15 italic bold" ,bg="blue",
width="10"
)
AlgortithmMenu.place(x="10",y="10")

algo_menu= ttk.Combobox(root,font="bold" ,textvariable=algo,values=['Bubble sort','Insetion sort','Merge Sort'],
                        width="10"
                        )
algo_menu.place(x="130",y="11")

root.mainloop()