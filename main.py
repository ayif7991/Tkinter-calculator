from tkinter import *


def expression_update(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))


def perform_operation(operation):
    n1 = e.get()
    global math
    math = operation
    global i
    i = float(n1)
    e.delete(0, END)


# def add():
#     n1 = e.get()
#     global math
#     math = "addition"
#     global i
#     i = int(n1)
#     e.delete(0, END)


# def sub():
#     n1 = e.get()
#     global math
#     math = "substraction"
#     global i
#     i = int(n1)
#     e.delete(0, END)
#
#
# def mul():
#     n1 = e.get()
#     global math
#     math = "multiplication"
#     global i
#     i = int(n1)
#     e.delete(0, END)
#
#
# def div():
#     n1 = e.get()
#     global math
#     math = "division"
#     global i
#     i = int(n1)
#     e.delete(0, END)


def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + float(n2))
    elif math == "substraction":
        e.insert(0, i - float(n2))
    elif math == "multiplication":
        e.insert(0, i * float(n2))
    elif math == "division":
        e.insert(0, i / float(n2))


def clear_field():
    e.delete(0, END)


if __name__ == "__main__":
    win = Tk()
    win.geometry("312x324")
    win.resizable(0, 0)
    win.title("Calculator")
    input_text = StringVar()

    e = Entry(win, textvariable=input_text)
    e.grid(columnspan=4, ipadx=70)

    button1 = Button(win, text=' 1 ', fg='black', bg='grey',
                     command=lambda: expression_update(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(win, text=' 2 ', fg='black', bg='grey',
                     command=lambda: expression_update(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(win, text=' 3 ', fg='black', bg='grey',
                     command=lambda: expression_update(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(win, text=' 4 ', fg='black', bg='grey',
                     command=lambda: expression_update(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(win, text=' 5 ', fg='black', bg='grey',
                     command=lambda: expression_update(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(win, text=' 6 ', fg='black', bg='grey',
                     command=lambda: expression_update(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(win, text=' 7 ', fg='black', bg='grey',
                     command=lambda: expression_update(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(win, text=' 8 ', fg='black', bg='grey',
                     command=lambda: expression_update(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(win, text=' 9 ', fg='black', bg='grey',
                     command=lambda: expression_update(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(win, text=' 0 ', fg='black', bg='grey',
                     command=lambda: expression_update(0), height=1, width=7)
    button0.grid(row=5, column=0)

    # operators
    # addition
    plus = Button(win, text=' + ', fg='black', bg='grey',
                  command=lambda: perform_operation("addition"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(win, text=' - ', fg='black', bg='grey',
                   command=lambda: perform_operation("substraction"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(win, text=' * ', fg='black', bg='grey',
                      command=lambda: perform_operation("multiplication"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(win, text=' / ', fg='black', bg='grey',
                    command=lambda: perform_operation("division"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(win, text=' = ', fg='black', bg='grey',
                   command=equal, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(win, text='Clear', fg='black', bg='grey',
                   command=clear_field, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(win, text='.', fg='black', bg='grey',
                     command=lambda: expression_update('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    win.mainloop()
