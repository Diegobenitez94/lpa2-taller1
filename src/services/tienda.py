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
        
        # Campos acumulativos para estadísticas
        self._total_muebles_vendidos: int = 0
        self._valor_total_ventas: float = 0.0

    @property
    def nombre(self) -> str:
        return self._nombre

    def agregar_mueble(self, mueble: "Mueble") -> str:
        if mueble is None:
            return "Error: El mueble no puede ser None"
        try:
            
            precio = mueble.calcular_precio()
            
           
            if float(precio) <= 0:
                return "Error: El mueble debe tener un precio válido mayor a 0"
        except (ValueError, TypeError) as e:
            return f"Error: Tipo de dato inválido en precio: {str(e)}"
        except Exception as e:
            return f"Error al calcular precio del mueble: {str(e)}"
            
        self._inventario.append(mueble)
        return f"Mueble {getattr(mueble, 'nombre', 'Sin nombre')} agregado exitosamente"

    def obtener_estadisticas(self) -> dict:
        """Calcula estadísticas asegurando que no fallen por datos nulos."""
        try:
            valor_inventario = 0.0
            for mueble in self._inventario:
                try:
                  
                    valor_inventario += float(mueble.calcular_precio())
                except:
                    continue

            tipos_muebles = {}
            for mueble in self._inventario:
                tipo = type(mueble).__name__
                tipos_muebles[tipo] = tipos_muebles.get(tipo, 0) + 1

            return {
                "total_muebles": len(self._inventario),
                "total_comedores": len(self._comedores),
                "valor_inventario": round(valor_inventario, 2),
                "tipos_muebles": tipos_muebles,
                "descuentos_activos": self._descuentos_activos.copy(),
                "ventas_realizadas": len(self._ventas_realizadas),
                "total_muebles_vendidos": self._total_muebles_vendidos,
                "valor_total_ventas": round(self._valor_total_ventas, 2),
            }
        except Exception:
            return {"error": "No se pudieron calcular estadísticas"}

    def realizar_venta(self, mueble: "Mueble", cliente: str = "Cliente Anónimo") -> Dict:
        if mueble not in self._inventario:
            return {"error": "El mueble no está disponible en inventario"}
        
        try:
            
            precio_original = float(mueble.calcular_precio())
            
            tipo_mueble = type(mueble).__name__
            descuento_porcentaje = self._descuentos_activos.get(tipo_mueble, 0.0)
            
            precio_final = precio_original * (1 - descuento_porcentaje)
            
            venta = {
                "mueble": getattr(mueble, "nombre", tipo_mueble),
                "cliente": cliente,
                "precio_original": precio_original,
                "descuento": descuento_porcentaje * 100,
                "precio_final": round(precio_final, 2),
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            
            self._ventas_realizadas.append(venta)
            self._inventario.remove(mueble)
            self._total_muebles_vendidos += 1
            self._valor_total_ventas += venta["precio_final"]
            
            return venta
        except Exception as e:
            return {"error": f"Error en venta: {str(e)}"}