from modelos import Libro, LibroDigital

#Pruebas de la clase Base
print("\nPRUEBAS DE LA CLASE BASE\n")
invisible=Libro("Invisible", "Eloy Moreno", "Nube de tinta", "Drama", 389, 100)
sobre_tu_cadaver=Libro("Sobre tu cadaver", "Dan Wells", "VRYA", "Acción", 200, 100)
lagrimas_de_bosque=Libro("Lágrimas de bosque", "Nathalie Bernard", "Fondo de cultura económica", "Suspenso", 198, 100)
#prubea de los métodos
invisible.mostrar_info()
sobre_tu_cadaver.mostrar_info()
lagrimas_de_bosque.mostrar_info()

invisible.aplicar_descuento(20)
sobre_tu_cadaver.vender(40)
lagrimas_de_bosque.reponer_stock(300)
#Volviendo a mostrar la info de cada uno nos damos cuenta de que lo anterior si funciono como lo de reponer stock
invisible.mostrar_info()
sobre_tu_cadaver.mostrar_info()
lagrimas_de_bosque.mostrar_info()

#Pruebas de la composición (Libro tiene objetos Reseña)
print("\n PRUEBAS DE LA COMPOSICIÓN\n")
invisible.mostrar_reseñas() #Todavía no tiene reseñas
invisible.agregar_reseña("Ana", 5, "Me emocionó muchísimo")
invisible.agregar_reseña("Luis", 4, "Muy bueno, aunque algo triste")
invisible.agregar_reseña("Marta", 3, "Está bien, esperaba más")
invisible.agregar_reseña("Pedro", 8, "Calificación inválida") #No se agrega
invisible.mostrar_reseñas()
print(f"Promedio de {invisible.titulo}: {invisible.promedio_calificacion():.2f}")
#La información del libro ahora también usa sus reseñas
invisible.mostrar_info()

#Pruebas de la subclase
print("\n PRUEBAS DE LA SUBCLASE\n")
#Creamos objetos de la subclase LibroDigital
el_tunel = LibroDigital("El túnel", "Ernesto Sábato", "Planeta", "Filosofía", 228, 100, 12.5, "PDF")
el_principito = LibroDigital("El Principito", "Antoine de Saint-Exupéry", "Reynal & Hitchcock", "Fábula", 15.0, 100, 5, "EPUB")
#Prueba de los métodos
el_principito.descargar()
el_tunel.descargar() #método propio
#La subclase hereda la composición sin escribir nada extra
el_principito.agregar_reseña("Sofía", 5, "Un clásico que nunca falla")
el_principito.agregar_reseña("Diego", 5, "Perfecto para leer en cualquier edad")
el_principito.mostrar_reseñas()
el_principito.mostrar_info()
el_tunel.mostrar_info()     #método sobrescrito

#Prueba del encapsulamiento desde la subclase (Getter y Setter del precio)
print(f"Precio original de {el_tunel.titulo}: ${el_tunel.get_precio()}")
# Modificación exitosa
el_tunel.set_precio(28.50)
print(f"Le pedimos solo el precio y con eso comprobamos que sí se cambio: {el_tunel.get_precio()}")
# Si intentamos poner un precio invalido, nos dará el print que pusimos en el método de la clase padre
el_tunel.set_precio(-5)
#Pruebas de polimorfismo
print("\n PRUEBA DE POLIMORFISMO\n")
catalogo = [invisible, el_tunel, el_principito]
for libro in catalogo:
    libro.mostrar_info()   #mismo método, pero cada tipo de libro lo muestra a su manera