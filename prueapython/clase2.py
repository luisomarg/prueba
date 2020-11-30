class Hotel(object):
    """ Hotel: sus atributos son: nombre, ubicacion, puntaje y precio."""

    def __init__(self, nombre = '*', ubicacion = '*',
                 puntaje = 0, precio = float("inf")):
        """ nombre y ubicacion deben ser cadenas no vacías,
            puntaje y precio son números.
            Si el precio es 0 se reemplaza por infinito. """

        if es_cadena_no_vacia (nombre):
            self.nombre = nombre
        else:
            raise TypeError ("El nombre debe ser una cadena no vacía")

        if es_cadena_no_vacia (ubicacion):
            self.ubicacion = ubicacion
        else:
            raise TypeError ("La ubicación debe ser una cadena no vacía")

        if es_numero(puntaje):
            self.puntaje = puntaje
        else:
            raise TypeError ("El puntaje debe ser un número")

        if es_numero(precio):
            if precio != 0:
                self.precio = precio
            else:
                self.precio = float("inf")
        else:
            raise TypeError("El precio debe ser un número")

    def __str__(self):
        """ Muestra el hotel según lo requerido. """
        return self.nombre + " de "+ self.ubicacion+ \
                " - Puntaje: "+ str(self.puntaje) + " - Precio: "+ \
                str(self.precio)+ " pesos."

h = Hotel("Hotel City", "Mercedes", 3.25, 78)
print (h)