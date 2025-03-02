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
        super(). __init__(nombre, contacto, direccion)
        self.mascotas =[]


    # Funciones de la clase
    def registrar_mascota(self,mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {mascota.nombre} registrada exitosamente")


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

# Lista global para almacenar los clientes
clientes = []


# Funciones auxiliares
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar cliente")
    print("2. Registrar mascota")
    print("3. Programar cita")
    print("4. Consultar historial de servicios")
    print("5. Mostrar información de clientes")
    print("6. Salir")
    return input("Seleccione una opción: ")

def registrar_cliente():
    nombre =  input("Ingrese el nombre del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    direccion = input("Ingrese la dirección dl cliente: ")
    cliente = Cliente(nombre, contacto, direccion)
    clientes.append(cliente)
    print(f"Cliente {nombre} registrado exitosamente")

def buscar_cliente(nombre):
    for cliente in clientes:
        if cliente.nombre.lower() == nombre.lower():
            return cliente
        return None

def registrar_mascota():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = buscar_cliente(nombre_cliente)
    if cliente:
        nombre =input("Ingrese el nombre de la mascota: ")
        especie = input("Ingrese la especie de la mascota: ")
        raza = input("Ingrese la raza de la mascota: ")
        edad = input("Ingrese la edad de la mascota: ")
        mascota = Mascota(nombre, especie, raza, edad)
        cliente.registrar_mascota(mascota)
    else:
        print(f"No se encontró el cliente con el nombre {nombre_cliente}")

def registrar_cita():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = buscar_cliente(nombre_cliente)
    if cliente:
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        mascota = next((m for m in cliente.mascotas if m.nombre.lower() == nombre_mascota.lower()))
        if mascota:
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ")
            hora = input("Ingrese la hora de la cita (HH:MM): ")
            servicio = input("Ingrese el servicio (consulta, vacunación, etc.): ")
            veterinario = input("Ingrese el nombre del veterinario: ")
            cita = Cita(fecha, hora, servicio, veterinario)
            mascota.registrar_cita(cita)
        else:
            print(f"La mascota con el nombre {nombre_mascota} no se encuentra registrada")
    else:
        print(f"El cliente con el nombre {nombre_cliente} no se encuentra registrado")


def consultar_historial():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = buscar_cliente(nombre_cliente)
    if cliente:
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        mascota = next((m for m in cliente.mascotas if m.nombre.lower()== nombre_mascota.lower()))
        if mascota:
            mascota.mostrar_historial()
        else:
            print(f"El  nombre de la mascota {nombre_mascota} no se encuentra registrado")
    else:
        print(f"El nombre del cliente {nombre_cliente} no se encuentra registrado")


def mostrar_clientes():
    if clientes:
        for cliente in clientes:
            cliente.mostrar_info()
    else:
        print(f"No se encuentran clientes registrados")


def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            registrar_mascota()
        elif opcion == "3":
            registrar_cita()
        elif opcion == "4":
            consultar_historial()
        elif opcion == "5":
            mostrar_clientes()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Gracias por usar Huella Feliz!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()