import tkinter as tk  # Importa tkinter como tk para crear la ventana.
from tkinter import messagebox  # Permite mostrar mensajes en pantalla.

from models.mascota_model import MascotaModel  # Importa el modelo que maneja los datos de las mascotas.
from views.mascota_view import MascotaView  # Importa la vista que muestra la interfaz del programa.


class MascotaController:  # Conecta la vista del programa con el modelo.
    """Controlador que maneja toda la logica de mascotas"""

    def __init__(self):  # Prepara lo necesario cuando se crea el controlador.
        self.root = tk.Tk()  # Crea la ventana principal.
        self.model = MascotaModel()  # Crea el modelo para trabajar con los datos.
        self.view = MascotaView(self.root, self)  # Crea la vista y le pasa la ventana y el controlador.

    def iniciar(self):  # Define el método que inicia la ventana.
        self.root.mainloop()  # Mantiene la ventana abierta y espera las acciones del usuario.

    def _validar(self, datos):  # Revisa los datos ingresados.
        """Devuelve (nombre, especie, raza, edad_int, propietario) or none"""
        nombre, especie, raza, edad, propietario = datos  # Separa los datos en sus respectivas variables.
        if not nombre or not especie or not edad or not propietario:  # Revisa si falta algún dato obligatorio.
            messagebox.showwarning("Aviso", "Complete los datos")  # Avisa que hay datos por completar.
            return None  # Sale de la validación porque faltan datos.
        try:  # Intenta convertir la edad a un número entero.
            edad = int(edad)  # Convierte la edad a un número sin decimales.
            if edad < 0:  # Revisa si la edad es negativa.
                messagebox.showwarning("Aviso", "Escriba una edad valida")  # Avisa que debe escribir una edad válida.
                return None  # Sale de la validación porque la edad es negativa.
        except ValueError:  # Se ejecuta si la edad no se puede convertir a un número entero.
            messagebox.showwarning("Aviso", "Escriba una edad valida")  # Avisa que la edad ingresada no es válida.
            return None  # Sale de la validación porque la conversión falló.
        return nombre, especie, raza, edad, propietario  # Devuelve los datos revisados y la edad como número entero.

    def _refrescar(self):  # Actualiza la vista después de un cambio.
        self.view.limpiar()  # Llama al método que limpia los campos.
        self.view.mostrar_mascotas()  # Vuelve a mostrar las mascotas con los cambios.

    # metodo para show the pets
    def cargar_mascotas(self):  # Obtiene las mascotas guardadas.
        try:  # Intenta consultar la lista de mascotas.
            return self.model.listar()  # Devuelve las mascotas que entrega el modelo.
        except Exception as e:  # Guarda en e el error que haya ocurrido.
            messagebox.showerror("Error", str(e))  # Muestra el error como texto.
            return []  # Devuelve una lista vacía si la consulta falla.

    def guardar(self, datos):  # Recibe los datos para guardar una mascota nueva.
        datos = self._validar(datos)  # Revisa los datos antes de guardarlos.
        if not datos:  # Comprueba si los datos no pasaron la validación.
            return  # Sale del método sin guardar.
        try:  # Intenta guardar la mascota y actualizar la vista.
            self.model.insertar(*datos)  # Envía los cinco datos por separado al modelo.
            messagebox.showinfo("Correcto", "Mascota creada")  # Informa que la mascota fue creada.
            self._refrescar()  # Limpia los campos y actualiza la lista.
        except Exception as e:  # Captura un error que ocurra dentro del try.
            messagebox.showwarning("Error", str(e))  # Muestra un aviso con el error.

    # metodo para actualizar
    def actualizar(self, id_mascotas, datos):  # Recibe el identificador y los datos para modificar una mascota.
        # validar que se seleccione una mascota
        if not id_mascotas:  # Revisa si falta el identificador de la mascota seleccionada.
            messagebox.showwarning("Aviso", "Seleccione una mascota")  # Avisa que primero debe seleccionar una mascota.
            return  # Sale del método porque no hay una mascota seleccionada.
        # capturamos los datos
        datos = self._validar(datos)  # Revisa los datos antes de actualizar.
        # si no hay datos
        if not datos:  # Comprueba si los datos no pasaron la validación.
            return  # Sale del método sin actualizar.
        try:  # Intenta actualizar la mascota y mostrar los cambios.
            self.model.actualizar(id_mascotas, *datos)  # Envía el identificador y cada dato por separado al modelo.
            messagebox.showinfo("Correcto", "Mascota actualizada")  # Informa que la mascota fue actualizada.
            self._refrescar()  # Limpia los campos y muestra la lista actualizada.
        except Exception as e:  # Captura un error que ocurra dentro del try.
            messagebox.showerror("Error", str(e))  # Muestra el detalle del error.
    # metodo eliminar
    def eliminar(self, id_mascotas):  # Recibe el identificador de la mascota que se eliminará.
        # Revisa si hay una mascota seleccionada.
        if not id_mascotas:
            messagebox.showwarning("Aviso", "Seleccione un dato")
            return  # Sale del método si no hay una mascota seleccionada.

        # Pide confirmación antes de eliminar.
        if messagebox.askyesno("Confirmar", "Desea eliminar el dato?"):
            try:
                self.model.eliminar(id_mascotas)  # Envía al modelo el identificador de la mascota.
                messagebox.showinfo("Correcto", "Dato eliminado")  # Confirma la eliminación.
                self._refrescar()  # Limpia los campos y actualiza la lista.
            except Exception as e:
                messagebox.showerror("Error", str(e))  # Muestra el error si algo falla.
    
    #metodo para abrir la ventana modal para citas
    def abrir_citas(self, id_mascotas):
        """Cierra la ventana de mascotas y abre el modulo de citas pensando el ID seleccionado"""
        try:
            #importacion local para evitar dependencias circulares
            from controllers.cita_controller import CitaController
            #cerrar la ventana principal
            self.root.destroy()
            #instanciamos o llamar la nueva ventana desde el controlador
            CitaController(id_mascotas).iniciar()
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible abrir la ventana: {str(e)}")