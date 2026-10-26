
from tkinter import ttk

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Login Veterinaria")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#FCE4EC")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame",
                        background="#FCE4EC")

        style.configure("TLabel",
                        background="#FCE4EC",
                        foreground="#8E6280")

        style.configure("TEntry",
                        fieldbackground="#FFF8E1",
                        foreground="#8E6280",
                        padding=5)

        style.configure("TButton",
                        background="#F8BBD0",
                        foreground="#8E6280",
                        font=("Arial", 11, "bold"),
                        padding=10)

        style.map("TButton",
                  background=[("active", "#EDE7F6")])

        frame = ttk.Frame(root, padding=30)
        frame.pack(expand=True)

        ttk.Label(frame,
                  text="Sistema veterinario",
                  font=("Arial", 18, "bold")).pack(pady=(0,20))
        ttk.Label(frame, text="Usuario").pack(anchor="w")
        self.textUsuario = ttk.Entry(frame, width=35)
        self.textUsuario.pack(pady=(0,10))
        # contraseña
        ttk.Label(frame, text="Contraseña").pack(anchor="w")
        self.textPassword = ttk.Entry(frame, width=35, show="*")
        self.textPassword.pack(pady=(0,20))
        ttk.Button(frame,
                   text="Iniciar Sesion",
                   command=self.iniciar_sesion).pack(fill="x")
        self.textUsuario.focus()
        # PRESIONAR ENTER
        self.textPassword.bind("<Return>", lambda event: self.iniciar_sesion())
    def iniciar_sesion(self):
        self.controller.iniciar_sesion(
            self.textUsuario.get().strip(),
            self.textPassword.get()
        )
