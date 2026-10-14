<h1 align="center">Cálculo de Comisiones de Ventas: Patrón MVC con Python y Flask</h1>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-COMPLETADO-green?style=for-the-badge" alt="Estado">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Bootstrap%205-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render">
  <img src="https://img.shields.io/badge/Arquitectura-MVC-0560de?style=for-the-badge" alt="MVC">
</p>

---

## 📑 Índice

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Estado del Proyecto](#-estado-del-proyecto)
- [Características](#️-características)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [Acceso y Ejecución](#-acceso-y-ejecución)
- [Desarrollador](#-desarrollador)

---

## 📖 Descripción del Proyecto

Aplicación web desarrollada como resolución a la **Tarea 4: Aplicación Ejercicio MVC** (basada en los videos y repositorios de alumnos de semestres anteriores). El objetivo principal fue construir un sistema de **cálculo de comisiones de ventas** aplicando estrictamente el patrón de diseño **Modelo-Vista-Controlador (MVC)**.

La aplicación procesa rangos de fechas dinámicos, calcula bonificaciones según reglas de negocio predefinidas y se encuentra **desplegada públicamente en la nube** mediante la plataforma **Render**.

---

## 🚦 Estado del Proyecto

<h4 align="center">
  ✅ Proyecto Finalizado, Funcional y Desplegado en la Nube ✅
</h4>

---

## ⚙️ Características

- 🧱 **Patrón MVC estricto:** separación clara entre la lógica de acceso a datos (SQLAlchemy), el enrutamiento y procesamiento (Flask) y la interfaz de usuario (HTML/Jinja2).
- 📅 **Filtro dinámico de fechas:** validación en el frontend (JavaScript) y en el backend (Python) para evitar fechas incoherentes o futuras, limitando la consulta hasta la fecha actual del sistema.
- 📊 **Cálculo automático:** motor de reglas que evalúa el total facturado por vendedor y asigna automáticamente un porcentaje de comisión (5%, 10%, 15% o 18%).
- 🗄️ **Autogeneración de datos:** creación automática de la base de datos local y registro de datos de demostración (ventas de mayo a octubre de 2026) al arrancar el servidor.
- 📱 **Interfaz UI/UX:** diseño limpio y responsivo impulsado por Bootstrap 5.
- ☁️ **Desplegado en producción:** servido con Gunicorn sobre Render.

---

## 📂 Estructura del Proyecto

```text
Ejercicio-MVC-Python-Flask/
├── app.py                         # Archivo principal: Modelos de BD, Controlador y Rutas
├── requirements.txt               # Dependencias del proyecto (Flask, SQLAlchemy, Gunicorn)
├── README.md                      # Documentación del proyecto
└── template/                      # Capa de Vistas
    ├── formulario_busqueda.html   # Interfaz de ingreso de fechas
    └── comision.html              # Interfaz de reporte y resultados
```

---

## 📐 Arquitectura MVC

| Capa del Patrón MVC          | Implementación en el Proyecto                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modelo (Model)**           | Clases `Vendedor` y `Factura` construidas con Flask-SQLAlchemy. Gestionan la conexión a SQLite y las consultas transaccionales (`db.session.query`).                   |
| **Vista (View)**             | Archivos dentro de la carpeta `/template`. Utilizan el motor Jinja2 para recibir variables desde el servidor y renderizar los resultados en tablas HTML5.              |
| **Controlador (Controller)** | Funciones decoradas con `@app.route` en `app.py`. Reciben las peticiones GET/POST, ejecutan la lógica de negocio (`calcular_comision()`) y deciden qué vista retornar. |

**Flujo de la aplicación:**

```text
Usuario → Formulario (Vista) → Ruta Flask (Controlador) → Consulta a BD (Modelo)
                                        ↓
                       calcular_comision() aplica reglas
                                        ↓
                    Reporte de comisiones (Vista Jinja2) → Usuario
```

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** [Python 3](https://www.python.org/) y [Flask](https://flask.palletsprojects.com/)
- **Base de Datos:** [SQLite](https://www.sqlite.org/) a través de [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
- **Frontend:** [HTML5](https://developer.mozilla.org/es/docs/Web/HTML), [CSS3](https://developer.mozilla.org/es/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript) y [Bootstrap 5](https://getbootstrap.com/)
- **Despliegue y Hosting:** [Render](https://render.com/) y servidor WSGI [Gunicorn](https://gunicorn.org/)
- **Control de Versiones:** [Git](https://git-scm.com/) y [GitHub](https://github.com/)

---

## 🚀 Acceso y Ejecución

### 1. Ejecución Local (Desarrollo)

**Clonar el repositorio y entrar al directorio:**

```bash
git clone https://github.com/ArielGitHuub/Ejercicio-MVC-Python-Flask.git
cd Ejercicio-MVC-Python-Flask
```

**Instalar las dependencias e iniciar el servidor:**

```bash
pip install -r requirements.txt
python app.py
```

El proyecto estará disponible en el navegador en: [http://localhost:50002](http://localhost:50002)

### 2. Despliegue en la Nube (Producción)

El proyecto se encuentra alojado y funcionando públicamente en **Render**.

- 🌐 **Enlace de la aplicación:** _(https://ejercicio-mvc-python-flask.onrender.com/)_
- 🎥 **Video explicativo de la tarea:** _(Inserta aquí tu link de YouTube/Loom)_

---

## 👤 Desarrollador

**Ariel Tejada**  
Estudiante de Ingeniería de Software — UDLA
