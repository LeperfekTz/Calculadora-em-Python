import tkinter as tk

def calculadora(operacao):
    global expressao

    if operacao == "C":
        expressao = ""
    elif operacao == "B":
        expressao = expressao[:-1]
    else:
        if expressao == "" and operacao in ["+", "-", "*", "/"]:
            return
        expressao += operacao

    label_text.set(expressao)

def evaluate():
    global expressao
    try:
        result = str(eval(expressao))
        label_text.set(result)
        expressao = result
    except:
        label_text.set("Error")
        expressao = ""

root = tk.Tk()
root.title('Calculadora')

expressao = ""
label_text = tk.StringVar()

label = tk.Label(root, textvariable=label_text, font=("Arial", 30), bg="white", width=15, height=2)
label.grid(row=0, column=0, columnspan=4)
                 
buttons = [
    ("7",1, 0), ("8",1, 1), ("9",1, 2),   ("C",1, 3),
    ("4",2, 0), ("5",2, 1), ("6",2, 2), ("+", 2, 3),
    ("1",3, 0), ("2",3, 1), ("3",3, 2), ("-", 3, 3),
    ("0",4, 0), (".",4, 1), ("B",4, 2),  ("*", 4, 3),
    ("/",5, 0), ("=",5, 1)
]
                 
for text, row, col in buttons: 
    action = lambda x=text: calculadora(x) if x != "=" else evaluate()
    button = tk.Button(root, text=text, command=action, font=("Arial", 30), width=5, height=2)
    button.grid(row=row, column=col)

button = tk.Button(root, text="=", command=evaluate, font=("Arial", 30), width=11, height=2)
button.grid(row=5, column=1, columnspan=2)

root.mainloop()
