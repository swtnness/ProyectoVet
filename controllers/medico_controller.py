import tkinter as tk
from tkinter import messagebox
from models.medico_model import MedicoModel
from views.medico_view import MedicoView


class MedicoController:
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)  # Abre una ventana dentro de la misma aplicación.
        self.root.transient(parent)
        self.model = MedicoModel()
        self.view = MedicoView(self.root, self)
        self.root.grab_set()  # Evita cambiar de módulo mientras se usa esta ventana.

    # Revisa los datos antes de enviarlos a MySQL.
    def _validar(self, datos):
        nombre, especialidad, telefono, correo = (dato.strip() for dato in datos)
        if not nombre or not especialidad:
            raise ValueError("Complete el nombre y la especialidad")
        if len(nombre) > 100 or len(especialidad) > 100 or len(correo) > 100:
            raise ValueError("Nombre, especialidad y correo permiten hasta 100 caracteres")
        if len(telefono) > 20:
            raise ValueError("El teléfono permite hasta 20 caracteres")
        return nombre, especialidad, telefono, correo

    # Carga la lista y avisa si la consulta falla.
    def cargar(self):
        try:
            return self.model.listar()
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=self.root)
            return None  # La vista conserva los datos anteriores si falla la consulta.

    def _refrescar(self):
        self.view.limpiar()
        self.view.mostrar_registros()

    # Guarda solamente después de validar los campos.
    def guardar(self, datos):
        try:
            datos = self._validar(datos)
        except ValueError as error:
            messagebox.showwarning("Aviso", str(error), parent=self.root)
            return
        try:
            self.model.insertar(*datos)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=self.root)
            return
        messagebox.showinfo("Correcto", "Registro guardado", parent=self.root)
        self._refrescar()

    # Actualiza el registro que se eligió en la tabla.
    def actualizar(self, identificador, datos):
        if not identificador:
            messagebox.showwarning("Aviso", "Seleccione un registro", parent=self.root)
            return
        try:
            datos = self._validar(datos)
        except ValueError as error:
            messagebox.showwarning("Aviso", str(error), parent=self.root)
            return
        try:
            self.model.actualizar(identificador, *datos)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=self.root)
            return
        messagebox.showinfo("Correcto", "Registro actualizado", parent=self.root)
        self._refrescar()

    # Pide confirmación antes de eliminar.
    def eliminar(self, identificador):
        if not identificador:
            messagebox.showwarning("Aviso", "Seleccione un registro", parent=self.root)
            return
        if not messagebox.askyesno("Confirmar", "Desea eliminar el registro seleccionado?", parent=self.root):
            return
        try:
            self.model.eliminar(identificador)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=self.root)
            return
        messagebox.showinfo("Correcto", "Registro eliminado", parent=self.root)
        self._refrescar()
