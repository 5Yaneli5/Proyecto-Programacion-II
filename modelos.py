#Ahora un Libro "tiene" una lista de objetos Reseña (clase auxiliar) y usa sus métodos


#Clase auxiliar (composición): representa una reseña de un libro
class Reseña:
    def __init__(self, usuario, calificacion, comentario):
        self.usuario=usuario
        self.calificacion=calificacion
        self.comentario=comentario

    def mostrar(self):
        print(f"  {self.usuario}: {self.calificacion}/5: {self.comentario}")


#Clase principal
class Libro:
    def __init__(self, titulo, autor, editorial, genero, precio, stock):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.genero=genero
        self.__precio=precio #Atributo privado
        self.stock=stock
        self.reseñas=[] #Composición: lista de objetos Reseña

    #métodos de acceso seguro Getters  y Setter
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio=nuevo_precio
            print(f"El precio del libro {self.titulo} ha sido actualizado a ${self.__precio}")
        else:
            print("El precio debe de ser mayor que 0")

    #métodos que trabajan con la composición
    def agregar_reseña(self, usuario, calificacion, comentario):
        if calificacion >= 1 and calificacion <= 5:
            nueva_reseña = Reseña(usuario, calificacion, comentario) #Se crea el objeto Reseña
            self.reseñas.append(nueva_reseña)                        #Se guarda en la lista
            print(f"Reseña de {usuario} agregada a {self.titulo}")
        else:
            print("La calificación debe estar entre 1 y 5")

    def promedio_calificacion(self):
        if len(self.reseñas) == 0:
            return 0
        suma = 0
        for reseña in self.reseñas:
            suma += reseña.calificacion
        return suma / len(self.reseñas)

    def mostrar_reseñas(self):
        print(f"\nRESEÑAS DE {self.titulo}:")
        if len(self.reseñas) == 0:
            print("Aún no hay reseñas")
        for reseña in self.reseñas:
            reseña.mostrar() #Cada Reseña sabe cómo mostrarse por su método en su clase

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
              Calificación promedio: {self.promedio_calificacion():.1f}
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
        # super() reutiliza los atributos del constructor del padre (incluida la lista de reseñas)
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
        Calificación promedio: {self.promedio_calificacion():.1f}
        """)
