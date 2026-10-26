from config.conexion import Conexion

class BaseModel:
    def __init__(self):
        self.db = Conexion()
    def _consultar(self, sql, params=(), uno=False):
        conexion = self.db.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, params)
                if uno:
                    return cursor.fetchone()
                else:
                    return cursor.fetchall()
        finally:
            conexion.close()
    def _ejecutar(self, sql, params=()):
        conexion = self.db.conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, params)
            conexion.commit()
        except Exception:
            conexion.rollback()
            return False
        finally:
            conexion.close()
