import tkinter as tk  # Permite crear la ventana.
from tkinter import ttk  # Permite crear los campos, botones y tabla.
from tkinter import messagebox  # Permite mostrar avisos.


class CitaView:
    # Constructor de la vista de citas.
    def __init__(self, root, controller, id_mascotas):
        self.root = root  # Guarda la ventana principal.
        self.controller = controller  # Guarda el controlador.
        self.id_mascotas = id_mascotas  # Guarda el identificador de la mascota.
        self.id_seleccionado = None  # Al inicio no hay una cita seleccionada.

        # Diseño de la ventana.
        self.root.title("Vet Vannecita - Citas de las mascotas")
        self.root.geometry("800x500")
        self.root.minsize(700, 400)

        # Crea el formulario, la tabla y carga las citas.
        self.crear_formulario()
        self.crear_tabla()
        self.mostrar_citas()

    # Método para crear el formulario.
    def crear_formulario(self):
        frame = ttk.LabelFrame(
            self.root,
            text=f"Datos de la cita (Mascota ID: {self.id_mascotas})",
            padding=15
        )  # La f permite mostrar el identificador dentro del texto.
        frame.pack(fill="x", padx=15, pady=15)
        frame.columnconfigure(1, weight=1)  # Permite ampliar la columna de los campos.

        # Etiqueta y campo para la fecha.
        ttk.Label(frame, text="Fecha (AAAA-MM-DD)").grid(
            row=0, column=0, sticky="w"
        )
        self.txt_fecha = ttk.Entry(frame, width=30)
        self.txt_fecha.grid(
            row=0, column=1, padx=8, pady=5, sticky="w"
        )

        # Etiqueta y campo para el motivo.
        ttk.Label(frame, text="Motivo").grid(
            row=1, column=0, sticky="w"
        )
        self.txt_motivo = ttk.Entry(frame, width=50)
        self.txt_motivo.grid(
            row=1, column=1, padx=8, pady=5, sticky="ew"
        )

        # Coloca los botones debajo del motivo.
        botones = ttk.Frame(frame)
        botones.grid(row=2, column=0, columnspan=2, pady=12)

        # Botón para guardar la cita.
        ttk.Button(
            botones, text="Guardar Cita", command=self.guardar
        ).pack(side="left", padx=5)

        # Botón para eliminar la cita seleccionada.
        ttk.Button(
            botones, text="Eliminar", command=self.eliminar
        ).pack(side="left", padx=5)

        # Botón para limpiar los campos.
        ttk.Button(
            botones, text="Limpiar", command=self.limpiar
        ).pack(side="left", padx=5)
        
        # Botón para regresar a la ventana de mascotas.
        ttk.Button(
            botones, text="Volver a mascotas", command=self.volver_mascotas
        ).pack(side="left", padx=5)

    # Método para crear la tabla.
    def crear_tabla(self):
        frame = ttk.Frame(self.root)  # Crea el contenedor de la tabla.
        frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Nombres internos de las columnas de citas.
        columnas = ("id_cita", "fecha", "motivo")

        # Crea la tabla y permite seleccionar una sola fila.
        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            selectmode="browse"
        )

        # Los nombres deben coincidir con los de columnas.
        titulos = {
            "id_cita": "ID",
            "fecha": "Fecha",
            "motivo": "Motivo"
        }

        # Ancho de cada columna.
        anchos = {
            "id_cita": 50,
            "fecha": 120,
            "motivo": 400
        }

        # Coloca los títulos y ajusta las columnas.
        for columna in columnas:
            self.tabla.heading(columna, text=titulos[columna])
            self.tabla.column(
                columna, width=anchos[columna], anchor="center"
            )

        # Crea la barra de desplazamiento.
        scroll = ttk.Scrollbar(
            frame, orient="vertical", command=self.tabla.yview
        )

        # Conecta la tabla con la barra.
        self.tabla.configure(yscrollcommand=scroll.set)

        # Ubica la tabla y la barra.
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Llama al método seleccionar cuando se marca una fila.
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)
        
    #metodo para mostrar los datos
    def mostrar_citas(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        self.id_seleccionado = None  # Quita el identificador de la selección anterior.
        citas = self.controller.cargar_citas()  # Obtiene las mascotas del controlador.

        for cita in citas:  # Recorre cada cita de la lista.
            self.tabla.insert(
                "",
                "end",
                values=(
                    cita["id_cita"],  # Identificador de la cita.
                    cita["fecha"],  # Fecha de la cita.
                    cita["motivo"]  # Motivo de la consulta.
                )
            )  # Agrega la cita a una fila de la tabla.
            
    # Método para seleccionar los datos de una cita.
    def seleccionar(self, event=None):
        seleccion = self.tabla.selection()  # Obtiene la fila seleccionada.
        if not seleccion:  # Revisa si no hay una fila seleccionada.
            return  # Sale del método si no hay selección.

        valores = self.tabla.item(seleccion[0], "values")  # Obtiene los datos de la fila.
        self.id_seleccionado = valores[0]  # Guarda el identificador de la cita.
        self.limpiar_campos()  # Borra los textos sin quitar la selección.

        self.txt_fecha.insert(0, valores[1])  # Coloca la fecha.
        self.txt_motivo.insert(0, valores[2])  # Coloca el motivo.

    # Método para obtener los datos del formulario de citas.
    def datos_formulario(self):
        return (
            self.txt_fecha.get().strip(),  # Obtiene la fecha sin espacios al inicio y al final.
            self.txt_motivo.get().strip()  # Obtiene el motivo sin espacios al inicio y al final.
        )

    # Método para guardar una cita.
    def guardar(self):
        self.controller.guardar(self.datos_formulario())  # Envía la fecha y el motivo al controlador.
        
        # Pide al controlador que abra la ventana de mascotas.
    def volver_mascotas(self):
        self.controller.volver_mascotas()

    # Método para eliminar una cita.
    def eliminar(self):
        self.controller.eliminar(self.id_seleccionado)  # Envía el identificador de la cita seleccionada.

    # Método para limpiar los campos.
    def limpiar_campos(self):
        for campo in (
            self.txt_fecha,  # Campo de la fecha.
            self.txt_motivo,  # Campo del motivo.
        ):
            campo.delete(0, tk.END)  # Borra todo el texto del campo.
            
    # Método para limpiar el formulario y quitar la selección.
    def limpiar(self):
        self.id_seleccionado = None  # Borra el identificador de la cita seleccionada.
        self.limpiar_campos()  # Borra la fecha y el motivo.
        for fila in self.tabla.selection():  # Recorre las filas seleccionadas.
            self.tabla.selection_remove(fila)  # Quita la selección.
        self.txt_fecha.focus()  # Coloca el cursor en el campo de la fecha.