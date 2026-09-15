class Libro:
    def __init__(self, titulo, autor, editorial, genero, precio, stock):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.genero=genero
        self.precio=precio
        self.stock=stock
        
    def mostrar_info(self,):
        print(f"""
              INFORMACIÓN DEL LIBRO 
              {self.titulo}:
              Autor: {self.autor}
              Editorial: {self.editorial}
              Genero: {self.genero}
              Precio: ${self.precio}
              Unidades disponibles: {self.stock}
              """)
    def aplicar_descuento(self,descuento):
        calculo_descuento= self.precio * (descuento/100)
        print(f"Se te descontarán ${calculo_descuento:.2f} de ${self.precio:.2f}")
        precio_final=self.precio - calculo_descuento
        print(f"TOTAL: {self.titulo} ---- ${precio_final}")
    
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
        
invisible=Libro("Invisible", "Eloy Moreno", "Nube de tinta", "Drama", 389, 100)
sobre_tu_cadaver=Libro("Sobre tu cadaver", "Dan Wells", "VRYA", "Acción", 200, 100)
lagrimas_de_bosque=Libro("Lágrimas de bosque", "Nathalie Bernard", "Fondo de cultura económica", "Suspenso", 198, 100)

invisible.mostrar_info()
sobre_tu_cadaver.mostrar_info()
lagrimas_de_bosque.mostrar_info()

invisible.aplicar_descuento(20)
sobre_tu_cadaver.vender(40)
lagrimas_de_bosque.reponer_stock(300)

invisible.mostrar_info()
sobre_tu_cadaver.mostrar_info()
lagrimas_de_bosque.mostrar_info()
