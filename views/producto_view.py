from tkinter import ttk

class ProductoView:
    def __init__(self, root):
        self.root = root  # Guarda la ventana.
        self.root.title("Vet Vannecita - Productos")
        self.root.geometry("600x350")
        self.root.minsize(550, 350)
        self.crear_formulario()  # Muestra los campos del producto.

    # Crea el formulario.
    def crear_formulario(self):
        frame = ttk.LabelFrame(self.root, text="Datos del producto", padding=15)
        frame.pack(fill="x", padx=15, pady=15)
        frame.columnconfigure(1, weight=1)  # Permite ampliar los campos.

        # Nombre del producto.
        ttk.Label(frame, text="Nombre").grid(row=0, column=0, sticky="w")
        self.txt_nombre = ttk.Entry(frame, width=40)
        self.txt_nombre.grid(row=0, column=1, padx=8, pady=5, sticky="ew")

        # Descripción del producto.
        ttk.Label(frame, text="Descripción").grid(row=1, column=0, sticky="w")
        self.txt_descripcion = ttk.Entry(frame, width=40)
        self.txt_descripcion.grid(row=1, column=1, padx=8, pady=5, sticky="ew")

        # Precio del producto.
        ttk.Label(frame, text="Precio").grid(row=2, column=0, sticky="w")
        self.txt_precio = ttk.Entry(frame, width=40)
        self.txt_precio.grid(row=2, column=1, padx=8, pady=5, sticky="ew")

        # Cantidad de unidades disponibles.
        ttk.Label(frame, text="Stock").grid(row=3, column=0, sticky="w")
        self.txt_stock = ttk.Entry(frame, width=40)
        self.txt_stock.grid(row=3, column=1, padx=8, pady=5, sticky="ew")

        #regresar a mascotas.
        ttk.Button(frame, text="Volver a mascotas", command=self.root.destroy).grid(row=4, column=0, columnspan=2, pady=12)