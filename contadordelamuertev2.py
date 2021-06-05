'''
Code by: "Lord Petyr"
This is a simple scrip that ask for you name and birthday, then with that data
it makes a regresive count till your dead (the code is supossing that you'll
live 80 years, it could be more or less deppending of your habits, or maybe a accident.)
Value your life, you just have one and with limited time.

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/.
'''
import time
import datetime
import tkinter as tk
from os import system
leftyears = 80 #años de vida esperados
leftdays = leftyears * 365.25 #se transforman los años a dias (delta time no soporta años)
#leftime = 1.1
system('clear')
nombre = input("Hola, dime tu nombre: ") #Se pide y guarda el nombre del jugador
fnacimiento = input("Genial " + nombre + ", ahora dime tu fecha de nacimiento (DD/MM/YYYY): ") #Se pide y guarda fecha de nacimiento
fnacimiento = datetime.datetime.strptime(fnacimiento, "%d/%m/%Y") #Se transforma el string a un datetimeclass
fdead = fnacimiento + datetime.timedelta(days=leftdays) #Se calcula la fecha de muerte sumandole 80 años al dia de fnacimiento
fhoy = datetime.datetime.now() #Se obtiene la fecha actual
edad = fhoy - fnacimiento #Se obtiene la difencia entre hoy y el dia de nacimiento
edadyear = str(round((edad.days/365.25), 2)) #Se transforma la diferencia a años
print("Listo " + nombre + " tu edad es de: " + edadyear + " años.") #Se imprime la edad en años
print("Suponiendo que fueras a vivir 80 esto es lo que te queda de vida: ")
class Digital_clock():
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.geometry("525x300")
        self.mywindow.resizable(0,0)
        self.mywindow.title("Suponiendo que vivieras 80 años, esto es lo que te resta de vida:")
        self.mywindow.config(background='#1f2f3f')
        self.current_time_label = tk.Label(text="", font=('Tahoma', 25), fg='#ffffff', bg='#72a922', pady=10, padx=10)
        self.created_by_label = tk.Label(text="By: LORD PETYR", font=('Tahoma', 9), fg='#ffffff', bg='#ff3333', pady=3, padx=3)
        self.current_time_label.place(x=75, y=75)
        self.created_by_label.place(x=75, y=200)
        self.update_clock()
        self.mywindow.mainloop()
    def update_clock(self):
        fhoy = datetime.datetime.now() #Se obtiene la fecha actual
        lefttime = fdead - fhoy #Se obtiene la difencia entre hoy y el dia de muerte
        plaintext = str(lefttime)
        plaintext = plaintext[:-21] + " días, " + fixplain(plaintext[-15:-14]) + plaintext[-14:-7]
        self.current_time_label.configure(text=plaintext)
        self.mywindow.after(1000, self.update_clock)
def fixplain(text):
    if text==" ":
        return "0"
    else:
        return text
main=Digital_clock()
