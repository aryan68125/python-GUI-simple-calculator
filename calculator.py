from tkinter import *
#import message box to create a pop up window of information display type
from tkinter import messagebox
window = Tk()

#--------writing the actual logic inside the functions-------------

#since functions dont have the ability to pass the variable's value among themselves
#hence we are going to use a global variable so that that variable can be acessed by all the mathematical functions
#global variable

#this function will deal with the buttons having numbers
def button_clicked(number):
	#insert(0,number) allows us to insert the number from button into editText input field
	#0= index at which the new string will be inserted
	#number = passed value from button to this function by using lambda
	entry.insert(100,number)

#this functions will deal with the clear button
def button_clear():
	#entry.delete(0,END) will delete the entire string that has been entered by the suer in the app
	#it will start at 0 position and go all the way to the END and then delete the entire string in the input field
	entry.delete(0,END)

#the functions below will deal with the mathamatical operations of this calculator
def button_add():
    #checking if the input field is empty or not
    if entry.get()=="":
    	entry.insert(0,"input field is empty!")
    else:
	    #entry.get() will pull the entered string from the input field
	    first_number=float(entry.get()) #typecasting it to an integer
	    #now we are going to declare a global variable that we talked about 
	    global f_num #we can use f_num outside of this function even though its declared inside this function
	    f_num = first_number
	    global operator
	    operator = "addition"
	    #clear the input field
	    entry.delete(0,END)
	    return
def button_subtract():
    #checking if the input field is empty or not
    if entry.get()=="":
    	entry.insert(0,"input field is empty!")
    else:
	    #entry.get() will pull the entered string from the input field
	    first_number=float(entry.get()) #typecasting it to an integer
	    #now we are going to declare a global variable that we talked about 
	    global f_num #we can use f_num outside of this function even though its declared inside this function
	    f_num = first_number
	    global operator
	    operator = "subtract"
	    #clear the input field
	    entry.delete(0,END)

def button_multiply():
    #checking if the input field is empty or not
    if entry.get()=="":
    	entry.insert(0,"input field is empty!")
    else:
	    #entry.get() will pull the entered string from the input field
	    first_number=float(entry.get()) #typecasting it to an integer
	    #now we are going to declare a global variable that we talked about 
	    global f_num #we can use f_num outside of this function even though its declared inside this function
	    f_num = first_number
	    global operator
	    operator = "multiply"
	    #clear the input field
	    entry.delete(0,END)

def button_divide():
    #checking if the input field is empty or not
    if entry.get()=="":
    	entry.insert(0,"input field is empty!")
    else:
	    #entry.get() will pull the entered string from the input field
	    first_number=float(entry.get()) #typecasting it to an integer
	    #now we are going to declare a global variable that we talked about 
	    global f_num #we can use f_num outside of this function even though its declared inside this function
	    f_num = first_number
	    global operator
	    operator = "divide"
	    #clear the input field
	    entry.delete(0,END)

def button_power():
    #checking if the input field is empty or not
    if entry.get()=="":
    	entry.insert(0,"input field is empty!")
    else:
	    #entry.get() will pull the entered string from the input field
	    first_number=float(entry.get()) #typecasting it to an integer
	    #now we are going to declare a global variable that we talked about 
	    global f_num #we can use f_num outside of this function even though its declared inside this function
	    f_num = first_number
	    global operator
	    operator = "Power"
	    #clear the input field
	    entry.delete(0,END)

#this function deals with the equals button
def button_equals():
    if entry.get()=="":
        entry.insert(0,"input field is empty!")
    else:
        second_number=float(entry.get())
        entry.delete(0,END)
        if operator=="addition":
            ans=f_num + second_number
            answer=str(ans)
            entry.insert(0,answer)
        if operator=="subtract":
            ans=f_num - second_number
            answer=str(ans)
            entry.insert(0,answer)
        if operator=="multiply":
            ans=f_num * second_number
            answer=str(ans)
            entry.insert(0,answer)
        if operator=="divide":
            ans=f_num / second_number
            answer=str(ans)
            entry.insert(0,answer)
        if operator=="Power":
            ans=f_num**second_number
            answer=str(ans)
            entry.insert(0,answer)
       
