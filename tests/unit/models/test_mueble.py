import pytest
from src.models.mueble import Mueble

def test_no_se_puede_instanciar_mueble_abstracto():
    with pytest.raises(TypeError):
        Mueble("Error", "Metal", 100)