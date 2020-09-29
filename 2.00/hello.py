# cadenas
mensaje = "tengo suenio"
print(mensaje)

# es que toda cadena se transforma en un arreglo de caracteres
mensaje = "este es el anio del dragon"
print(mensaje[1])

# slicing (pedacear)
mensaje = "este es el anio del dragon"
print(mensaje[20:26])

# longitud de una cadena
mensaje = "este es el anio del dragon"
longitud = len(mensaje)
print(longitud)
print(mensaje[:longitud])

# strip() quita caracteres al inicio y al final

mensaje = "      este es el anio del dragon    "
print(mensaje.strip())

# lower en minuscula

mensaje = "ESTE ES EL ANIO DEL DRAGON"
print(mensaje.lower())

# replace

mensaje = "este es el anio del dragon"
print(mensaje.replace("dragon", "conejito"))

# split

mensaje = "manzana, uva, fresa, sandia "
print(mensaje.split(","))
listaFrutas = mensaje.split(",")
print(listaFrutas[1])

# una cadena en otra

mensaje = "este es el anio del dragon"
resultado = "dragon" in mensaje
print(resultado)
