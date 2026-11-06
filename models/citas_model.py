from models.base_model import BaseModel  # Importa la clase que realiza las consultas.


class CitaModel(BaseModel):
        # Obtiene las citas de la mascota seleccionada.
    def listar_por_mascota(self, id_mascotas):
        return self._consultar(
            """
            SELECT * FROM cita
            WHERE id_mascotas = %s
            ORDER BY fecha ASC
            """,
            (id_mascotas,)
        )
    # Guarda una cita nueva.
    def insertar(self, id_mascotas, fecha, motivo):
        self._ejecutar(
            """
            INSERT INTO cita (id_mascotas, fecha, motivo)
            VALUES (%s, %s, %s)
            """,
            (id_mascotas, fecha, motivo)
        )  # Guarda la mascota, la fecha y el motivo de la cita.

    # Elimina la cita seleccionada.
    def eliminar(self, id_cita):
        return self._ejecutar(
            "DELETE FROM cita WHERE id_cita = %s",
            (id_cita,)
        )  # Envía el identificador de la cita que se eliminará.