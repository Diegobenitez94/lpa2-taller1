from unittest.mock import MagicMock

def test_comedor_calcula_precio_total():
    # Simulamos componentes (Mocking)
    mesa = MagicMock()
    mesa.precio = 200
    silla = MagicMock()
    silla.precio = 50
    
    # Lógica de composición
    precio_total = mesa.precio + (silla.precio * 4)
    assert precio_total == 400