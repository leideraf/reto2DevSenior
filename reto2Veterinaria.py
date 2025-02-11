# Importamos la libreria datetime para trabajar con fechas
import datetime

# Creamos las clases con las que trabajarempos en este proyecto

class Persona:
    def __init__(self, nombre,contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super(). __init__(self, nombre, contacto, direccion)
        self.mascotas =[]

class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas =[]

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
        
