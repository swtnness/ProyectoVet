#importar las librerias y archivos necesarios para el controlador
import tkinter as tk
from tkinter import messagebox
#modelo y vista
from models.citas_model import CitaModel
from views.cita_view import CitaView

#clase u objeto
class CitaController:
    """Controlador que maneja la logica de las citas"""
    #constructor
    def __init__(self, id_mascotas):  # Prepara lo necesario cuando se crea el controlador.
        self.id_mascotas = id_mascotas
        self.root = tk.Tk()  # Crea la ventana principal.
        self.model = CitaModel()  # Crea el modelo para trabajar con los datos.
        self.view = CitaView(self.root, self, self.id_mascotas)  # Crea la vista y le pasa la ventana y el controlador. def iniciar(self):  # Define el método que inicia la ventana.
                
    def iniciar(self):  # Define el método que inicia la ventana.
        self.root.mainloop()  # Mantiene la ventana abierta y espera las acciones del usuario.
        
    def _refrescar(self):  # Actualiza la vista después de un cambio.
        self.view.limpiar()  # Llama al método que limpia los campos.
        self.view.mostrar_citas()  # Vuelve a mostrar las citas con los cambios.
        
    # metodo para show the pets
    def cargar_citas(self):  # Obtiene las citas guardadas.
        try:  # Intenta consultar la lista de citas.
            return self.model.listar_por_mascota(self.id_mascotas)  # Devuelve las mascotas que entrega el modelo.
        except Exception as e:  # Guarda en e el error que haya ocurrido.
            messagebox.showerror("Error", str(e))  # Muestra el error como texto.
            return []  # Devuelve una lista vacía si la consulta falla.
        
    def guardar(self, datos):  # Recibe los datos para guardar una mascota nueva.
        fecha, motivo = datos
        if not fecha or not motivo: # Comprueba si los datos no pasaron la validación.
            messagebox.showwarning("Aviso", "Debe de ingresar una fecha o un motivo")
            return  # Sale del método sin guardar.
        try:  # Intenta guardar la mascota y actualizar la vista.
            self.model.insertar(self.id_mascotas, fecha, motivo)  # Envía los datos al modelo para guardar la mascota.
            messagebox.showinfo("Correcto", "Cita creada")  # Informa que la mascota fue creada.
            self._refrescar()  # Limpia los campos y actualiza la lista.
        except Exception as e:  # Captura un error que ocurra dentro del try.
            messagebox.showwarning("Error", str(e))  # Muestra un aviso con el error.

    # metodo eliminar
    def eliminar(self, id_mascota):
        # Revisa si hay un dato seleccionado.
        if not id_mascota:
            messagebox.showwarning("Aviso", "Seleccione un dato")
            return

        # Pide confirmación antes de eliminar el dato.
        if messagebox.askyesno("Confirmar", "Desea eliminar el dato?"):
            try:
                self.model.eliminar(id_mascota)  # Envía al modelo el identificador del dato que se eliminará.
                messagebox.showinfo("Correcto", "Dato eliminado")  # Informa que el dato fue eliminado.
                self._refrescar()  # Limpia los campos y actualiza la lista de citas.
            except Exception as e:
                messagebox.showerror("Error", str(e))  # Muestra el error si la eliminación falla.
                
    #metodo para volver a la ventana principal
    def volver_a_mascotas(self):
        """cierra la ventana de citas y regresa a la ventana principal"""
        try:
            from controllers.mascota_controller import MascotaController
            self.root.destroy()
            MascotaController().iniciar
        except Exception as e:
            messagebox.showerror("Error", str(e))

