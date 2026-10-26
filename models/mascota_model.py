from models.base_model import BaseModel
#crear el objeto
class MascotaModel(BaseModel):
    def listar(self):
        return self._consultar("SELECT * FROM TABLA MASCOTA ORDER BY id_mascota ASC")
    
    #metodo de insertar
    def insertar(self, nombre, especie, raza, edad, propietario):
        self._ejecutar(
            """ 
            INSERT INTO mascota(nombre, especie, raza, edad, propietario) VALUES (%s, %s, %s, %s, %s)
            """,
            #datos como tuplas
            (nombre, especie, raza, edad, propietario),
        )
        
    def actualizar(self, id_mascota, nombre, especie, raza, edad, propietario):
        self._ejecutar(
            """ 
            UPDATE SET nombre =%s, especie = %s, raza = %s, edad = %s, propietario = %s WHERE id_mascota = %s
            """,
            #datos como tuplas
            (nombre, especie, raza, edad, propietario, id_mascota),
        )
    #metodo de eliminar
    def eliminar(self, id_mascota):
        return self._ejecutar("DELETE FROM mascota WHERE id_mascota = %s")