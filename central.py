from fabrica import crearPieza,agregarPieza,verPedido
lista=[]

#pedir datos por teclado
id=input("Digita el id: ")

#Llamar a la funcion que crea la pieza
pieza = crearPieza(id,"abcd001","plato maravilloso",50000,100,10,"01/04/2025")

#Llamar a la funcion que agrega la pieza a la lista
agregarPieza(lista,pieza)

#Llamar a la funcion que meustra la lista
verPedido(lista)