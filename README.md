# Sistema de Gestión de Alquiler de Vehículos

## Descripción

Este proyecto consiste en el desarrollo de un sistema de gestión para una empresa de alquiler de vehículos. Permite administrar sedes, vehículos y trabajadores mediante una estructura basada en programación orientada a objetos en Python. El proyecto esta orientado para el enfoque de la empresa, es decir que no tengan acceso directo los cllientes 

## Funcionalidades

* Gestión de sedes:

  * Añadir sedes
  * Buscar sedes por ID o nombre
  * A

* Gestión de trabajadores:

  * Alta y baja de trabajadores
  * Asignación de trabajadores a sedes

* Gestión de vehículos:

  * Registro de vehículos
  * Asociación de vehículos a sedes
  * Control básico de disponibilidad

## Estructura del proyecto

```
proyecto/
│
├── Entidades/
│   ├── vehiculo.py
│   ├── coche.py
│   ├── sede.py
│   ├── trabajador.py
│
├── Servicios/
│   ├── GestionSede.py
│   ├── GestionTrabajador.py
│
├── main.py
└── README.md
```

## Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos

## Ejecución

1. Clonar el repositorio:

```
git clone https://github.com/tuusuario/turepo.git
```

2. Acceder al directorio:

```
cd turepo
```

3. Ejecutar el programa:

```
python main.py
```

## Autor

Antonio Ferrández Rodríguez

## Notas

Proyecto desarrollado con fines educativos.
