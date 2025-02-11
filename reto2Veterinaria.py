# Importamos la libreria datetime para trabajar con fechas
import datetime

# Creamos las clases con las que trabajarempos en este proyecto

class Persona:
    # Funcion inicializadora de atributos (Constructor)
    def __init__(self, nombre,contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion



class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super(). __init__(self, nombre, contacto, direccion)
        self.mascotas =[]


    # Funciones de la clase
    def registrar_mascota(self,mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {self.mascota} registrada exitosamente")


    def mostrar_info(self):
        print("=" * 40)
        print(f"Datos del cliente")
        print("")
        print(f" Cliente:    {self.nombre}")
        print(f" Contacto:   {self.contacto}")
        print(f" Dirección:  {self.direccion}")
        print("-" * 40)
        for mascota in self.mascotas:
            print(f"Datos de la mascota")
            print("")
            print(f"Nombre: {mascota.nombre}")
            print(f"Especie: {mascota.especie}")
            print(f"Raza: {mascota.raza}")
            print(f"Edad: {mascota.edad}")
            print(f"Edad: {mascota.edad}")
        print("=" * 40)



class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas =[]

    # Funciones de la clase
    def registrar_cita(self,cita):
        self.historial_citas.append(cita)
        print(f"Cita programada para  {self.nombre} el {cita.hora} a las {cita.hora}")

    def mostrar_historial(self):
        print(f"Historial de citas para {self.nombre}")
        for cita in self.historial_citas:
            print(f"-{cita.fecha} a las {cita.hora} : {cita.servicio} con {cita.veterinario}")


class Cita:
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario

class Servicio:
    def __init__(self, tipo, descripcion, costo):
        self.tipo = tipo
        self.descripcion = descripcion
        self.costo = costo
        
