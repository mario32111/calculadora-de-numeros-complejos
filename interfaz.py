# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:00:01 2023

@author: mario
"""

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import font
import cmath  # Módulo para manejar números complejos



class Eventos:
    def __init__(self):
        self.ind = 0

    def bot_click(self, event, caja):
        if event.widget.cget("text") == "iz":
            self.ind -= 1
        elif event.widget.cget("text") == "der":
            self.ind += 1
        else:
            self.ind = self.ind + 1
            caja.config(state="normal")

            if event.widget.cget("text") == "CE":
                self.ind = 0
                caja.delete(0, tk.END)
            elif event.widget.cget("text") == "C":
                self.ind -= 1
                cont = caja.get()
                cont = cont[:-1]  # Eliminar el último carácter
                caja.delete(0, tk.END)
                caja.insert(0, cont)
                caja.config(state="readonly")
            elif event.widget.cget("text") == "=":
                self.mostrar_resultado(caja)
            elif event.widget.cget("text") == "NPo":
                caja.insert(self.ind, "NPo(")
                self.ind += 4
                caja.config(state="readonly")
            elif event.widget.cget("text") == "NCa":
                caja.insert(self.ind, "NCa(")
                self.ind += 4
                caja.config(state="readonly")
            elif event.widget.cget("text") != "CE":
                caja.insert(self.ind, event.widget.cget("text"))
                caja.config(state="readonly")

    def bot_m(self, event):
        event.widget.config(background="light blue")

    def bot_m2(self, event):
        event.widget.config(background="light gray")

    def mostrar_resultado(self, caja):
        expresion = caja.get()
        try:
            resultado = self.procesar_expresion(expresion)
            caja.delete(0, tk.END)
            caja.insert(0, str(resultado))
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)

    def procesar_expresion(self, expresion):
        for i in expresion:
            if i == '+' or i == '-' or i == '*' or i == '/':
                partes = expresion.split(i)
                numeros = []
                for parte in partes:
                    parte = parte.strip().replace('NCa(', '').replace(')', '')
                    numeros.append(complex(parte.replace('i', 'j')))
                print(expresion)
                print(numeros)
                if i=='+':
                    resultado = sum(numeros)
                    return resultado

class EventosTk(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x480")
        self.title("Calculadora de Números Complejos")
        self.config(bg="gray")
        self.botones = []
        fuente_externa = font.Font(family="Calculator", size=19)
        f2 = font.Font(family="Calculator", size=35)

        car_botones = [
            "NCa", "NPo", "j", "VG", "1", "2", "3", "*", "4", "5", "6", "+", "7", "8",
            "9", "-", "+/-", "0", ".", "=", "/", "√", "C", "CE", "Shift", "pot", "(", ")",
            "ESTO NO ES UN BOTON", "iz", "der",
        ]

        # Caja de texto
        inM = tk.Entry(self, width=50, font=f2, state="readonly")
        inM.place(x=0, y=0)

        for i, texto in enumerate(car_botones):
            boton = tk.Button(self, text=texto, width=9, height=1, background="light gray", font=fuente_externa)
            boton.bind("<Button-1>", lambda event, boton=boton: eventos.bot_click(event, inM))
            boton.bind("<Enter>", lambda event, boton=boton: eventos.bot_m(event))
            boton.bind("<Leave>", lambda event, boton=boton: eventos.bot_m2(event))
            if i < 27:
                boton.place(x=(i % 4) * 100, y=(i // 4) * 50 + 80)
            elif i == 28:
                pass
            else:
                boton.place(x=(i % 4) * 100, y=(i // 4) * 50 + 80)

            self.botones.append(boton)

eventos = Eventos()
app = EventosTk()
app.mainloop()
"""
        # Cargar una imagen en formato PNG
        imagen_original = Image.open("C:/Users/Mario/Desktop/calculadora de numeros complejos/hola.png")  # Reemplaza "mi_imagen.png" con la ruta de tu imagen PNG

        # Redimensionar la imagen al tamaño deseado
        nuevo_tamano = (50, 50)  # Ancho x Alto en píxeles
        imagen_redimensionada = imagen_original.resize(nuevo_tamano, Image.BOX)

        # Crear una referencia global a la imagen
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        # Crear un botón con la imagen redimensionada
        boton_con_imagen = tk.Button(ventana, image=imagen_tk, borderwidth=0, relief="flat",highlightthickness=0, highlightbackground="white")
        boton_con_imagen.pack()
"""
