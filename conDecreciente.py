import tkinter as tk

class ContDecrecienteApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("ContDecreciente")
        
        self.contador = 88
        
        self.etiqueta = tk.Label(ventana, text="Contador", font=("Helvetica", 12))
        self.etiqueta.grid(row=0, column=0, padx=10)
        
        self.valorContador = tk.StringVar()
        self.valorContador.set(str(self.contador))
        
        self.lineEdit = tk.Entry(ventana, textvariable=self.valorContador, font=("Helvetica", 12), state="readonly", width=5)
        self.lineEdit.grid(row=0, column=1, padx=5)
        
        self.botonMenos = tk.Button(ventana, text="-", font=("Helvetica", 12), command=self.DecrecerContador, width=3)
        self.botonMenos.grid(row=0, column=2, padx=10)

    def DecrecerContador(self):
        self.contador -= 1
        self.valorContador.set(str(self.contador))

ventanaPrincipal = tk.Tk()
app = ContDecrecienteApp(ventanaPrincipal)
ventanaPrincipal.mainloop()
