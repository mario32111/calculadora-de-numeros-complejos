# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:42:54 2023

@author: mario
"""

import tkinter as tk
from tkinter import font

class Eventos:
    def bot_click(self,boton):
        boton.config(background="black")

    def bot_m(self, boton):
        boton.config(background="light blue")

    def bot_m2(self,boton):
        boton.config(background="light gray")

class EventosTk(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("325x530")
        self.title("Calculadora")
        self.config(bg="gray")
        fuente_externa = font.Font(family="LCDDot TR", size=19)

        b1 = tk.Button(self, text="1", width=10, height=3, background="light gray", font=fuente_externa)
        b1.bind("<Button-1>", lambda event: eventos.bot_click(b1))
        b1.bind("<Enter>", lambda event: eventos.bot_m(b1))
        b1.bind("<Leave>", lambda event: eventos.bot_m2(b1))
        b1.place(x=0,y=250)
        b2= tk.Button(self, text="2", width=10, height=3, background="light gray", font=fuente_externa)
        b2.place(x=80,y=250)
        b3= tk.Button(self, text="3", width=10, height=3, background="light gray", font=fuente_externa)
        b3.place(x=160,y=250)
        b4= tk.Button(self, text="4", width=10, height=3, background="light gray", font=fuente_externa)
        b4.place(x=0,y=305)
        b5= tk.Button(self, text="5", width=10, height=3, background="light gray", font=fuente_externa)
        b5.place(x=80,y=305)
        b6= tk.Button(self, text="6", width=10, height=3, background="light gray", font=fuente_externa)
        b6.place(x=160,y=305)
        b7= tk.Button(self, text="7", width=10, height=3, background="light gray", font=fuente_externa)
        b7.place(x=0,y=360)
        b8= tk.Button(self, text="8", width=10, height=3, background="light gray", font=fuente_externa)
        b8.place(x=80,y=360)
        b9= tk.Button(self, text="9", width=10, height=3, background="light gray", font=fuente_externa)
        b9.place(x=160,y=360)
        b0= tk.Button(self, text="0", width=10, height=3, background="light gray", font=fuente_externa)
        b0.place(x=80,y=415)
        #Botones operciones
        bpor= tk.Button(self, text="x", width=10, height=3, background="light gray", font=fuente_externa)
        bpor.place(x=240,y=250)
        bmenos= tk.Button(self, text="-", width=10, height=3, background="light gray", font=fuente_externa)
        bmenos.place(x=240,y=305)
        bmas= tk.Button(self, text="+", width=10, height=3, background="light gray", font=fuente_externa)
        bmas.place(x=240,y=360)
        bigual= tk.Button(self, text="=", width=10, height=3, background="light gray", font=fuente_externa)
        bigual.place(x=240,y=415)
        #otros botones
        bigual= tk.Button(self, text=".", width=10, height=3, background="light gray", font=fuente_externa)
        bigual.place(x=160,y=415)
        bmas_menos= tk.Button(self, text="+/-", width=10, height=3, background="light gray", font=fuente_externa)
        bmas_menos.place(x=0,y=415)
        bdiv= tk.Button(self, text="/", width=10, height=3, background="light gray", font=fuente_externa)
        bdiv.place(x=80,y=195)
        braiz= tk.Button(self, text="raiz", width=10, height=3, background="light gray", font=fuente_externa)
        braiz.place(x=160,y=195)
        bpot= tk.Button(self, text="pot", width=10, height=3, background="light gray", font=fuente_externa)
        bpot.place(x=240,y=195)
        bce= tk.Button(self, text="CE", width=10, height=3, background="light gray", font=fuente_externa)
        bce.place(x=80,y=145)
        bc= tk.Button(self, text="C", width=10, height=3, background="light gray", font=fuente_externa)
        bc.place(x=160,y=145)
        bi= tk.Button(self, text="i", width=10, height=3, background="light gray", font=fuente_externa)
        bi.place(x=0,y=150)
        bborrar= tk.Button(self, text="borrar", width=10, height=3, background="light gray", font=fuente_externa)
        bborrar.place(x=240,y=145)
        bpar1= tk.Button(self, text="(", width=10, height=3, background="light gray", font=fuente_externa)
        bpar1.place(x=160,y=95)
        bpar2= tk.Button(self, text=")", width=10, height=3, background="light gray", font=fuente_externa)
        bpar2.place(x=240,y=95)
        biz= tk.Button(self, text="iz", width=10, height=3, background="light gray", font=fuente_externa)
        biz.place(x=0,y=95)
        bder= tk.Button(self, text="der", width=10, height=3, background="light gray", font=fuente_externa)
        bder.place(x=80,y=95)
        bCart= tk.Button(self, text="NCart", width=10, height=3, background="light gray", font=fuente_externa)
        bCart.place(x=160,y=37)
        bPol= tk.Button(self, text="NPol", width=10, height=3, background="light gray", font=fuente_externa)
        bPol.place(x=0,y=37)
        bVG= tk.Button(self, text="Vista gr[afica", width=10, height=3, background="light gray", font=fuente_externa)
        bVG.place(x=80,y=470)
        #Caja de texto
        inM=tk.Text(self,width=40, height=2)
        inM.place(x=0,y=0)




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
eventos = Eventos()
app = EventosTk()
app.mainloop()