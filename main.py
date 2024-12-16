import random
from tkinter import *


def play(user_choice):
    options=["TAS","KAGIT","MAKAS"]
    computer_choice=random.choice(options)

    if user_choice == computer_choice:
        result=f"Berabere! Bilgisayar da {computer_choice} secti."

    elif (user_choice=="TAS" and computer_choice=="MAKAS") or \
        (user_choice=="KAGIT" and computer_choice=="TAS") or \
        (user_choice=="MAKAS" and computer_choice=="KAGIT"):
     result=f"Tebrikler! Bilgisayar {computer_choice} secti.Kazandiniz."
    else:
        result=f"Kaybettiniz! Bilgisayar {computer_choice} secti."

    result_label.config(text=result)

#screen
window=Tk()
window.title("Tas,Kagit,Makas")
window.minsize(width=250,height=350)

info_label=Label(window,text="Bir secim yapiniz", font=("Arial",14),bg="Red", fg="white")
info_label.pack(pady=10)

button_switch=Frame(window)
button_switch.pack(pady=10)

Button(button_switch, text="TAS", font=("arial",12), command=lambda: play("TAS")).pack(side="left", padx=10)
Button(button_switch, text="KAGIT", font=("arial",12), command=lambda: play("KAGIT")).pack(side="left", padx=10)
Button(button_switch, text="MAKAS", font=("arial",12), command=lambda: play("MAKAS")).pack(side="left", padx=10)

result_label=Label(window,text="", font=("Arial",16),bg="Blue", fg="white")
result_label.pack(pady=20)

window.mainloop()