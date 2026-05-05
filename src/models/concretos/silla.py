"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

from ..categorias.asientos import Asiento

class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        precio_base: float,
        capacidad_personas: int = 1,
        color: str = "N/A",
        tiene_respaldo: bool = True,
        material_tapizado: str = None,
        altura_regulable: bool = False,
        tiene_ruedas: bool = False,
        **kwargs,
    ):
        # Aseguramos que el precio sea float antes de subirlo al padre
        precio_numerico = float(precio_base)
        
        super().__init__(
            nombre=nombre, 
            material=material, 
            color=color, 
            precio_base=precio_numerico,
            capacidad_personas=capacidad_personas,
            tiene_respaldo=tiene_respaldo, 
            material_tapizado=material_tapizado,
        )
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

    @property
    def precio_base(self) -> float:
        """
        Getter para recuperar el precio desde la clase base.
        Busca los nombres de atributo más comunes en Mueble.
        """
        for attr in ['_precio_base', '_precio', 'precio_base']:
            if hasattr(self, attr):
                return float(getattr(self, attr))
        return 0.0

    def calcular_precio(self) -> float:
        """
        Calcula el precio final sumando los adicionales de silla.
        """
        # Intentamos obtener el precio base procesado por el padre (con descuentos si existen)
        try:
            precio = float(super().calcular_precio())
        except (AttributeError, TypeError):
            precio = self.precio_base

        # Adicionales por funcionalidad
        if getattr(self, '_altura_regulable', False):
            precio += 30.0
        if getattr(self, '_tiene_ruedas', False):
            precio += 20.0

        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """Genera la descripción textual para los tests."""
        # Usamos getattr para evitar errores si el padre no inicializó los atributos
        nombre = getattr(self, 'nombre', 'Silla')
        material = getattr(self, 'material', 'N/A')
        color = getattr(self, 'color', 'N/A')
        
        desc = f"Silla: {nombre}\n"
        desc += f"  Material: {material}\n"
        desc += f"  Color: {color}\n"
        
        # Info del padre
        if hasattr(self, 'obtener_info_asiento'):
            desc += f"  {self.obtener_info_asiento()}\n"
            
        desc += f"  Altura regulable: {'Sí' if getattr(self, '_altura_regulable', False) else 'No'}\n"
        desc += f"  Ruedas: {'Sí' if getattr(self, '_tiene_ruedas', False) else 'No'}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc