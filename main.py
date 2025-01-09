from tkinter import *
from tkinter import ttk
from random import *
from Bubblesort import bubbleSort
from BogoSort import bogosort
from InsertionSort import insertionSort
from MergeSort import *
from QuickSort import tempQuickSort


root = Tk()
root.title("Sorting Algorithms")
root.geometry("1500x1000")
root.config(background="#274186")
algo = StringVar()
data=[]
minSize=1
maxSize=1




timeOfCompletion=0
totalSwaps=0
writesToAuxilaryArray=0
writesToMainArray=0

def ZeroDivisionErrorPopUp():
    zero =Toplevel(root)
    zero_width=500
    zero_height=400

    zero.title("zero Window")
    zero.config(background="cyan")

    root_width=root.winfo_screenwidth()
    root_height=root.winfo_screenheight()

    pos_Left=int(root_height/2 - zero_height/2)
    pos_Right=int(root_width/2 - zero_width/2)


    zero.geometry(f"{zero_width}x{zero_height}+{pos_Right}+{pos_Left}")
    
    labelEroor = Label(zero,text="please select atleast one size array",font=("Z003",20,"bold")
                       ,anchor="center",justify='center'
                       ,background="cyan"
                       )
    labelEroor.pack(pady=100)

    closeButton=Button(zero,text="Close",command=zero.destroy
                       ,background="red",fg="orange",font=("MathJax_AMS",10,"bold")
        )
    closeButton.pack(pady=10)



    zero.mainloop()


def popForSelectAlgo():
    selectAlgo=Toplevel(root)
    algo_width=500
    algo_height=400

    selectAlgo.title("Select Algo Window")
    selectAlgo.config(background="cyan")

    root_width=root.winfo_screenwidth()
    root_height=root.winfo_screenheight()

    pos_Left=int(root_height/2 - algo_height/2)
    pos_Right=int(root_width/2 - algo_width/2)


    selectAlgo.geometry(f"{algo_width}x{algo_height}+{pos_Right}+{pos_Left}")
    
    labelEroor = Label(selectAlgo,text="please select atleast one Algorithm",font=("Z003",20,"bold")
                       ,anchor="center",justify='center'
                       ,background="cyan"
                       )
    labelEroor.pack(pady=100)

    closeButton=Button(selectAlgo,text="Close",command=selectAlgo.destroy
                       ,background="red",fg="orange",font=("MathJax_AMS",10,"bold")
        )
    closeButton.pack(pady=10)



    selectAlgo.mainloop()



def printAlgoStates():
    global timeOfCompletion, totalSwaps, writesToAuxilaryArray, writesToMainArray

    print(timeOfCompletion, totalSwaps, writesToAuxilaryArray, writesToMainArray)

    child_height = 300
    child_width = 400
    text_size = 12

    root_height = root.winfo_screenheight()
    root_width = root.winfo_screenwidth()

    pos_left = int(root_height / 2 - child_height / 2)
    pos_right = int(root_width / 2)

    child = Toplevel(root)
    iconimage = PhotoImage(file=r"dragon.png")  
    child.iconphoto(True, iconimage)
    child.title("Algorithm Statistics")
    child.config(bg="#249388")
    child.geometry(f"{child_width}x{child_height}+{pos_right}+{pos_left}")

    vline1 = Canvas(child, width=1, height=child_height, bg="black")
    vline1.grid(row=0, column=1, rowspan=4, sticky="ns")

    label1 = Label(child, text="Time:", font=f"Georgia {text_size} italic bold", anchor="w", padx=20, bg="#249388")
    label1.grid(row=0, column=0, sticky="w")

    label2 = Label(child, text=timeOfCompletion, font=("Arial", 12), anchor="w", bg="#249388")
    label2.grid(row=0, column=2, padx=30, sticky="w")

    label3 = Label(child, text="Total Swaps:", font=f"Georgia {text_size} italic bold", anchor="w", padx=20, bg="#249388")
    label3.grid(row=1, column=0, sticky="w")

    label4 = Label(child, text=str(totalSwaps), font=("Arial", 12), anchor="w", bg="#249388")
    label4.grid(row=1, column=2, padx=30, sticky="w")

    label5 = Label(child, text="Writes to Auxiliary Array:", font=f"Georgia {text_size} italic bold", anchor="w", padx=20, bg="#249388")
    label5.grid(row=2, column=0, sticky="w")

    label6 = Label(child, text=writesToAuxilaryArray, font=("Arial", 12), anchor="w", bg="#249388")
    label6.grid(row=2, column=2, padx=30, sticky="w")

    label7 = Label(child, text="Writes to Main Array:", font=f"Georgia {text_size} italic bold", anchor="w", padx=20, bg="#249388")
    label7.grid(row=3, column=0, sticky="w")

    label8 = Label(child, text=writesToMainArray, font=("Arial", 12), anchor="w", bg="#249388")
    label8.grid(row=3, column=2, padx=30, sticky="w")

    child.mainloop()


def startAlgo():
    global timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray
    sleeptime= speed.get()
    algo_name=algo.get()
    if sleeptime==0:
        #like if sleeptime is 0 1ms extremely fast
        sleeptime=0.01

    print(algo,algo_name)
    if algo_name=="Bubble sort":
        timeOfCompletion, totalSwaps, writesToAuxilaryArray, writesToMainArray=bubbleSort(data,drawData,sleeptime)
    elif algo_name=="Insertion sort":
        timeOfCompletion, totalSwaps, writesToAuxilaryArray, writesToMainArray=insertionSort(data,drawData,sleeptime)

    elif algo_name=="Merge Sort":
        timeOfCompletion, totalSwaps, writesToAuxilaryArray, writesToMainArray=merge_sort(data,drawData,sleeptime)
    elif algo_name=="Quick Sort":
        timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray=tempQuickSort(data,0,len(data),drawData,sleeptime)
    elif algo_name=="Bogo Sort":
        timeOfCompletion,totalSwaps,writesToAuxilaryArray,writesToMainArray = bogosort(data,drawData,sleeptime)
    else:
        popForSelectAlgo()
        return
       #making theh window for atleats one algo
    printAlgoStates()
