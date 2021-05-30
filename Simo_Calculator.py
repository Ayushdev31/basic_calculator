from tkinter import *

"""
    this is a self-made GUI Calculator
    with lesser functions
    Beginner project--01
"""

# main window initialized
root = Tk()

# variables:
root_wid = 370
root_hei = 275
expression = ""
equation = StringVar()

# window size configuration:
root.geometry(f"{root_wid}x{root_hei}")
root.maxsize(root_wid, root_hei)
root.minsize(root_wid, root_hei)
root.title("Simple Calculator GUI")


# functions:
def press(num):
    """function to be used in buttons to take the input as a string"""
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    """This function is to be used in equal button to evaluate the input with python function eval()"""
    try:
        global expression
        # converting the result into a string variable
        total = str(eval(expression))
        equation.set(total)

    except:
        equation.set("Not Possible")
        expression = ""


def press_clear():
    """This functions helps to clear the Text Box in the clear button"""
    global expression
    equation.set("")
    expression = ""


# All the buttons initialized:

b1 = Button(root, fg='black', bg='light yellow', text="1", borderwidth=6, padx=23, pady=18, command=lambda: press(1)) \
    .grid(row=1, column=0)
b2 = Button(root, fg='black', bg='light yellow', text="2", borderwidth=6, padx=23, pady=18, command=lambda: press(2)) \
    .grid(row=1, column=1)
b3 = Button(root, fg='black', bg='light yellow', text="3", borderwidth=6, padx=23, pady=18, command=lambda: press(3)) \
    .grid(row=1, column=2)
b4 = Button(root, fg='black', bg='light yellow', text="4", borderwidth=6, padx=23, pady=18, command=lambda: press(4)) \
    .grid(row=1, column=3)
b5 = Button(root, fg='black', bg='light yellow', text="5", borderwidth=6, padx=23, pady=18, command=lambda: press(5)) \
    .grid(row=2, column=0)
b6 = Button(root, fg='black', bg='light yellow', text="6", borderwidth=6, padx=23, pady=18, command=lambda: press(6)) \
    .grid(row=2, column=1)
b7 = Button(root, fg='black', bg='light yellow', text="7", borderwidth=6, padx=23, pady=18, command=lambda: press(7)) \
    .grid(row=2, column=2)
b8 = Button(root, fg='black', bg='light yellow', text="8", borderwidth=6, padx=23, pady=18, command=lambda: press(8)) \
    .grid(row=2, column=3)
b9 = Button(root, fg='black', bg='light yellow', text="9", borderwidth=6, padx=23, pady=18, command=lambda: press(9)) \
    .grid(row=3, column=1)
b0 = Button(root, fg='black', bg='light yellow', text="0", borderwidth=6, padx=23, pady=18, command=lambda: press(0)) \
    .grid(row=3, column=2)
b_equals = Button(root, fg='black', bg='yellow', text="=", borderwidth=6, padx=23, pady=18, command=equal_press) \
    .grid(row=3, column=0)
b_clear = Button(root, fg='black', bg='yellow', text="<X>", borderwidth=6, padx=23, pady=18, command=press_clear) \
    .grid(row=3, column=3)
b_entry = Entry(root, textvariable=equation, relief=SUNKEN).grid(columnspan=5, ipadx=70, row=0, column=0)
b_plus = Button(root, fg='black', bg='violet', text="+", borderwidth=6, padx=23, pady=18, command=lambda: press('+')) \
    .grid(row=0, column=5)
b_minus = Button(root, fg='black', bg='violet', text="-", borderwidth=6, padx=23, pady=18, command=lambda: press('-')) \
    .grid(row=1, column=5)
b_mul = Button(root, fg='black', bg='violet', text="x", borderwidth=6, padx=23, pady=18, command=lambda: press('*')) \
    .grid(row=2, column=5)
b_div = Button(root, fg='black', bg='violet', text="%", borderwidth=6, padx=23, pady=18, command=lambda: press('/')) \
    .grid(row=3, column=5)

# main loop started:
mainloop()
