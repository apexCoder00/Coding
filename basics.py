import tkinter as t



# btn = t.Button(window, text = "click me").grid(row=0,column=0)
# # pack, grid

# t.Entry().grid(row=0, column=1)
# t.Label(window, text = "This is a text").grid(row=0, column=2)   

expression = ""

def button_pressed(num):
    global expression
    expression = expression + str(num)
    value.set(expression)


# lambda

def resetAC():
    global expression
    expression = ""
    value.set(expression)

def equals():
    global expression
    # error handlers
    try:
        expression = eval(expression)
        value.set(expression)
        expression = ""
        
    except:
        value.set("ERROR")
        expression = ""


if __name__ == "__main__":

    window = t.Tk()
    window.geometry("500x500")

    value = t.StringVar()

    output = t.Entry(textvariable=value).grid(row=0, column=1)

    one = t.Button(window, text = "1", command= lambda: button_pressed(1)).grid(row=1,column=0)
    two = t.Button(window, text="2",  command= lambda: button_pressed(2)).grid(row=1, column=1)
    three = t.Button(window, text="3", command = lambda: button_pressed(3)).grid(row=1, column=2)
    four = t.Button(window, text="4", command = lambda: button_pressed(4)).grid(row=2, column=0)
    five=t.Button(window, text="5",  command = lambda: button_pressed(5)).grid(row=2, column=1)
    six = t.Button(window, text="6", command = lambda: button_pressed(6)).grid(row=2, column=2)
    seven = t.Button(window, text="7", command = lambda: button_pressed(7)).grid(row = 3, column=0)
    eight = t.Button(window, text="8", command = lambda: button_pressed(8)).grid(row = 3, column = 1)
    nine = t.Button(window, text="9", command = lambda: button_pressed(9)) .grid(row = 3, column = 2 )
    zero = t.Button(window, text="0", command = lambda: button_pressed(0)).grid(row = 4, column = 1 ) 
    dec = t.Button(window, text = ".", command = lambda: button_pressed(".")).grid(row = 4, column = 0)
    reset = t.Button(window, text = "AC", command = lambda: resetAC()).grid(row = 4, column = 2)  
    add = t.Button(window, text="+", command = lambda: button_pressed("+")).grid(row=1, column=5)
    minus=t.Button(window, text="-", command = lambda: button_pressed("-")).grid(row=2, column=5)
    multiply= t.Button(window, text ="*", command = lambda: button_pressed("*")).grid(row=3, column = 5)
    divide = t.Button(window, text = "/", command = lambda: button_pressed("/")).grid(row=4, column=5)
    equal= t.Button(window, text="=", width= "5", command = lambda: equals()).grid(row=0, column = 4)


# btn_pack()

    window.mainloop()