import tkinter as tk
from tkinter import messagebox
# Comunicar el controlador con el modelo propio
from models.usuario_model import UsuarioModel
# Comunicar con la vista
from views.login_view import LoginView
# Despues de loguear ira a la vista principal
from controllers.mascota_controller import MascotaController

# Crear el objeto de carga de todo
class LoginController:
    """Controlador que gestiona la logica de flujo de sesion"""
    # Constructor
    def __init__(self):
        # Crea la ventana
        self.root = tk.Tk()
        # Instancia o llama el modelo
        self.model = UsuarioModel()
        # Llamar la vista
        self.view = LoginView(self.root, self)
    # Metodo para iniciar la ventana
    def iniciar(self):
        self.root.mainloop()
    # Metodo de iniciar sesion
    def iniciar_sesion(self, usuario, password):
        # Validamos si los campos estan vacios
        if not usuario or not password:
            messagebox.showwarning("¡Aviso!", "Escriba su usuario y clave:")
            return
        try:
            # Llamar el metodo de validacion del modelo
            resultado = self.model.validar_usuario(usuario, password)
            # Validar si es exitoso todo
            if resultado:
                messagebox.showinfo("Bienvenido", "Inicio de sesion exitoso")
                # Cuando se cree el controlador de mascotas
                # self.root.destroy()
                # MascotaController().iniciar()
            else:
                messagebox.showerror("Error", "Usuario o Clave incorrecta")
        except Exception as e:
            messagebox.showerror("Error de conexion", str(e))
