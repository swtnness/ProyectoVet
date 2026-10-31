from models.base_model import BaseModel  # Importa la clase que realiza las consultas.


class MascotaModel(BaseModel):
    # Obtiene las mascotas ordenadas por su identificador.
    def listar(self):
        return self._consultar(
            "SELECT * FROM mascotas ORDER BY id_mascotas ASC"
        )

    # Guarda una mascota nueva.
    def insertar(self, nombre, especie, raza, edad, propietario):
        self._ejecutar(
            """
            INSERT INTO mascotas (nombre, especie, raza, edad, propietario)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (nombre, especie, raza, edad, propietario)
        )  # Envía los datos para guardarlos en la base de datos.

    # Actualiza los datos de la mascota seleccionada.
    def actualizar(self, id_mascotas, nombre, especie, raza, edad, propietario):
        self._ejecutar(
            """
            UPDATE mascotas
            SET nombre = %s, especie = %s, raza = %s,
                edad = %s, propietario = %s
            WHERE id_mascotas = %s
            """,
            (nombre, especie, raza, edad, propietario, id_mascotas)
        )  # Envía los nuevos datos y el identificador de la mascota.

    # Elimina la mascota seleccionada.
    def eliminar(self, id_mascotas):
        return self._ejecutar(
            "DELETE FROM mascotas WHERE id_mascotas = %s",
            (id_mascotas,)
        )  # Envía el identificador de la mascota que se eliminará.