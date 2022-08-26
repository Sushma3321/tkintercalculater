from tkinter import *


main_window=Tk()
main_window.title('calculater') 


def clear():
    display_box.delet(0, END)


def btn_clk(num):
    cur_num = display_box.get()
    clear()
    f_num = cur_num + num
    display_box.insert(0, f_num)

first_num = 0
math=''

def calc(math_type):
    global first_num, math
    math = math_type
    first_num = display_box.get()
    clear()


def equal():
    result =''
    global first_num
    second_num = display_box.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
    display_box.insert(0, str(result))

    
display_box = Entry(main_window, width=14, font=('arial', 28), justify=RIGHT)


button_0 = Button(main_window, text='0', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('0'))
button_1 = Button(main_window, text='1', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('1'))
button_2 = Button(main_window, text='2', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('2'))
button_3 = Button(main_window, text='3', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('3'))
button_4 = Button(main_window, text='4', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('4'))
button_5 = Button(main_window, text='5', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('5'))
button_6 = Button(main_window, text='6', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('6'))
button_7 = Button(main_window, text='7', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('7'))
button_8 = Button(main_window, text='8', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('8'))
button_9 = Button(main_window, text='9', padx=36, pady=10, font=('arial', 14), command=lambda:btn_clk('9'))


button_clear=Button(main_window, text='clear', padx=74, pady=10, font=('arial', 14), command=clear)
button_division=Button(main_window, text='/', padx=38, pady=10, font=('arial', 14), command=lambda:calc('division')
button_mul=Button(main_window, text='*', padx=38, pady=10, font=('arial', 14), command=lambda:calc('muliply')
button_sub=Button(main_window, text='-', padx=38, pady=10, font=('arial', 14), command=lambda:calc('sub')
button_add=Button(main_window, text='+', padx=36, pady=10, font=('arial', 14), command=lambda:calc('add')
button_equal=Button(main_window, text='=', padx=36, pady=40, font=('arial', 14), command=equal)


button_equal.grid(row=5, column=2,rowspan=2, padx=2, pady=2)
button_sub.grid(row=6, column=0, padx=2, pady=2)
button_mul.grid(row=5, column=1, padx=2, pady=2)
button_div.grid(row=5, column=0, padx=2, pady=2)



button_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
button_0.grid(row=4, column=0, padx=2, pady=2)

button_1.grid(row=3, column=0, padx=2, pady=2)
button_2.grid(row=3, column=1, padx=2, pady=2)
button_3.grid(row=3, column=2, padx=2, pady=2)


button_4.grid(row=2, column=0, padx=2, pady=2)
button_5.grid(row=2, column=1, padx=2, pady=2)
button_6.grid(row=2, column=2, padx=2, pady=2)

button_4.grid(row=1, column=0, padx=2, pady=2)
button_5.grid(row=1, column=1, padx=2, pady=2)
button_6.grid(row=1, column=2, padx=2, pady=2)

display_box.grid(row=0, column=0, padx=0, pady=10)

button_1.grid(row=, column=0, padx=2, pady=2)
button_2.grid(row=, column=1, padx=2, pady=2)
button_3.grid(row=, column=2, padx=2, pady=2)

button_4.grid(row=, column=0, padx=2, pady=2)
button_5.grid(row=, column=1, padx=2, pady=2)
button_6.grid(row=, column=2, padx=2, pady=2)

button_7.grid(row=, column=0, padx=2, pady=2)
button_8.grid(row=, column=1, padx=2, pady=2)
button_9.grid(row=, column=2, padx=2, pady=2)

main_window.mainloop()


 

     


     


        

