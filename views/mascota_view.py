import tkinter as tk  # Permite crear la ventana.
from tkinter import ttk  # Permite crear los campos, botones y tabla.
from tkinter import messagebox  # Permite mostrar avisos.


class MascotaView:
    # Constructor.
    def __init__(self, root, controller):
        self.root = root  # Guarda la ventana principal.
        self.controller = controller  # Guarda el controlador.
        self.id_seleccionado = None  # Al inicio no hay una mascota seleccionada.

        # Diseño de la ventana.
        self.root.title("Vet Vannecita")
        self.root.geometry("900x600")
        self.root.minsize(800, 500)

        # Crea el formulario, la tabla y carga las mascotas.
        self.crear_formulario()
        self.crear_tabla()
        self.mostrar_mascotas()

    # Método para crear el formulario.
    def crear_formulario(self):
        frame = ttk.LabelFrame(
            self.root, text="Datos de la mascota", padding=15
        )  # Crea el recuadro del formulario.
        frame.pack(fill="x", padx=15, pady=15)  # Ubica el formulario.

        # Etiqueta y campo para el nombre.
        ttk.Label(frame, text="Nombre").grid(row=0, column=0, sticky="w")
        self.txt_nombre = ttk.Entry(frame, width=30)
        self.txt_nombre.grid(row=0, column=1, padx=8, pady=5)

        # Etiqueta y campo para la especie.
        ttk.Label(frame, text="Especie").grid(row=0, column=2, sticky="w")
        self.txt_especie = ttk.Entry(frame, width=25)
        self.txt_especie.grid(row=0, column=3, padx=8, pady=5)

        # Etiqueta y campo para la raza.
        ttk.Label(frame, text="Raza").grid(row=1, column=0, sticky="w")
        self.txt_raza = ttk.Entry(frame, width=30)
        self.txt_raza.grid(row=1, column=1, padx=8, pady=5)

        # Etiqueta y campo para la edad.
        ttk.Label(frame, text="Edad").grid(row=1, column=2, sticky="w")
        self.txt_edad = ttk.Entry(frame, width=25)
        self.txt_edad.grid(row=1, column=3, padx=8, pady=5)

        # Etiqueta y campo para el propietario.
        ttk.Label(frame, text="Propietario").grid(
            row=2, column=0, sticky="w"
        )
        self.txt_propietario = ttk.Entry(frame, width=30)
        self.txt_propietario.grid(row=2, column=1, padx=8, pady=5)

        # Contenedor de los botones.
        botones = ttk.Frame(frame)
        botones.grid(row=3, column=0, columnspan=4, pady=12)

        # Botón para guardar una mascota.
        ttk.Button(
            botones, text="Guardar", command=self.guardar
        ).pack(side="left", padx=5)

        # Botón para actualizar la mascota seleccionada.
        ttk.Button(
            botones, text="Actualizar", command=self.actualizar
        ).pack(side="left", padx=5)

        # Botón para eliminar la mascota seleccionada.
        ttk.Button(
            botones, text="Eliminar", command=self.eliminar
        ).pack(side="left", padx=5)

        # Botón para limpiar los campos.
        ttk.Button(
            botones, text="Limpiar", command=self.limpiar
        ).pack(side="left", padx=5)

        # Botón para abrir las citas de la mascota seleccionada.
        ttk.Button(
            botones, text="Citas", command=self.ver_citas
        ).pack(side="left", padx=5)

    # Método para crear la tabla.
    def crear_tabla(self):
        frame = ttk.Frame(self.root)  # Crea el contenedor de la tabla.
        frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Nombres internos de las columnas.
        columnas = (
            "id_mascotas",
            "nombre",
            "especie",
            "raza",
            "edad",
            "propietario"
        )

        # Crea la tabla y muestra solamente los encabezados y los datos.
        self.tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            selectmode="browse"
        )

        # Títulos que se muestran en la tabla.
        titulos = {
            "id_mascotas": "ID",
            "nombre": "Nombre",
            "especie": "Especie",
            "raza": "Raza",
            "edad": "Edad",
            "propietario": "Propietario"
        }

        # Ancho de cada columna.
        anchos = {
            "id_mascotas": 50,
            "nombre": 100,
            "especie": 100,
            "raza": 100,
            "edad": 50,
            "propietario": 180
        }

        # Aplica el título, ancho y alineación a cada columna.
        for columna in columnas:
            self.tabla.heading(columna, text=titulos[columna])
            self.tabla.column(
                columna, width=anchos[columna], anchor="center"
            )

        # Crea la barra para desplazarse por la tabla.
        scroll = ttk.Scrollbar(
            frame, orient="vertical", command=self.tabla.yview
        )

        # Conecta la tabla con la barra de desplazamiento.
        self.tabla.configure(yscrollcommand=scroll.set)

        # Ubica la tabla y la barra dentro del contenedor.
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Ejecuta seleccionar cuando se selecciona una fila.
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)
        
    #metodo para mostrar los datos
    def mostrar_mascotas(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        self.id_seleccionado = None  # Quita el identificador de la selección anterior.
        mascotas = self.controller.cargar_mascotas()  # Obtiene las mascotas del controlador.

        for mascota in mascotas:  # Recorre cada mascota de la lista.
            self.tabla.insert(
                "",
                "end",
                values=(
                    mascota["id_mascotas"],
                    mascota["nombre"],
                    mascota["especie"],
                    mascota["raza"],
                    mascota["edad"],
                    mascota["propietario"]
                )
            )  # Agrega los datos de la mascota a una fila.
    # Método para seleccionar los datos de una fila.
    def seleccionar(self, event=None):
        seleccion = self.tabla.selection()  # Obtiene la fila seleccionada.
        if not seleccion:  # Revisa si no hay una fila seleccionada.
            return  # Sale del método si no hay selección.

        valores = self.tabla.item(seleccion[0], "values")  # Obtiene los datos de la fila.
        self.id_seleccionado = valores[0]  # Guarda el identificador de la mascota.
        self.limpiar_campos()  # Borra los textos sin quitar la selección.

        self.txt_nombre.insert(0, valores[1])  # Coloca el nombre.
        self.txt_especie.insert(0, valores[2])  # Coloca la especie.
        self.txt_raza.insert(0, valores[3])  # Coloca la raza.
        self.txt_edad.insert(0, valores[4])  # Coloca la edad.
        self.txt_propietario.insert(0, valores[5])  # Coloca el propietario.
        
    # Método para obtener los datos del formulario.
    def datos_formulario(self):
        return (
            self.txt_nombre.get().strip(),  # Obtiene el nombre sin espacios al inicio y al final.
            self.txt_especie.get().strip(),  # Obtiene la especie.
            self.txt_raza.get().strip(),  # Obtiene la raza.
            self.txt_edad.get().strip(),  # Obtiene la edad como texto.
            self.txt_propietario.get().strip()  # Obtiene el propietario.
        )
    
    #metodo para guardar
    def guardar(self):
        self.controller.guardar(self.datos_formulario())
        
    #metodo actualizar 
    def actualizar(self):
        self.controller.actualizar(self.id_seleccionado, self.datos_formulario())

    # Método para eliminar.
    def eliminar(self):
        self.controller.eliminar(self.id_seleccionado)
        
    #metodo para limpiar campos
    def limpiar_campos(self):
        for campo in (
            self.txt_nombre,
            self.txt_especie,
            self.txt_raza,
            self.txt_edad,
            self.txt_propietario,
        ):
            
            campo.delete(0, tk.END)
    
    #deseleccionar
    def limpiar(self):
        self.id_seleccionado = None
        self.limpiar_campos()
        for fila in self.tabla.selection():  # Recorre las filas seleccionadas.
            self.tabla.selection_remove(fila)  # Quita la selección.
        self.txt_nombre.focus()
        
    #metodo para abrir la nueva ventana de citas
    def ver_citas(self):
        #verifica que se haya seleccionado una mascota de la tabla
        if not self.id_seleccionado:
            messagebox.showwarning("Aviso", "Debe seleccionar algo")
            return
        #llamar al controlador para que abra la ventana
        self.controller.abrir_citas(self.id_seleccionado)
