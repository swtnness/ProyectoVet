from tkinter import ttk 

class MedicoView:
    def __init__(self, root):
        self.root = root  # Guarda la ventana.
        self.root.title("Vet Vannecita - Médicos")
        self.root.geometry("600x350")
        self.root.minsize(550, 350)

        self.crear_formulario()

    def crear_formulario(self):
        frame = ttk.LabelFrame(self.root, text="Datos del médico", padding=15)
        frame.pack(fill="x", padx=15, pady=15)
        frame.columnconfigure(1, weight=1)  # Permite ampliar los campos.

        # Nombre del médico.
        ttk.Label(frame, text="Nombre").grid(row=0, column=0, sticky="w")
        self.txt_nombre = ttk.Entry(frame, width=40)
        self.txt_nombre.grid(row=0, column=1, padx=8, pady=5, sticky="ew")

        ttk.Label(frame, text="Especialidad").grid(row=1, column=0, sticky="w")
        self.txt_especialidad = ttk.Entry(frame, width=40)
        self.txt_especialidad.grid(row=1, column=1, padx=8, pady=5, sticky="ew")

        ttk.Label(frame, text="Teléfono").grid(row=2, column=0, sticky="w")
        self.txt_telefono = ttk.Entry(frame, width=40)
        self.txt_telefono.grid(row=2, column=1, padx=8, pady=5, sticky="ew")

        ttk.Label(frame, text="Correo").grid(row=3, column=0, sticky="w")
        self.txt_correo = ttk.Entry(frame, width=40)
        self.txt_correo.grid(row=3, column=1, padx=8, pady=5, sticky="ew")

        #regresar a mascotas.
        ttk.Button(frame, text="Volver a mascotas", command=self.root.destroy).grid(row=4, column=0, columnspan=2, pady=12)