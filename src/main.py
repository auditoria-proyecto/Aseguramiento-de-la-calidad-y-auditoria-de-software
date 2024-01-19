
#Valida los productos disponibles para compra, verificando el código (máx 20 caracteres), precio y cantidad positiva.
def validar_producto(codigo_producto, precio, cantidad):

    if len(codigo_producto) > 20:
        return False
    
    if precio < 0:
        return False

    if cantidad < 0:
        return False

    #Si todas las verificaciones son exitosas, devuelve True
    return True


