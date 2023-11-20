class Jugador:
    def __init__(self,nombre, año, sexo, beca):
        self.nombre=nombre
        self.año=año
        self.sexo=sexo
        self.beca=beca
        if beca=="Becado":
            beca=0
        else:
            beca=1
        self.total=beca
        if sexo=="M":
            sexo=1
        else:
            sexo=0
        self.mujer=sexo

      
    def __str__(self):
        return f"Nombre: {self.nombre:<20} Año de Nacimiento: {self.año:<10} Sexo: {self.sexo:<10} Beca: {self.beca:<5} "
        
class Categoria:
    def __init__(self,nombre, rango, costo):
        self.nombre=nombre
        self.rango=rango
        self.costo=costo
        self.jugadores=list()

    def agregarJugador(self,jugador):
        self.jugadores.append(jugador)

    def totalJugador(self):
        total=0
        for jugador in self.jugadores:
            total+=self.costo*jugador.total
        return total

    def totalMujer(self):
        mujer=0
        for jugador in self.jugadores:
            mujer+=jugador.mujer
        return mujer


    def __str__(self):
        return f"Nombre: {self.nombre:<15} Rango: {self.rango:<10} Costo: ${self.costo:<10.2f}"

class Academia:
    def __init__(self,nombre,propietario,domicilio):
        self.nombre=nombre
        self.propietario=propietario
        self.domicilio=domicilio
        self.categorias =list()

    def agregarCategoria(self,categoria):
        self.categorias.append(categoria)

    def totalJugador(self):
        total=0
        for categoria in self.categorias:
            total+=len(categoria.jugadores)
        return total

    def totalImporte(self):
        total=0
        for categoria in self.categorias:
            total+=categoria.totalJugador();
        return total
##
    def totalMujer(self):
        mujer=0
        for categoria in self.categorias:
            mujer+=len(categoria.jugadores)
        return mujer

    def totalImporteM(self):
        mujer=0
        for categoria in self.categorias:
            mujer+=categoria.totalMujer()
        return mujer
    
    def totalImporteH(self):
        mujer=0
        for categoria in self.categorias:
            mujer+=len(categoria.jugadores)-categoria.totalMujer()
        return mujer

    
    def __str__(self):
        return f"Nombre:{self.nombre} \nPropietario:{self.propietario} \nDomiciio:{self.domicilio}"

#PROGRAMA PRINCIPAL
#Academia
miAcademia = Academia(nombre=" Academia Santos Laguna", propietario=" Francisco Nava", domicilio=" Aguanaval 123, Hidraulica")

#Categoria
miAcademia.agregarCategoria(Categoria(nombre="Junior A", rango= 2006, costo=1000))
miAcademia.agregarCategoria(Categoria(nombre="Junior B", rango= 2005, costo=1500))
miAcademia.agregarCategoria(Categoria(nombre="Junior C", rango= 2004, costo=2000))

#Jugadores
miAcademia.categorias[0].agregarJugador(Jugador(nombre="Juana Maria Lopez", año=2006, sexo="M", beca="Becado"))
miAcademia.categorias[0].agregarJugador(Jugador(nombre="Marisol Luna", año=2006, sexo="M", beca="Becado"))
miAcademia.categorias[1].agregarJugador(Jugador(nombre="Alejandra Daiz", año=2005, sexo="M", beca="Sin Beca"))
miAcademia.categorias[1].agregarJugador(Jugador(nombre="Carlos Dominguez", año=2005, sexo="H", beca="Sin Beca"))
miAcademia.categorias[2].agregarJugador(Jugador(nombre="Roberto Barrios", año=2004, sexo="H", beca="Sin Beca"))
miAcademia.categorias[2].agregarJugador(Jugador(nombre="Angelica Garcia", año=2004, sexo="M", beca="Sin Beca"))


#REPORTE
print("\nREPORTE DEL CLUB DEPORTIVO\n")
print(miAcademia)
print(f"\nTotal de categorias : {len(miAcademia.categorias)}")
print(f'Total jugadores : {miAcademia.totalJugador()}')
print(f"Total Mujeres: {miAcademia.totalImporteM()}")
print(f"Total Hombres: {miAcademia.totalImporteH()}")

print("\n>>Datos generales de las Categorias:")
for categorias in miAcademia.categorias:
    print(categorias)

print("\n>>Jugadores por categoria")
for categorias in miAcademia.categorias:
    print(f"\n> {categorias.nombre} -- {categorias.rango} ")
    for jugador in categorias.jugadores:
        print(f'{jugador}')
    print(f"-Subtotal: $ {categorias.totalJugador():,.2f}")
  
print(f"\nTotal : {miAcademia.totalImporte():,.2f}")

