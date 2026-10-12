#Esta es el segundo avance del proyecto de la materia Programación dos, aquí utilizamos los nuevos conceptos como la herencia.
#Hicimos una subclase que hereda lo de Libro, difinimos un atributo como privado y sobreescribirmos un método


#Clase principal
class Libro:
    def __init__(self, titulo, autor, editorial, genero, precio, stock):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.genero=genero
        self.__precio=precio #Atributo privado
        self.stock=stock

    #métodos de acceso seguro Getters  y Setter
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio=nuevo_precio
            print(f"El precio del libro {self.titulo} ha sido actualizado a ${self.__precio}")
        else:
            print("El precio debe de ser mayor que 0")

    #métodos normales    
    def mostrar_info(self,):
        print(f"""
              INFORMACIÓN DEL LIBRO 
              {self.titulo}:
              Autor: {self.autor}
              Editorial: {self.editorial}
              Genero: {self.genero}
              Precio: ${self.__precio}
              Unidades disponibles: {self.stock}
              """)
    def aplicar_descuento(self,descuento):
        calculo_descuento= self.__precio * (descuento/100)
        print(f"Se te descontarán ${calculo_descuento:.2f} de ${self.__precio:.2f}")
        precio_final=self.__precio - calculo_descuento
        print(f"TOTAL: {self.titulo} ---- ${precio_final:.2f}")
    
    def vender(self,comprados):
        if comprados <= self.stock:
            self.stock -= comprados
            print(f"SE REALIZO LA COMPRA DE {comprados} libros de {self.titulo}")
            print(f"Quedaron disponibles {self.stock} a la venta")
        else:
            print(f"No se puede realizar la venta de {self.titulo} ya que estan disponibles {self.stock} y tu pediste {comprados}")
    
    def reponer_stock(self,cantidad):
        self.stock += cantidad
        print(f"""Se agregaron {cantidad} al stock de {self.titulo}
              Nuevo stock disponible : {self.stock}
              """)

#Subclase que hereda lo de libro
class LibroDigital(Libro):
    #Los atributos únicos de esta clase son tamaño_mb (tamño en magabytes) y formato (PDF, EPUB,etc)
    def __init__(self, titulo, autor, editorial, genero, precio, stock, tamaño_mb, formato):
        # super() reutiliza los atributos del constructor del padre
        super().__init__(titulo, autor, editorial, genero, precio, stock)

        #Atributos únicos de la subclase
        self.tamaño_mb=tamaño_mb
        self.formato=formato

    #Método de la subclase
    def descargar(self):
        print(f"Compra completada \n Descargando '{self.titulo}' ({self.formato}, {self.tamaño_mb} MB)...")
    #método sobrescrito 
    def mostrar_info(self):
        print(f"""
        INFORMACIÓN DEL LIBRO DIGITAL:
        {self.titulo}
        Autor: {self.autor} | Género: {self.genero}
        Formato: {self.formato} ({self.tamaño_mb} MB)
        Precio: ${self.get_precio()}
        Licencias disponibles: {self.stock}
        """)



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

#Pruebas de la subclase
print("\n PRUEBAS DE LA SUBCLASE\n")
#Creamos objetos de la subclase LibroDigital
el_tunel = LibroDigital("El túnel", "Ernesto Sábato", "Planeta", "Filosofía", 228, 100, 12.5, "PDF")
el_principito = LibroDigital("El Principito", "Antoine de Saint-Exupéry", "Reynal & Hitchcock", "Fábula", 15.0, 100, 5, "EPUB")
#Prueba de los métodos
el_principito.descargar()
el_tunel.descargar() #método propio
el_principito.mostrar_info()
el_tunel.mostrar_info()     #método sobrescrito

#Prueba del encapsulamiento desde la subclase (Getter y Setter del precio)
print(f"Precio original de {el_tunel.titulo}: ${el_tunel.get_precio()}")
# Modificación exitosa
el_tunel.set_precio(28.50)
print(f"Le pedimos solo el precio y con eso comprobamos que sí se cambio: {el_tunel.get_precio()}")
# Si intentamos poner un precio invalido, nos dará el print que pusimos en el método de la clase padre 
el_tunel.set_precio(-5)
