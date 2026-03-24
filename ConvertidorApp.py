import customtkinter
from tkinter import messagebox, ttk

class ConvertidorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400+450+250")
        self.root.resizable(False, False)
        self.root.title("Convertidor de temperatura")
        self.conversiones = ["Celcius (°C) - Kelvin(K)",
                              "Celcius(°C) - Fahrenheit (°F)",
                                "Kelvin(K) - Celcius(°C)",
                                  "Kelvin(K) - Fahrenheit (°F)",
                                    "Fahrenheit (°F) - Celcius(°C)",
                                      "Fahrenheit (°F) - Kelvin(K)"]


        self.titulo = customtkinter.CTkLabel(root, text="Convertidor", font=("Arial", 24, "italic"))
        self.titulo.pack(side = "top")

        self.label_1 = customtkinter.CTkLabel(root, text="Ingrese los grados que desee convertir", font=("Arial", 18, "italic"))
        self.label_1.pack(pady=20)

        self.grados_entry = customtkinter.CTkEntry(root, width=100)
        self.grados_entry.pack(pady=20)

        self.label_2 = customtkinter.CTkLabel(root , text="Seleccione una opción", font = ("Arial", 18, "italic"))
        self.label_2.pack(pady=20)

        self.combobox = ttk.Combobox(root, values=(self.conversiones))
        self.combobox.pack(pady=5)

        self.label_3 = customtkinter.CTkLabel(root, text="Resultado:", font=("Arial", 18, "italic"))
        self.label_3.pack(pady=5)

        self.salida_entry = customtkinter.CTkEntry(root, width=100)
        self.salida_entry.pack(pady=20)

        self.grados_entry.bind("<Return>", self.ingresar_grados)
        self.combobox.bind("<<ComboboxSelected>>", self.calcular_conversion)

    def ingresar_grados(self, event):
        global grados
        grados = self.grados_entry.get().strip()

        if not grados:
            messagebox.showerror("Error", "Ingrese los grados!!")
            return
        
        try:
            grados = float(grados)
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida.")
            return
        
    def calcular_conversion(self, event):
        global grados
        seleccion = self.combobox.get()
        if not grados:
            messagebox.showerror("Error", "Ingrese los grados!!")
            return
        
        else:
            if seleccion == self.conversiones[0]:
                print(f'Se ha seleccionado: {seleccion}')
                celcius = float(self.grados_entry.get())
                kelvin = celcius + 273.5
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{kelvin:.2f}')
                messagebox.showinfo("Info", f'Kelvin: {kelvin:.2f} K')
            
            elif seleccion == self.conversiones[1]:
                print(f'Se ha seleccionado: {seleccion}')
                celcius = float(self.grados_entry.get())
                fahrenheit = (1.8 * celcius) + 32
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{fahrenheit:.2f}')
                messagebox.showinfo("Info", f'Fahrenheit: {fahrenheit:.2f} °F')
            
            elif seleccion == self.conversiones[2]:
                print(f'Se ha seleccionado: {seleccion}')
                kelvin = float(self.grados_entry.get())
                celcius = kelvin - 273.5
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{celcius:.2f}')
                messagebox.showinfo("Info", f'Celcius: {celcius:.2f}')
            
            elif seleccion == self.conversiones[3]:
                print(f'Se ha seleccionado: {seleccion}')
                kelvin = float(self.grados_entry.get())
                fahrenheit = (kelvin - 273.5) * 1.8 + 32
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{fahrenheit:.2f}')
                messagebox.showinfo("Info", f'Fahrenheit: {fahrenheit:.2f} °F')

            elif seleccion == self.conversiones[4]:
                print(f'Se ha seleccionado: {seleccion}')
                fahrenheit = float(self.grados_entry.get())
                celcius = (fahrenheit - 32) / 1.8
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{celcius:.2f}')
                messagebox.showinfo("Info", f'Celcius: {celcius:.2f}')

            elif seleccion == self.conversiones[5]:
                print(f'Se ha seleccionado: {seleccion}')
                fahrenheit = float(self.grados_entry.get())
                kelvin = ((fahrenheit - 32) / 1.8) + 273.5
                self.salida_entry.delete(0, "end")
                self.salida_entry.insert(0, f'{kelvin:.2f}')
                messagebox.showinfo("Info", f'Kelvin: {kelvin:.2f} K')

        
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = ConvertidorApp(root)
    root.mainloop()