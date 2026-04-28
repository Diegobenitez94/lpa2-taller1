import pytest
from src.models.categorias.asientos import Asiento

@pytest.fixture
def silla_base():
    return Asiento(nombre="Silla Minimal", material="Madera", precio=50.0, capacidad=1)

@pytest.fixture
def datos_validos_mueble():
    return {"nombre": "Mesa Pro", "material": "Acero", "precio": 150.0}