def drawData(data,colorArray):
    

    canvas_width = canvas.winfo_width()
    canvas_height= canvas.winfo_height()

    try:
        rec_width=canvas_width/(len(data))
    except ZeroDivisionError:
        ZeroDivisionErrorPopUp()
    padding_top=50


    offset = 10
    spacing_bet_rec=1
    normalizedData = [ i / max(data) if max(data) > 0 else 0 for i in data ]
    canvas.delete("all")
    max_height = max(normalizedData) if normalizedData else 1
    font_size = max(8, 20 - len(data) // 10)

     
    for i, height in enumerate(normalizedData):
        # Calculate the starting "x" position for normalize to fit in frame :)
        x0 = i * rec_width + (1* spacing_bet_rec)  
        # Starting y position liek to  normalized height
        y0 = canvas_height - (height * (canvas_height-padding_top))  
        y0= max(y0,padding_top)
        
         # Ending x position
        x1 = x0 + rec_width 
        y1 = canvas_height 

        # Draw rectangle--
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        
        # Place text in the middle of the rectangle, above it
        canvas.create_text(x0 + rec_width / 2 , y0-10, anchor="center",
                            text=str(data[i]), fill="orange", font=("Arial",font_size,"bold"))
    root.update_idletasks()

def randomGenrateData():
    print(minSize.get() , maxSize.get(),size.get())
    min_size = minSize.get()
    max_size= maxSize.get()
    len= size.get() 

    l= [] 
    for i in range(len):
        randomNum = randint(min_size,max_size+1)
        l.append(randomNum)
    return l


def GENERATE():
    global data
    global minSize
    global maxSize


    print("GENERATING function"+algo.get() )
    
    
    if minSize.get() > maxSize.get():
        maxSize,minSize=minSize,maxSize

    data= randomGenrateData()
    colorArray= ['Blue' for x in range(len(data))]
    drawData(data,colorArray)

        


# Algorithm Label
AlgorithmMenu = Label(root, text="Algorithm: ", font="Arial 15 italic bold", bg="blue", width=15)
AlgorithmMenu.grid(row=0, column=0, padx=20, pady=8)

# Algorithm Dropdown Menu
algo_menu = ttk.Combobox(root, font="bold", textvariable=algo, values=['Bubble sort', 'Insertion sort', 'Merge Sort','Quick Sort','Bogo Sort'], width=15)
algo_menu.grid(row=0, column=1, padx=10, pady=8)

# Input Size Label and Scale
sizeLabel = Label(root, text="Input Size:", font="Courier 15 italic bold", bg="green", relief="solid", width=15)
sizeLabel.grid(row=1, column=0, padx=20, pady=8)
size = Scale(root, from_=0, to=100, orient="horizontal", font="Courier 15 italic bold", bg="green", relief="solid", width=15)
size.grid(row=1, column=1, padx=20, pady=8)

# Minimum Size Label and Scale
minLabel = Label(root, text="Minimum", font="Courier 15 italic bold", bg="blue", relief="solid", width=15)
minLabel.grid(row=1, column=2, padx=20, pady=8)
minSize = Scale(root, from_=0, to=100, orient="horizontal", font="Courier 15 italic bold", bg="green", relief="solid", width=15)
minSize.grid(row=1, column=3, padx=20, pady=8)

# Maximum Size Label and Scale
maxLabel = Label(root, text="Maximum", font="Courier 15 italic bold", bg="blue", relief="solid", width=15)
maxLabel.grid(row=1, column=4, padx=20, pady=8 )
maxSize = Scale(root, from_=0, to=100, orient="horizontal", font="Courier 15 italic bold", bg="green", relief="solid", width=15)
maxSize.grid(row=1, column=5, padx=20, pady=8)

# Generate Button
randomGenerate = Button(root, text="GENERATE", bg="cyan", font="Georgia 15 italic bold", relief='sunken', width=15, command=GENERATE)
randomGenerate.grid(row=1, column=6, padx=20, pady=8)

# Speed Label and Scale
speedLabel = Label(root, text="Speed", font="Arial 15 italic bold", bg="blue", width=15)
speedLabel.grid(row=0, column=2, padx=20, pady=8 )
speed = Scale(root, from_=0, to=5,resolution=0.2, orient="horizontal", font="Courier 15 italic bold", bg="green", relief="solid", width=15
              )
speed.grid(row=0, column=3, padx=20, pady=8)

# Start Button
start = Button(root, text="Start", bg="cyan",command=startAlgo, font="Georgia 15 italic bold", relief='sunken', width=15)
start.grid(row=0, column=4, padx=20, pady=8)

# Configure row weights to allow the canvas to fill available space
root.grid_rowconfigure(2, weight=1)  # This is the row where the canvas is
root.grid_columnconfigure(0, weight=1)  # Optional: allows the first column to expand

# Canvas
canvas = Canvas(root, bg="black")
canvas.grid(row=2, columnspan=7, padx=20, pady=20, sticky='nsew')  # Fill all columns and stretch



root.mainloop()