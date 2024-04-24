# Odoo Class Project: Management System

## Installation Guide and Features

### Installation

- Once you download this repository, it is recommended not to name the module folder with "_" as it may cause issues.
- Place the folder in the Odoo addons directory.
- Update your app list and install the module.

### Features

- Create new users with two different roles: "Manager" and "Manager/Chief".
- The Manager Chief can access the Managers menu and edit managers. Managers can access the rest of the menus.
- In the Appointment menu, you can manage appointments; the end date will be automatically calculated once the start date is set.
- The Appointment menu includes a time slot validator (from 09:00 to 20:00 currently) and a validator to prevent scheduling an appointment for a manager at the same time as another.
- In the Consultancy menu, you can manage the prices and timings of each type of consultation from the "Types of Consultation" submenu.
- In the Calculator submenu, you can calculate the total price and time of various consultations.
- Both submenus offer the option to generate reports.
- In the Managers menu, you can edit managers (not end-users, just those you can select for your appointment).
- Clients is the menu to register and manage clients. It has Kanban, Tree, and Form views.

## Future Implementations

- Add colors to calendar cards.
- Improve the time slot logic, including a menu to enter the desired schedule.

---

# Proyecto de Clase en Odoo: Sistema de Gestión

## Guía de Instalación y Funcionalidades

### Instalación

- Una vez descargues este repositorio, se recomienda no nombrar la carpeta del módulo con "_" ya que puede ocasionar problemas.
- Introduce la carpeta en los addons de Odoo.
- Actualiza tu lista de aplicaciones e instálala.

### Funcionalidades

- Puedes crear nuevos usuarios con dos roles distintos: "Gestor" y "Gestor / Jefe".
- El Gestor Jefe puede acceder al menú de Gestores y editar los gestores. El Gestor puede acceder al resto de menús.
- En el menú Cita puedes gestionar citas, cuando pongas la fecha de inicio la final se calculará automáticamente.
- El menú Cita incluye un validador de franja horaria (de 09:00 a 20:00 actualmente) y un validador para que no se pueda poner una cita a un gestor al mismo tiempo.
- En el menú Consultoría puedes gestionar los precios y temporalización de cada tipo de consulta desde el submenú "Tipos de Consulta".
- En el submenú de Calculadora puedes calcular la suma del precio y tiempo total de diferentes consultas.
- Ambos submenús tienen la opción de generar informes.
- En el menú Gestores puedes editar los gestores (no son los usuarios finales, es simplemente los que puedes seleccionar para tu cita).
- Clientes es el menú para dar de alta y gestionar los clientes. Tiene vista Kanban, Tree y Form.

## Implementaciones Futuras

- Añadir colores a las tarjetas del calendario.
- Mejorar la lógica de la franja horaria, incluyendo un menú para introducir el horario deseado.
