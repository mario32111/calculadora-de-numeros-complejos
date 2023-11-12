# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:00:01 2023

@author: mario
"""

import tkinter as tk
from tkinter import font

class Eventos:
    def bot_click(self, event):
        print("Botón pulsado:", event.widget.cget("text"))

    def bot_m(self, event):
        event.widget.config(background="light blue")

    def bot_m2(self, event):
        event.widget.config(background="light gray")

class EventosTk(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x540")
        self.title("Calculadora")
        self.config(bg="gray")
        self.botones=[]
        fuente_externa = font.Font(family="LCDDot TR", size=19)

        botones = [
            "NCart", "NPol", "Vista grafica","i","1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            "x", "-", "+", "=", ".", "+/-", "/", "raiz", "pot", "CE", "C","borrar", "(", ")",
            "ESTO NO ES UN BOTON", "iz", "der", 
        ]

        for i, texto in enumerate(botones):
            boton = tk.Button(self, text=texto, width=10, height=3, background="light gray", font=fuente_externa)
            boton.bind("<Button-1>", lambda event, boton=boton: eventos.bot_click(event))
            boton.bind("<Enter>", lambda event, boton=boton: eventos.bot_m(event))
            boton.bind("<Leave>", lambda event, boton=boton: eventos.bot_m2(event))
            if i < 27:
                boton.place(x=(i % 4) * 100, y=(i // 4) * 55 + 100)
            elif i ==28:
                pass
            else:
                boton.place(x=(i % 4) * 100, y=(i // 4) * 55 + 100)
                

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
