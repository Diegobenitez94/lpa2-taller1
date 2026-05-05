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
        color: str,
        precio_base: float, 
        tiene_respaldo: bool = True,
        material_tapizado: str = None,
        altura_regulable: bool = False,
        tiene_ruedas: bool = False,
    ):
       
        super().__init__(
            nombre, 
            material, 
            color, 
            float(precio_base), 
            1,                  
            tiene_respaldo, 
            material_tapizado
        )
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

    
    @property
    def precio_base(self) -> float:
       
        return getattr(self, '_precio', 0.0)

    def calcular_precio(self) -> float:
        """
        Calcula el precio final de la silla sumando extras.
        """
        
        try:
           
            precio = float(super().calcular_precio())
        except (AttributeError, TypeError, ValueError):
            
            precio = float(self.precio_base)

        
        if self._altura_regulable:
            precio += 30.0
        if self._tiene_ruedas:
            precio += 20.0

        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """Descripción detallada con los atributos correctos."""
        desc = f"Silla: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  {self.obtener_info_asiento() if hasattr(self, 'obtener_info_asiento') else ''}\n"
        desc += f"  Altura regulable: {'Sí' if self._altura_regulable else 'No'}\n"
        desc += f"  Ruedas: {'Sí' if self._tiene_ruedas else 'No'}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc
    
    