"""
Clase concreta Mesa.
Representa una mesa genérica.
"""

from ..categorias.superficies import Superficie


class Mesa(Superficie):
    """
    Clase concreta que representa una mesa.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        precio_base: float,
        forma: str = "rectangular",
        capacidad_personas: int = 4,
        largo: float = 120.0,
        ancho: float = 80.0,
        altura: float = 75.0,
        color: str = "N/A",
        **kwargs,
    ):
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._forma = forma
        self._capacidad_personas = capacidad_personas

    @property
    def forma(self) -> str:
        """Getter para forma."""
        return self._forma

    @forma.setter
    def forma(self, value: str) -> None:
        """Setter para forma con validación."""
        formas_validas = ["rectangular", "redonda", "cuadrada", "ovalada"]
        if value not in formas_validas:
            raise ValueError(f"Forma debe ser una de: {formas_validas}")
        self._forma = value

    @property
    def capacidad_personas(self) -> int:
        """Getter para capacidad de personas."""
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        """Setter para capacidad con validación."""
        if value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value

    def calcular_precio(self) -> float:
        """Calcula el precio final de la mesa."""
        return round(float(self.precio_base), 2)

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada de la mesa.
        """
        desc = f"Mesa: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  Forma: {self.forma}\n"
        desc += f"  {self.obtener_info_superficie()}\n"
        desc += f"  Capacidad: {self.capacidad_personas} personas\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc
