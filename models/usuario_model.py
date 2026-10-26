import hashlib
from models.base_model import BaseModel

class UsuarioModel(BaseModel):
    def validar_usuario(self, usuario, password):

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        return self._consultar(
            "SELECT * FROM usuarios WHERE usuario = %s AND password = %s",
            (usuario, password_hash),
            uno=True
        )
