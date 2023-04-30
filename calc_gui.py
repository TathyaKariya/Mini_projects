'''GUI implementaion module'''
import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    """OUTPUT showing function."""
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calcultion():
    '''evaluating values for the given input'''
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    '''clearing the whole function'''
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

#creating an object for graphical user interface.
base=tk.Tk()
base.geometry("300x275")

#text_result is output window size and design.
text_result=tk.Text(base, height="2",width="16",font=("Vladimir Script", 24))
text_result.grid(columnspan=5)
#1
btn_1=tk.Button(base, text="1", command= lambda: add_to_calculation(1),width=5,font=("Arial", 14))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(base, text="2", command= lambda: add_to_calculation(2),width=5,font=("Arial", 14))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(base, text="3", command= lambda: add_to_calculation(3),width=5,font=("Arial", 14))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(base, text="4", command= lambda: add_to_calculation(4),width=5,font=("Arial", 14))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(base, text="5", command= lambda: add_to_calculation(5),width=5,font=("Arial", 14))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(base, text="6", command= lambda: add_to_calculation(6),width=5,font=("Arial", 14))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(base, text="7", command= lambda: add_to_calculation(7),width=5,font=("Arial", 14))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(base, text="8", command= lambda: add_to_calculation(8),width=5,font=("Arial", 14))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(base, text="9", command= lambda: add_to_calculation(9),width=5,font=("Arial", 14))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(base, text="0", command= lambda: add_to_calculation(0),width=5,font=("Arial", 14))
btn_0.grid(row=5,column=2)
#9,0
#expressions
btn_plus=tk.Button(base, text="+",
                    command= lambda: add_to_calculation(str("+")),width=5,font=("Arial", 14))
btn_plus.grid(row=2,column=4)
btn_subtract=tk.Button(base, text="-",
                        command= lambda: add_to_calculation(str("-")),width=5,font=("Arial", 14))
btn_subtract.grid(row=3,column=4)
btn_multiply=tk.Button(base, text="*",
                        command= lambda: add_to_calculation(str("*")),width=5,font=("Arial", 14))
btn_multiply.grid(row=4,column=4)
btn_divide=tk.Button(base, text="/",
                      command= lambda: add_to_calculation(str("/")),width=5,font=("Arial", 14))
btn_divide.grid(row=5,column=4)
#parenthesis
btn_opparen=tk.Button(base, text="(",
                       command= lambda: add_to_calculation(str("(")),width=5,font=("Arial", 14))
btn_opparen.grid(row=5,column=1)
btn_closeparen=tk.Button(base, text=")",
                          command= lambda: add_to_calculation(str(")")),width=5,font=("Arial", 14))
btn_closeparen.grid(row=5,column=3)
#clear & equlas
btn_clear=tk.Button(base, text="CLEAR", command=clear_field,width=11,font=("Arial", 14))
btn_clear.grid(row=6,column=1,columnspan=2)
btn_equals=tk.Button(base, text="=", command= evaluate_calcultion,width=11,font=("Arial", 14))
btn_equals.grid(row=6,column=3,columnspan=2)
#running the main loop
base.mainloop()
