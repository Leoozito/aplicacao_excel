from tkinter import *
import subprocess

app = Tk()
app.title("Total dos Pagamentos Mensais")
app.geometry("600x320")
app.configure(background="#008")

def on_enter(event):
    event.widget.configure(background="white")  # Muda a cor de fundo para amarelo quando o mouse entra no botão

def on_leave(event):
    event.widget.configure(background="yellow")  # Restaura a cor de fundo original (branca) quando o mouse sai do botão

def executar_arquivo():
    subprocess.Popen(["python", "main.py"])

# Especifique a cor de fundo original explicitamente como "white"
btn1 = Button(app, text="Total 1° Pagamento", background="yellow", foreground="#000")
btn1.place(x=220, y=20, width=150, height=30)
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)

btn2 = Button(app, text="Total 2° Pagamento", background="yellow", foreground="#000")
btn2.place(x=220, y=70, width=150, height=30)
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

btn3 = Button(app, text="Total 3° Pagamento", background="yellow", foreground="#000")
btn3.place(x=220, y=120, width=150, height=30)
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)

btn4 = Button(app, text="Total 4° Pagamento", background="yellow", foreground="#000")
btn4.place(x=220, y=170, width=150, height=30)
btn4.bind("<Enter>", on_enter)
btn4.bind("<Leave>", on_leave)

btn5 = Button(app, text="Total 5° Pagamento", background="yellow", foreground="#000")
btn5.place(x=220, y=220, width=150, height=30)
btn5.bind("<Enter>", on_enter)
btn5.bind("<Leave>", on_leave)

btn6 = Button(app, text="Total dos Pagamentos Mensais", background="white", foreground="#000", command=executar_arquivo)
btn6.place(x=180, y=270, width=240, height=50)
btn6.bind("<Enter>", on_enter)
btn6.bind("<Leave>", on_leave)

app.mainloop()