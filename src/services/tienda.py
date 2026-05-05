"""
Servicio de la tienda que maneja la lógica de negocio.
Esta clase implementa el patrón de servicio para separar la lógica de negocio de la UI.
"""

from typing import List, Dict, Optional, Union
from datetime import datetime
from src.models.mueble import Mueble
from src.models.composicion.comedor import Comedor

class Tienda:
    """
    Clase que maneja toda la lógica de negocio de la tienda de muebles.
    """

    def __init__(self, nombre: str = "Mueblería OOP"):
        self._nombre = nombre
        self._inventario: List["Mueble"] = []
        self._comedores: List["Comedor"] = []
        self._ventas_realizadas: List[Dict] = []
        self._descuentos_activos: Dict[str, float] = {}
      
        self._total_muebles_vendidos: int = 0
        self._valor_total_ventas: float = 0.0

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def inventario(self) -> List["Mueble"]:
        return self._inventario

    def agregar_producto(self, mueble: "Mueble") -> str:
        """Agrega un mueble al inventario de la tienda."""
        if mueble is None:
            return "Error: El mueble no puede ser None"
        try:
            precio = mueble.calcular_precio()
            if float(precio) <= 0:
                return "Error: El mueble debe tener un precio válido mayor a 0"
        except (ValueError, TypeError, AttributeError):
            
            return "Error: Datos de precio inválidos"
            
        self._inventario.append(mueble)
        return f"Mueble {getattr(mueble, 'nombre', 'Sin nombre')} agregado exitosamente"

    
    def vender_producto(self, identificador_mueble: Union["Mueble", str], cliente: str = "Cliente Anónimo") -> Union[Dict, str]:
        """
        Vende un producto del inventario. 
        Soporta recibir el objeto Mueble o el nombre del mismo (para flexibilidad del test).
        """
        mueble_encontrado = None
        
        
        if isinstance(identificador_mueble, str):
            for m in self._inventario:
                if getattr(m, 'nombre', '') == identificador_mueble:
                    mueble_encontrado = m
                    break
        else:
            if identificador_mueble in self._inventario:
                mueble_encontrado = identificador_mueble

        if mueble_encontrado is None:
            print("El mueble no está disponible en inventario")
            return False
        
        try:
            precio_original = float(mueble_encontrado.calcular_precio())
            tipo_mueble = type(mueble_encontrado).__name__
            descuento_porcentaje = self._descuentos_activos.get(tipo_mueble, 0.0)
            
            precio_final = precio_original * (1 - descuento_porcentaje)
            
            venta = {
                "mueble": getattr(mueble_encontrado, "nombre", tipo_mueble),
                "cliente": cliente,
                "precio_original": precio_original,
                "descuento": descuento_porcentaje * 100,
                "precio_final": round(precio_final, 2),
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            
            self._ventas_realizadas.append(venta)
            self._inventario.remove(mueble_encontrado)
            self._total_muebles_vendidos += 1
            self._valor_total_ventas += venta["precio_final"]
            print(f"Mueble {getattr(mueble_encontrado, 'nombre', tipo_mueble)} vendido")
            return True
        except Exception as e:
            print(f"Error en venta: {str(e)}")
            return False

    def obtener_estadisticas(self) -> dict:
        """Calcula estadísticas del estado actual de la tienda."""
        valor_inventario = 0.0
        for mueble in self._inventario:
            try:
                valor_inventario += float(mueble.calcular_precio())
            except:
                continue

        return {
            "total_muebles": len(self._inventario),
            "valor_inventario": round(valor_inventario, 2),
            "total_muebles_vendidos": self._total_muebles_vendidos,
            "valor_total_ventas": round(self._valor_total_ventas, 2),
        }