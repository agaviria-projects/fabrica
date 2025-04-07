#una fabrica de productos ceramicos
#elabora 10 productos para CORONA
#cada producto esta identificado por
#id,referencia,(8 caracteres),descripcion,
#precio de fabricacion individual
#numero de piezas fabricadas
#numero de piezas defectuosas
#fecha de envio de las piezas

#construya una funcion para agregar piezas al pedido
#construya una funcion para ver el pedido

def agregarPieza(lista,pieza):
    lista.append(pieza)
    return lista

def crearPieza(id, referencia, descripcion, precio, numeroFabricadas, numeroDefectuosas, fechaEnvio):
    pieza = {
        "id": id,
        "referencia": referencia,
        "descripcion": descripcion,
        "precio": precio,
        "numeroFabricadas": numeroFabricadas,
        "numeroDefectuosas": numeroDefectuosas,
        "fechaEnvio": fechaEnvio
    }
    return pieza