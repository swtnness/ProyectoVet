import tkinter as tk
from tkinter import messagebox

from models.mascota_model import MascotaModel
from views.mascota_view import MascotaView

class MascotaController:
    """Controlador que maneja toda la logica de mascotas"""
    def __init__(self):
        self.root = tk.Tk()
        self.model = MascotaModel()
        self.view = MascotaView(self.root, self)
    def iniciar(self):
        self.root.mainloop()
    def _validar(self, datos):
        """Devuelve (nombre, especie, raza, edad_int, propietario) or none"""
        nombre, especie, raza, edad, propietario = datos
        if not nombre or not especie or not edad or not propietario:
            messagebox.showwarning("Aviso", "Complete los datos")
            return None
        try:
            edad = int(edad)
            if edad < 0:
                messagebox.showwarning("Aviso", "Escriba una edad valida")
                return None
        except ValueError:
            messagebox.showwarning("Aviso", "Escriba una edad valida")
            return None
        return nombre, especie, raza, edad, propietario
    
    def _refrescar(self):
        self.view.limpiar()
        self.view.mostrar_mascotas()
    #metodo para show the pets
    def cargar_mascotas(self):
        try:
            return self.model.listar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return [] 
    def guardar(self, datos):
        datos = self._validar(datos)
        if not datos:
            return
        try:
            self.model.insertar(datos)
            messagebox.showinfo("Correcto", "Mascota creada")
            self._refrescar()
        except Exception as e:
            messagebox.showwarning("Error", str(e)) 
    
