from models.base_model import BaseModel  # Reutiliza la conexión y las consultas.


class ProductoModel(BaseModel):
    # Consulta todos los registros para mostrarlos en la tabla.
    def listar(self):
        return self._consultar("SELECT id_producto, nombre, descripcion, precio, stock FROM productos ORDER BY id_producto ASC")

    # Guarda un registro nuevo; los valores se envían separados del SQL.
    def insertar(self, nombre, descripcion, precio, stock):
        return self._ejecutar(
            "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)",
            (nombre, descripcion, precio, stock)
        )

    # Cambia solamente el registro que tenga el identificador seleccionado.
    def actualizar(self, identificador, nombre, descripcion, precio, stock):
        return self._ejecutar(
            "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s WHERE id_producto = %s",
            (nombre, descripcion, precio, stock, identificador)
        )

    # Borra solamente el registro seleccionado.
    def eliminar(self, identificador):
        return self._ejecutar("DELETE FROM productos WHERE id_producto = %s", (identificador,))
