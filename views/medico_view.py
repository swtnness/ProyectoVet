import tkinter as tk
from tkinter import ttk


class MedicoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.id_seleccionado = None
        self.root.title("Vet Vannecita - Médicos")
        self.root.geometry("900x600")
        self.root.minsize(800, 550)
        self.campos = {}  # Guarda los campos del formulario por su nombre.
        self.crear_formulario()
        self.crear_tabla()
        self.mostrar_registros()

    # Crea los campos y botones del formulario.
    def crear_formulario(self):
        frame = ttk.LabelFrame(self.root, text="Datos de médicos", padding=15)
        frame.pack(fill="x", padx=15, pady=15)
        frame.columnconfigure(1, weight=1)
        etiquetas = [('nombre', 'Nombre'), ('especialidad', 'Especialidad'), ('telefono', 'Teléfono'), ('correo', 'Correo')]
        for fila, (nombre, etiqueta) in enumerate(etiquetas):
            ttk.Label(frame, text=etiqueta).grid(row=fila, column=0, sticky="w")
            campo = ttk.Entry(frame, width=45)
            campo.grid(row=fila, column=1, padx=8, pady=5, sticky="ew")
            self.campos[nombre] = campo

        botones = ttk.Frame(frame)
        botones.grid(row=4, column=0, columnspan=2, pady=12)
        acciones = [("Guardar", self.guardar), ("Actualizar", self.actualizar),
                    ("Eliminar", self.eliminar), ("Limpiar", self.limpiar),
                    ("Volver a mascotas", self.root.destroy)]
        for texto, accion in acciones:
            ttk.Button(botones, text=texto, command=accion).pack(side="left", padx=5)

    # Crea la tabla donde aparecen los registros guardados.
    def crear_tabla(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.columnas = ('id_medico', 'nombre', 'especialidad', 'telefono', 'correo')
        self.tabla = ttk.Treeview(frame, columns=self.columnas, show="headings", selectmode="browse")
        titulos = ('ID', 'Nombre', 'Especialidad', 'Teléfono', 'Correo')
        for columna, titulo in zip(self.columnas, titulos):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=60 if columna == "id_medico" else 155, minwidth=45)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.tabla.pack(side="left", fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

    # Consulta de nuevo para mostrar los cambios de la base de datos.
    def mostrar_registros(self):
        registros = self.controller.cargar()
        if registros is None:
            return
        self.limpiar()
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for registro in registros:
            valores = ["" if registro[columna] is None else registro[columna] for columna in self.columnas]
            self.tabla.insert("", "end", values=valores)

    # Copia los datos de la fila seleccionada al formulario.
    def seleccionar(self, event=None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = valores[0]
        for campo, valor in zip(self.campos.values(), valores[1:]):
            campo.delete(0, tk.END)
            campo.insert(0, valor)

    def datos_formulario(self):
        return tuple(campo.get().strip() for campo in self.campos.values())

    def guardar(self):
        self.controller.guardar(self.datos_formulario())

    def actualizar(self):
        self.controller.actualizar(self.id_seleccionado, self.datos_formulario())

    def eliminar(self):
        self.controller.eliminar(self.id_seleccionado)

    # Limpia los campos y quita la selección de la tabla.
    def limpiar(self):
        self.id_seleccionado = None
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        for fila in self.tabla.selection():
            self.tabla.selection_remove(fila)
        self.campos["nombre"].focus_set()
