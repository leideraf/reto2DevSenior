# Proyecto Huella Feliz - Sistema de Gestión Veterinaria

## 📌 Descripción General

**Huella Feliz** es un sistema de gestión para clínicas veterinarias desarrollado en **Python**. Permite administrar información de clientes, sus mascotas, programar citas veterinarias y mantener un registro del historial de servicios. 

El sistema opera mediante una **interfaz de línea de comandos** con un menú interactivo que facilita la navegación entre sus funcionalidades.

---

## ⚙️ Funcionamiento

El programa implementa un flujo de trabajo típico de una clínica veterinaria:

- 📌 **Registro de clientes** en el sistema.
- 🐾 **Asociación de mascotas** a los clientes registrados.
- 📅 **Programación de citas** veterinarias para las mascotas.
- 📜 **Consulta del historial** de servicios por mascota.
- 🔍 **Visualización de información** de clientes y sus mascotas.

---

## 🏗️ Estructura de Clases

El sistema sigue los principios de la **Programación Orientada a Objetos (POO)**, con las siguientes clases principales:

### 📌 Clase `Persona`
- **Función:** Clase base que almacena información básica de contacto.
- **Atributos:**
  - `nombre`: Nombre de la persona.
  - `contacto`: Información de contacto (teléfono, email).
  - `direccion`: Dirección física.

### 📌 Clase `Cliente` _(hereda de `Persona`)_
- **Función:** Representa a los clientes de la clínica.
- **Atributos adicionales:**
  - `mascotas`: Lista de objetos `Mascota` asociados al cliente.
- **Métodos:**
  - `registrar_mascota(mascota)`: Añade una mascota a la lista del cliente.
  - `mostrar_info()`: Muestra la información del cliente y sus mascotas.

### 📌 Clase `Mascota`
- **Función:** Almacena la información de las mascotas de los clientes.
- **Atributos:**
  - `nombre`: Nombre de la mascota.
  - `especie`: Tipo de animal (perro, gato, etc.).
  - `raza`: Raza específica de la mascota.
  - `edad`: Edad de la mascota.
  - `historial_citas`: Lista de objetos `Cita` asociados a la mascota.
- **Métodos:**
  - `registrar_cita(cita)`: Añade una cita al historial.
  - `mostrar_historial()`: Muestra todas las citas registradas.

### 📌 Clase `Cita`
- **Función:** Representa una cita médica programada.
- **Atributos:**
  - `fecha`: Fecha de la cita.
  - `hora`: Hora de la cita.
  - `servicio`: Tipo de servicio (consulta, vacunación, etc.).
  - `veterinario`: Nombre del veterinario asignado.

### 📌 Clase `Servicio`
- **Función:** Define los diferentes servicios que ofrece la clínica.
- **Atributos:**
  - `tipo`: Categoría del servicio.
  - `descripcion`: Descripción detallada.
  - `costo`: Precio del servicio.

---

## 🛠️ Funciones Principales

### 🔹 Funciones de Gestión de Clientes
- `mostrar_menu()`: Muestra las opciones disponibles y captura la selección del usuario.
- `registrar_cliente()`: Captura los datos para crear un nuevo cliente.
- `buscar_cliente(nombre)`: Localiza un cliente por su nombre (insensible a mayúsculas/minúsculas).
- `mostrar_clientes()`: Muestra información de todos los clientes registrados.

### 🔹 Funciones de Gestión de Mascotas
- `registrar_mascota()`: Asocia una nueva mascota a un cliente existente.

### 🔹 Funciones de Gestión de Citas
- `registrar_cita()`: Programa una nueva cita para una mascota específica.
- `consultar_historial()`: Muestra el historial de citas de una mascota.

### 🔹 Función Principal
- `main()`: Implementa el bucle principal del programa y maneja la lógica de navegación del menú.

---

📌 **Autor:** [Tu Nombre]  
📌 **Tecnologías utilizadas:** Python  
📌 **Licencia:** MIT  