#------creating widgets and GUI window components------
#generating window title
window.title("calculator")

#creating an input field like editText in android in application
#width will allow us to make the input editText larger across x axis
entry = Entry(window, width = 15, borderwidth = 5)

#now we need to create buttons
#numeric buttons, lambda: myfunction(passing value)
buttonOne = Button(window, text="1",command = lambda: button_clicked(1),padx=20,pady=20)
buttonTwo = Button(window, text="2",command = lambda: button_clicked(2),padx=20,pady=20)
buttonThree = Button(window, text="3",command = lambda: button_clicked(3),padx=20,pady=20)
buttonFour = Button(window, text="4",command = lambda: button_clicked(4),padx=20,pady=20)
buttonFive = Button(window, text="5",command = lambda: button_clicked(5),padx=20,pady=20)
buttonSix = Button(window, text="6",command = lambda: button_clicked(6),padx=20,pady=20)
buttonSeven = Button(window, text="7",command = lambda: button_clicked(7),padx=20,pady=20)
buttonEight = Button(window, text="8",command = lambda: button_clicked(8),padx=20,pady=20)
buttonNine = Button(window, text="9",command = lambda: button_clicked(9),padx=20,pady=20)
buttonZero = Button(window, text="0",command = lambda: button_clicked(0),padx=20,pady=20)
#mathematic operation buttons
buttonAdd = Button(window,text = "+",command = lambda: button_add(),padx=20,pady=20)
buttonSub = Button(window, text="-",command = lambda: button_subtract(),padx=20,pady=20)
buttonMul = Button(window, text="X",command = lambda: button_multiply(),padx=20,pady=20)
buttonDivide = Button(window, text="/",command = lambda: button_divide(),padx=20,pady=20)
buttonEquals = Button(window, text="=",command = lambda: button_equals(),padx=20,pady=20)
buttonPower = Button(window, text="^",command = lambda: button_power(),padx=20,pady=20)
buttonDot = Button(window,text=".",command = lambda: button_clicked("."),padx=20,pady=20)
buttonClear = Button(window,command = lambda: button_clear(),text="C",padx=20,pady=20)

# ------putting widets and GUI window components on the screen---------

#input feild editText
#columnspan = 4 :-it will make the input field span across 4 columns in the grid
entry.grid(row=0,column=0, columnspan=4, padx = 20, pady=20)

#buttons
buttonOne.grid(row=1,column=0)
buttonTwo.grid(row=1,column=1)
buttonThree.grid(row=1,column=2)
buttonAdd.grid(row=1,column=3)

buttonFour.grid(row=2,column=0)
buttonFive.grid(row=2,column=1)
buttonSix.grid(row=2,column=2)
buttonSub.grid(row=2,column=3)

buttonSeven.grid(row=3,column=0)
buttonEight.grid(row=3,column=1)
buttonNine.grid(row=3,column=2)
buttonMul.grid(row=3,column=3)

buttonDot.grid(row=4,column=0)
buttonZero.grid(row=4,column=1)
buttonPower.grid(row=4,column=2)
buttonDivide.grid(row=4,column=3)

buttonEquals.grid(row=5,column=3)
buttonClear.grid(row=5,column=2)

#creating a function for our pop up window
def dev():
    #create a message box showinfo will just show some kind of information on the pop up window it is not interactive
    #showinfo("the title bar that you want to show up", message that you want to show in your actual pop up window)
    messagebox.showinfo("developer info", "Name = Aditya Kumar \n class = B.tech 2nd year \n college = SITM \n Roll number = 1901230100001")

#now here we are going to create a button which when clicked will trigger a popup window
ButtonDev = Button(window,text="Developer information",command = dev).grid(row=6,column=0,columnspan=4, padx = 20, pady=20)

window.mainloop()