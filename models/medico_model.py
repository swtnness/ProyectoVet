from models.base_model import BaseModel  # Reutiliza la conexión y las consultas.


class MedicoModel(BaseModel):
    # Consulta todos los registros para mostrarlos en la tabla.
    def listar(self):
        return self._consultar("SELECT id_medico, nombre, especialidad, telefono, correo FROM medico ORDER BY id_medico ASC")

    # Guarda un registro nuevo; los valores se envían separados del SQL.
    def insertar(self, nombre, especialidad, telefono, correo):
        return self._ejecutar(
            "INSERT INTO medico (nombre, especialidad, telefono, correo) VALUES (%s, %s, %s, %s)",
            (nombre, especialidad, telefono, correo)
        )

    # Cambia solamente el registro que tenga el identificador seleccionado.
    def actualizar(self, identificador, nombre, especialidad, telefono, correo):
        return self._ejecutar(
            "UPDATE medico SET nombre = %s, especialidad = %s, telefono = %s, correo = %s WHERE id_medico = %s",
            (nombre, especialidad, telefono, correo, identificador)
        )

    # Borra solamente el registro seleccionado.
    def eliminar(self, identificador):
        return self._ejecutar("DELETE FROM medico WHERE id_medico = %s", (identificador,))
