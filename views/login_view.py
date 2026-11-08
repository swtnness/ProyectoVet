from tkinter import ttk  # Importa los elementos para crear etiquetas, campos y botones.


class LoginView:  # Crea la vista de la ventana de inicio de sesión.
    def __init__(self, root, controller):  # Prepara la ventana cuando se crea la vista.
        self.root = root  # Guarda la ventana principal.
        self.controller = controller  # Guarda el controlador que revisa el inicio de sesión.

        self.root.title("Login Veterinaria")  # Coloca el título de la ventana.
        self.root.geometry("400x400")  # Define el tamaño de la ventana en píxeles.
        self.root.resizable(False, False)  # Evita que se cambie el ancho o el alto.
        self.root.configure(bg="#FCE4EC")  # Coloca un fondo rosado claro.

        style = ttk.Style()  # Crea el objeto que permite cambiar el diseño de los elementos.
        style.theme_use("clam")  # Usa el tema clam para aplicar los colores y estilos.

        # Coloca el fondo rosado en los contenedores.
        style.configure("TFrame", background="#FCE4EC")

        # Cambia el fondo y el color del texto de las etiquetas.
        style.configure(
            "TLabel",
            background="#FCE4EC",  # Fondo rosado.
            foreground="#8E6280"  # Color del texto.
        )

        # Cambia el diseño de los campos donde se escribe.
        style.configure(
            "TEntry",
            fieldbackground="#FFF8E1",  # Fondo crema dentro del campo.
            foreground="#8E6280",  # Color del texto que se escribe.
            padding=5  # Deja espacio entre el texto y los bordes.
        )

        # Cambia el diseño de los botones.
        style.configure(
            "TButton",
            background="#F8BBD0",  # Fondo rosado del botón.
            foreground="#8E6280",  # Color del texto del botón.
            font=("Arial", 11, "bold"),  # Usa letra Arial, tamaño 11 y en negrita.
            padding=10  # Deja espacio alrededor del texto dentro del botón.
        )

        # Cambia el fondo del botón cuando el mouse pasa por encima.
        style.map("TButton", background=[("active", "#EDE7F6")])

        frame = ttk.Frame(root, padding=30)  # Crea un contenedor con espacio alrededor de los elementos.
        frame.pack(expand=True)  # Ubica el contenedor y lo centra en el espacio disponible.

        # Coloca el título dentro del formulario.
        ttk.Label(
            frame,  # Indica que la etiqueta va dentro del contenedor.
            text="Sistema veterinario",  # Texto que se muestra.
            font=("Arial", 18, "bold")  # Tamaño y tipo de letra del título.
        ).pack(pady=(0, 20))  # Deja 20 píxeles de espacio debajo del título.

        # Etiqueta y campo para el usuario.
        ttk.Label(frame, text="Usuario").pack(anchor="w")  # Coloca la etiqueta a la izquierda.
        self.textUsuario = ttk.Entry(frame, width=35)  # Crea el campo para escribir el usuario.
        self.textUsuario.pack(pady=(0, 10))  # Ubica el campo y deja espacio debajo.

        # Etiqueta y campo para la contraseña.
        ttk.Label(frame, text="Contraseña").pack(anchor="w")  # Coloca la etiqueta a la izquierda.
        self.textPassword = ttk.Entry(
            frame,
            width=35,  # Define el ancho aproximado del campo en caracteres.
            show="*"  # Muestra asteriscos para ocultar la contraseña en pantalla.
        )
        self.textPassword.pack(pady=(0, 20))  # Ubica el campo y deja espacio debajo.

        # Botón para iniciar sesión.
        ttk.Button(
            frame,
            text="Iniciar Sesion",  # Texto que aparece en el botón.
            command=self.iniciar_sesion  # Llama al método al hacer clic.
        ).pack(fill="x")  # Hace que el botón ocupe el ancho disponible del contenedor.

        self.textUsuario.focus()  # Coloca el cursor en el campo del usuario.

        # Permite iniciar sesión al presionar Enter desde el campo de contraseña.
        self.textPassword.bind(
            "<Return>",  # Detecta cuando se presiona Enter.
            lambda event: self.iniciar_sesion()  # Llama al mismo método que usa el botón.
        )

    # Método que envía los datos al controlador.
    def iniciar_sesion(self):
        self.controller.iniciar_sesion(
            self.textUsuario.get().strip(),  # Obtiene el usuario y quita espacios al inicio y al final.
            self.textPassword.get()  # Obtiene la contraseña tal como fue escrita.
        )