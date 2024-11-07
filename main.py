from tkinter import *
from random import *
from tkinter import ttk
from Bubblesort import bubbleSort
from BogoSort import bogosort
# from InsertionSort import insertionSort
# from MergeSort import mergeSort 
from QuickSort import quicksort


root = Tk()
root.title("Sorting Algorithms")
root.geometry("1500x1000")
root.config(background="#274186")
algo = StringVar()
data=[]
minSize=1
maxSize=1





def startAlgo():
    sleeptime= speed.get()
    
    length=len(data)
    quicksort(data,0,length,drawData,sleeptime)
    drawData(data,['green' for x in range(len(data))])
    print(data)
    # if algo=="Bubble sort":
        # bubbleSort(data,drawData,sleeptime)
    # elif algo=="Insertion sort":
    #     insertionSort(data,drawData,sleeptime)
    # elif algo=="Merge Sort":
    #     mergeSort(data,drawData,sleeptime)
    # elif algo=="Quick Sort":
    #     print("i")
    # elif algo=="Bogo Sort":
    #     print("remaming")

        

def drawData(data,colorArray):
    

    canvas_width = canvas.winfo_width()
    canvas_height= canvas.winfo_height()


    rec_width=canvas_width/(len(data))
    padding_top=50


    offset = 10
    spacing_bet_rec=1
    normalizedData = [ i / max(data) if max(data) > 0 else 0 for i in data ]
    canvas.delete("all")
    max_height = max(normalizedData) if normalizedData else 1
    font_size = max(8, 20 - len(data) // 10)

     
    for i, height in enumerate(normalizedData):
        x0 = i * rec_width + (1* spacing_bet_rec)  # Calculate the starting x position
        y0 = canvas_height - (height * (canvas_height-padding_top))  # Starting y position based on normalized height
        y0= max(y0,padding_top)
        
        x1 = x0 + rec_width  # Ending x position
        y1 = canvas_height  # Bottom of the canvas

        # Draw rectangle
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