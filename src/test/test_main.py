from src.main import validar_producto

#def test_validar_usuario_correcto():
#    assert validar_usuario("usuario1", "contraseña123") is True


def test_validar_producto_correcto():
    assert validar_producto("1234567890123456789", 1000, 20) is True
    
def test_validar_producto_codigo_incorrecto():
    assert validar_producto("12345678901234512312367890", 1000, 0) is False

def test_validar_producto_precio_incorrecto():
    assert validar_producto("12345678901234567890", -500, 20) is False

def test_validar_producto_sin_stock():
    assert validar_producto("12345678901234567890", 1000, -1) is False

def test_validar_producto_codigoprecio_incorrectos():
    assert validar_producto("12312123123123123121", -1000, 20) is False

def test_validar_producto_codigostock_incorrectos():
    assert validar_producto("1231212312312312312123", -2000, -2) is False

def test_validar_producto_preciostock_incorrectos():
    assert validar_producto("12312123123123123121", -2000, -2) is False

def test_validar_producto_codigostockprecio_incorrectos():
    assert validar_producto("12312123123123123121231", -10, -10) is False