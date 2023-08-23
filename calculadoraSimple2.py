import tkinter as tk
from tkinter import ttk

class Calculadora2App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora 2")
        
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.resultado = tk.StringVar()
        self.operacion = tk.StringVar(value="Sumar")
        
        self.etiquetaValor1 = tk.Label(ventana, text="Valor 1:", font=("Helvetica", 12))
        self.etiquetaValor1.grid(row=0, column=0, padx=10, pady=5)
        
        self.etiquetaValor2 = tk.Label(ventana, text="Valor 2:", font=("Helvetica", 12))
        self.etiquetaValor2.grid(row=1, column=0, padx=10, pady=5)
        
        self.etiquetaResultado = tk.Label(ventana, text="Resultado:", font=("Helvetica", 12))
        self.etiquetaResultado.grid(row=2, column=0, padx=10, pady=5)
        
        self.etiquetaOperaciones = tk.Label(ventana, text="Operaciones:", font=("Helvetica", 12))
        self.etiquetaOperaciones.grid(row=0, column=2, padx=10, pady=5)
        
        self.lineEditValor1 = tk.Entry(ventana, textvariable=self.valor1, font=("Helvetica", 12), width=15)
        self.lineEditValor1.grid(row=0, column=1, padx=5)
        
        self.lineEditValor2 = tk.Entry(ventana, textvariable=self.valor2, font=("Helvetica", 12), width=15)
        self.lineEditValor2.grid(row=1, column=1, padx=5)
        
        self.lineEditResultado = tk.Entry(ventana, textvariable=self.resultado, font=("Helvetica", 12), state="readonly", width=15)
        self.lineEditResultado.grid(row=2, column=1, padx=5)
        
        self.radioButtonSumar = tk.Radiobutton(ventana, text="Sumar", variable=self.operacion, value="Sumar")
        self.radioButtonSumar.grid(row=1, column=2, padx=5)
        
        self.radioButtonRestar = tk.Radiobutton(ventana, text="Restar", variable=self.operacion, value="Restar")
        self.radioButtonRestar.grid(row=2, column=2, padx=5)
        
        self.radioButtonMultiplicar = tk.Radiobutton(ventana, text="Multiplicar", variable=self.operacion, value="Multiplicar")
        self.radioButtonMultiplicar.grid(row=3, column=2, padx=20)
        
        self.radioButtonDividir = tk.Radiobutton(ventana, text="Dividir", variable=self.operacion, value="Dividir")
        self.radioButtonDividir.grid(row=4, column=2, padx=5)
        
        self.botonCalcular = tk.Button(ventana, text="Calcular", font=("Helvetica", 12), command=self.calcular)
        self.botonCalcular.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def calcular(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get())
            operacion = self.operacion.get()
            
            if operacion == "Sumar":
                resultado = num1 + num2
            elif operacion == "Restar":
                resultado = num1 - num2
            elif operacion == "Multiplicar":
                resultado = num1 * num2
            elif operacion == "Dividir":
                resultado = num1 / num2
            
            self.resultado.set(str(resultado))
        except:
            self.resultado.set("Error")

# Crear la ventana principal
ventanaPrincipal = tk.Tk()

# Crear una instancia de la clase Calculadora2App
app = Calculadora2App(ventanaPrincipal)

# Iniciar el bucle principal
ventanaPrincipal.mainloop()
