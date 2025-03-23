import tkinter as tk
import cmath
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CalculadoraComplejos(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Calculadora de Números Complejos")
        self.geometry("460x420")

        # Creación de la caja de texto para la entrada y resultado
        self.caja_texto = tk.Entry(self, font=("Calculator", 14), justify="right", width=50)
        self.caja_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

        # Definición de los botones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("j", 5, 0), ("∠", 5, 1)
        ]

        # Creación de botones en una cuadrícula
        for (texto, fila, columna) in botones:
            tk.Button(self, text=texto, font=("Calculator", 14), width=9, height=1, command=lambda t=texto: self.presionar(t)).grid(row=fila, column=columna, ipadx=10, ipady=10)

        # Botones adicionales para borrar
        tk.Button(self, text="C", font=("Calculator", 14), width=9, height=1, command=self.borrar).grid(row=5, column=2, ipadx=10, ipady=10,)
        tk.Button(self, text="CE", font=("Calculator", 14), width=9, height=1, command=self.borrar_todo).grid(row=5, column=3, ipadx=10, ipady=10)

        # Checkbox para seleccionar tipo de número
        self.numero_complejo = tk.BooleanVar()
        tk.Checkbutton(self, text="Complejo", font=("Arial", 12), variable=self.numero_complejo, command=self.cambiar_tipo).grid(row=6, column=0, columnspan=4)

        # Tipo de número actual (real, polar, cartesiano)
        self.tipo_numero = "real"
        
        # Botón para agregar la vista gráfica
        tk.Button(self, text="VG", font=("Calculator", 14),width=9, height=1, command=self.crear_grafico).grid(row=6, column=0, ipadx=10, ipady=10)
        



    def crear_grafico (self):
        self.geometry("460x720")
        # Crear la figura de Matplotlib
        self.figura, self.ejes = plt.subplots()

        # Crear el widget de lienzo para integrar la figura en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=7, column=0, columnspan=4)

        # Llenar la figura con datos iniciales
        self.actualizar_grafico([resultado])
        
    def presionar(self, valor):
        # Función para manejar los eventos de presionar un botón
        if valor == "=":
            self.calcular()
        else:
            self.caja_texto.insert(tk.END, valor)

    def borrar(self):
        # Función para borrar el último carácter en la caja de texto
        self.caja_texto.delete(len(self.caja_texto.get()) - 1)

    def borrar_todo(self):
        # Función para borrar todo el contenido de la caja de texto
        self.caja_texto.delete(0, tk.END)

    def calcular(self):
        global resultado
        # Función para evaluar la expresión y mostrar el resultado
        expresion = self.caja_texto.get()

        if self.numero_complejo.get() == True:
            try:
                if self.tipo_numero == "polar":
                    resultado = cmath.polar(eval(expresion))
                    self.separar(resultado)
                elif self.tipo_numero == "cartesiano":
                    resultado = cmath.rect(*eval(expresion))
                    self.separar(resultado)
                else:
                    resultado = "Error"         
            except Exception as e:
                resultado = "Error"
        else:
            try:
                resultado = eval(expresion)
                self.separar(resultado)
            except Exception as e:
                resultado = "Error"

        self.borrar_todo()
        self.caja_texto.insert(tk.END, resultado)

    def cambiar_tipo(self):
        # Función para cambiar el tipo de número entre real, polar y cartesiano
        if self.numero_complejo.get()== False:
            self.tipo_numero = "real"
        else:
            self.tipo_numero = "polar"

    def actualizar_grafico(self, datos):
        
        # Función para actualizar el gráfico con nuevos datos
        self.ejes.clear()
        self.ejes.scatter(range(1, len(datos) + 1), datos)  # Mostrar puntos en lugar de una línea continua
        self.ejes.set_xlabel('Eje X')
        self.ejes.set_ylabel('Eje Y')
        self.figura.tight_layout()
        self.canvas.draw_idle()
        
    def separar (self,res):
        print(res)


if __name__ == "__main__":
    app = CalculadoraComplejos()
    app.mainloop()
