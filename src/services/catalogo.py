from src.models.mueble import Mueble

class Catalogo:
    def __init__(self):
        self._muebles = []

    def agregar_mueble(self, mueble: Mueble):
        if not isinstance(mueble, Mueble):
            raise ValueError("Solo se pueden agregar objetos tipo Mueble")
        self._muebles.append(mueble)

    def listar_muebles(self):
        return self._muebles

    def buscar_por_nombre(self, nombre: str):
        return [m for m in self._muebles if nombre.lower() in m.nombre.lower()]