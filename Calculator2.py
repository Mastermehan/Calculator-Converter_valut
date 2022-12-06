import tkinter as tk
import math

window = tk.Tk()
window.title('Calculator')
window.geometry('615x550')
window.resizable(False, False)
window.configure(bg='gray10')

def calculate(operation):
    global formula
    num = txt_entry_dollar.get() #считываем c ввода доллара
        
    try:
        if operation == '!':
            return calculate1(operation)
        elif operation == 'C':
            formula = '0'
        elif operation == 'del':
            formula = formula[0:-1]
        elif operation == 'X^2':
            formula = str((eval(formula)) ** 2)
        elif operation == 'X^3':
            formula = str((eval(formula)) ** 3) 
        elif operation == 'Dollar':
            formula = str(eval(formula)/float(num))
        elif operation == '√':
            formula = (str(math.sqrt(eval(formula))))
        elif operation == '!':
            label_text1.configure(text=formula)
     
        elif operation == '=':
            formula = str(eval(formula))
        else:
            if formula == '0':
                formula = ''
            formula += operation
        label_text.configure(text=formula)

    except (ZeroDivisionError, Exception):
         formula = '0'
         label_text.configure(text=formula)
         
#Cоздаем лэйбл и поле ввода доллара
lbl_converter_dollar = tk.Label(window, text="курс доллара или евро", font=('Roboto', 15),  bg='gray10', fg='white')  
lbl_converter_dollar.place(x=17, y=100)

txt_entry_dollar = tk.Entry(window, width=4, bg ='orange', font=('Roboto', 18), justify = 'center')
txt_entry_dollar.pack(anchor='nw', padx=235, pady= 102 )

lbl_converter_dollar_to_rub = tk.Label(window, text="рублей(тут ввод с клавиатуры)", font=('Roboto', 15),  bg='gray10', fg='white')  
lbl_converter_dollar_to_rub.place(x=295, y=100)


#Создание окна для вывода вычислений
formula = '0'
label_text = tk.Label(text=formula,  font=('Roboto', 40, 'bold'), bg='gray10', fg='white', anchor="e")
label_text.place(x=17, y=20)


# Создаем кнопки
buttons = ['C', 'del', '√', '*', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '.', '0', '00', '=']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button,relief = "solid",   bg='deep sky blue', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x +=117
    if x > 400:
        x = 18
        y += 81
        
buttons_new = ['(', ')', 'X^2', 'X^3','Dollar']
x = 486
y = 140
for button in buttons_new:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text=button,relief = "solid",   bg='orange', font=('Roboto', 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 500:
        x = 486
        y += 81

window.mainloop()
