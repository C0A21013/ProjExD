import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    n = btn["text"]

    if n == "=":
        ikolove = entry.get()      # 数式の文字列
        res = eval(ikolove)        # 数式文字列の評価
        entry.delete(0, tk.END)    # 表示文字列の削除
        entry.insert(tk.END, res)  # 結果の挿入


    else:
        #tkm.showinfo("", f"[{n}]ボタンが押されました")
        entry.insert(tk.END, n)


root = tk.Tk()
root.geometry("400x650")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row = 0, column=0, columnspan=3) 

r,c = 1,0
for n in range(9, -1, -1):
    button = tk.Button(root, text=f"{n}",width=4, height=2, font=("", 30))    
    button.grid(row = r, column = c)
    button.bind("<1>", button_click)
    c += 1
    if c % 3 ==0:
        r += 1
        c = 0

operators = ["+","-","/","*"]  #四則演算
iko = ["="]
r = 1
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=3)
    button.bind("<1>", button_click)
    r += 1

for ope in iko:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=4, column=2)
    button.bind("<1>", button_click)
    r += 1

    #c += 1
    #if c%3 == 0:
        #r += 1
        #c = 0

root.mainloop()


