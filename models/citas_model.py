from models.base_model import BaseModel
#crear el objeto
class CitaModel(BaseModel):
    def listar_por_mascota(self, id_mascota):
        return self._consultar("SELECT * FROM CITA WHERE id_mascota = %s ORDER BY fecha ASC", (id_mascota,))
    
    #metodo de insertar
    def insertar_por_cita(self, id_mascota, fecha, motivo):
        self._ejecutar(
            """ 
            INSERT INTO cita(id_mascota, fecha, motivo) VALUES (%s, %s, %s)
            """,
            #datos como tuplas
            (id_mascota, fecha, motivo),
        )
        
    #metodo de eliminar
    def eliminar(self, id_cita):
        return self._ejecutar("DELETE FROM cita WHERE id_cita = %s", (id_cita,))