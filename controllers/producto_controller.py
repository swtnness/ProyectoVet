import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation
from models.producto_model import ProductoModel
from views.producto_view import ProductoView


class ProductoController:
    def __init__(self, parent):
        self.root = tk.Toplevel(parent)  # Abre una ventana dentro de la misma aplicación.
        self.root.transient(parent)
        self.model = ProductoModel()
        self.view = ProductoView(self.root, self)
        self.root.grab_set()  # Evita cambiar de módulo mientras se usa esta ventana.

    # Revisa los datos antes de enviarlos a MySQL.
    def _validar(self, datos):
        nombre, descripcion, precio, stock = (dato.strip() for dato in datos)
        if not nombre or not precio or not stock:
            raise ValueError("Complete el nombre, precio y stock")
        if len(nombre) > 100:
            raise ValueError("El nombre permite hasta 100 caracteres")
        if len(descripcion.encode("utf-8")) > 65535:
            raise ValueError("La descripción es demasiado larga")
        try:
            precio = Decimal(precio.replace(",", "."))  # Acepta 12.50 o 12,50.
        except InvalidOperation:
            raise ValueError("Escriba un precio válido, por ejemplo 12500.50")
        if not precio.is_finite() or precio < 0 or precio > Decimal("99999999.99"):
            raise ValueError("El precio debe estar entre 0 y 99999999.99")
        if precio != precio.quantize(Decimal("0.01")):
            raise ValueError("El precio puede tener máximo dos decimales")
        if not stock.isascii() or not stock.isdigit():
            raise ValueError("El stock debe ser un número entero sin negativos")
        stock = int(stock)
        if stock > 2147483647:
            raise ValueError("El stock es demasiado grande")
        return nombre, descripcion, precio.quantize(Decimal("0.01")), stock

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
        if not messagebox.askyesno("Confirmar", "¿Desea eliminar el registro seleccionado?", parent=self.root):
            return
        try:
            self.model.eliminar(identificador)
        except Exception as error:
            messagebox.showerror("Error", str(error), parent=self.root)
            return
        messagebox.showinfo("Correcto", "Registro eliminado", parent=self.root)
        self._refrescar()
