def test_creacion_silla(silla_base):
    assert silla_base.nombre == "Silla Minimal"
    assert silla_base.capacidad == 1

def test_descripcion_silla(silla_base):
    assert "1 personas" in silla_base.obtener_descripcion()