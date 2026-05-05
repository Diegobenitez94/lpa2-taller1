"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

# Importar List para anotaciones de tipo
from typing import List
# from ..concretos.mesa import Mesa
# from ..concretos.silla import Silla



class Comedor:
    """
    Clase que implementa composición conteniendo una mesa y sillas.
    """

    def __init__(self, nombre: str, mesa: "Mesa", sillas: List["Silla"] = None):
        self._nombre = nombre
        self._mesa = mesa
        self._sillas = sillas if sillas is not None else []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mesa(self) -> "Mesa":
        return self._mesa

    @property
    def sillas(self) -> List["Silla"]:
        return self._sillas.copy()

    def agregar_silla(self, silla: "Silla") -> str:
       
        capacidad_maxima = self._calcular_capacidad_maxima()
        if len(self._sillas) >= capacidad_maxima:
            return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}"
        
        self._sillas.append(silla)
        nombre_silla = getattr(silla, 'nombre', "Silla")
        return f"Silla {nombre_silla} agregada exitosamente al comedor"

    def quitar_silla(self, indice: int = -1) -> str:
        if not self._sillas:
            return "No hay sillas para quitar"
        try:
            silla_removida = self._sillas.pop(indice)
            nombre_silla = getattr(silla_removida, 'nombre', "Silla")
            return f"Silla {nombre_silla} removida del comedor"
        except IndexError:
            return "Índice de silla inválido"

    
    def calcular_precio(self) -> float:
        """
        Calcula el precio total del comedor sumando todos sus componentes.
        """
      
        precio_total = float(self._mesa.calcular_precio())
        
        for silla in self._sillas:
            precio_total += float(silla.calcular_precio())

        return round(precio_total, 2)

    def obtener_descripcion(self) -> str:
        """
        Alias de descripción para mantener consistencia con otros muebles.
        """
        descripcion = f"=== COMEDOR {self.nombre.upper()} ===\n"
        descripcion += f"MESA: {self._mesa.nombre}\n"
        descripcion += f"SILLAS: {len(self._sillas)} unidades\n"
        descripcion += f"PRECIO TOTAL: ${self.calcular_precio():.2f}"
        return descripcion

    def _obtener_materiales_unicos(self) -> list:
        materiales = set()
        if hasattr(self._mesa, "material"):
            materiales.add(self._mesa.material)
        for silla in self._sillas:
            if hasattr(silla, "material"):
                materiales.add(silla.material)
        return list(materiales)

    def _calcular_capacidad_maxima(self) -> int:
        return getattr(self._mesa, "capacidad_personas", 6)

    def __str__(self) -> str:
        return f"Comedor {self._nombre}: Mesa + {len(self._sillas)} sillas"

    def __len__(self) -> int:
        """Retorna el número total de muebles (mesa + sillas)."""
        return 1 + len(self._sillas)