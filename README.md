# 🚫NoStore Website

Una plataforma de comercio electrónico robusta y escalable construida con Django, diseñada para ofrecer una experiencia de compra fluida y segura.

-----

## 🔥Tabla de Contenidos

  * Acerca del Proyecto
  * Características Destacadas
  * Tecnologías Utilizadas
  * Requisitos Previos
  * Instalación Local
  * Uso
  * Estructura del Proyecto
  * Despliegue
  * Contribuir
  * Licencia
  * Contacto
  * Agradecimientos

-----

## ℹ️Acerca del Proyecto

Este proyecto es una solución de **eCommerce completa** que permite la gestión de productos, carritos de compra, procesos de pago y pedidos. Su objetivo es proporcionar una base sólida para cualquier negocio que desee vender productos en línea, ofreciendo una experiencia de usuario intuitiva y una gestión administrativa eficiente.

### ✅¿Qué problema resuelve?

Facilita la creación y gestión de una tienda en línea, desde la visualización de productos hasta la finalización de la compra, con un enfoque en la seguridad y la escalabilidad.

-----

## 🎇Características Destacadas

  * **Catálogo de Productos:** Navegación por categorías, búsqueda de productos, detalles de producto con imágenes y descripciones.
  * **Carrito de Compras:** Añadir, eliminar y actualizar cantidades de productos en el carrito.
  * **Autenticación de Usuarios:** Registro, inicio de sesión y gestión de perfiles de usuario.
  * **Proceso de Pago Seguro:** Integración con pasarelas de pago (ej. Stripe) para transacciones seguras.
  * **Gestión de Pedidos:** Historial de pedidos para usuarios, gestión de estado de pedidos para administradores.
  * **Panel de Administración:** Interfaz de Django Admin personalizada para la gestión de productos, pedidos, usuarios, etc.
  * **Sistema de Descuentos/Cupones:** Aplicación de códigos de descuento en el carrito.
  * **Reviews y Calificaciones de Productos:** Permite a los usuarios dejar comentarios y calificaciones.
  * **Diseño Responsivo:** Adaptable a diferentes dispositivos (móviles, tablets, escritorio).

-----

## 🔥Tecnologías Utilizadas

  * **Backend:**
      * **Django:** El framework web principal para el desarrollo rápido y seguro.
      * **Python:** Lenguaje de programación.
      * **Django REST Framework (DRF):** Para construir la API RESTful (si aplica).
      * **Base de Datos:** PostgreSQL (recomendado para producción), SQLite (para desarrollo).
      * **Stripe Python Library:** Para la integración de pagos.
      * **Celery:** Para tareas asíncronas (ej. envío de correos, procesamiento de pagos).
      * **Redis:** Como broker para Celery y caché.
  * **Frontend:**
      * HTML5, CSS3 con Tailwind.
      * JavaScript.
  * **Herramientas de Desarrollo y Despliegue:**
      * **Git:** Control de versiones.
      * **Docker / Docker Compose:** Para un entorno de desarrollo consistente y despliegue.
      * **Gunicorn / Nginx:** Servidor WSGI y servidor web para producción.

-----

## 💻Requisitos Previos

Asegúrate de tener instalado lo siguiente:

  * **Python 3.9+**
  * **pip** (gestor de paquetes de Python)
  * **Git**
  * **Docker y Docker Compose**
  * **PostgreSQL** 

-----

## 🛠️Instalación Local

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/plzchristianot/NOStoreApp.git
    cd nombre-de-tu-e-commerce
    ```

2.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz del proyecto (junto a `manage.py`) y configura las siguientes variables. **Nunca subas este archivo al control de versiones.**

    ```ini
    # .env
    HOST_DB = mydatabase.cluster-c1a2b3d4e5.us-east-1.rds.amazonaws.com
    USER_DB = db_username
    PASSWORD_DB = password_test
    DB_NAME = db_name_test
    PORT_DB = 0000
    ```

3.  **Configuración:**

    a.  **Crear y activar un entorno virtual:**
    ` bash python -m venv venv # Windows .\venv\Scripts\activate # macOS/Linux source venv/bin/activate  `

    b.  **Instalar dependencias:**
    ` bash pip install -r requirements.txt  `

    c.  **Ejecutar migraciones:**
    ` bash python manage.py migrate  `

    d.  **Recolectar archivos estáticos:**
    ` bash python manage.py collectstatic  `

    e.  **Crear un superusuario (opcional, para acceder al admin de Django):**
    ` bash python manage.py createsuperuser  `

    f.  **Iniciar el servidor de desarrollo:**
    ` bash python manage.py runserver  `
    Ahora puedes acceder a la aplicación en `http://127.0.0.1:8000/`.

-----

## Uso

Una vez que el servidor está en funcionamiento:

  * **Página Principal:** `http://127.0.0.1:8000/`
  * **Panel de Administración:** `http://127.0.0.1:8000/admin/` (accede con las credenciales de superusuario)
  * **Registro de Usuario:** `http://127.0.0.1:8000/accounts/signup/`
  * **Página de Productos:** `http://127.0.0.1:8000/products/` (o la URL de tu catálogo)
  * **Carrito de Compras:** `http://127.0.0.1:8000/cart/`
  * **Proceso de Pago:** Dirigido desde el carrito.

-----

## Estructura del Proyecto

Una visión general de la organización de los archivos principales:

```
ecommerce/
├── .env
├── .gitignore
├── package.json
├── package-lock.json
├── requirements.txt
├── .vscode/
├── .venv/
├── node_modules/
├── core/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── templates/
│   ├── static/
│   ├── utils/
│   ├── shopapp/
│   ├── nostore/             #App matriz
│   ├── loginapp/
│   └── deliveryapp/

```

-----

## 🚀Despliegue

Este proyecto está diseñado para ser desplegado en entornos de producción utilizando **Docker Compose** o servicios de contenedores como **Heroku, AWS ECS, Google Cloud Run**.

**Pasos generales para un despliegue en la nube (ej. con Docker):**

1.  Asegúrate de que tus variables sensibles estén configuradas de forma segura como **variables de entorno** en tu proveedor de hosting.
2.  Configura tu base de datos de producción (ej. AWS RDS PostgreSQL).
3.  Asegúrate de que `DEBUG=False` y `ALLOWED_HOSTS` incluya tu dominio de producción.
4.  Configura un servidor web (Nginx) para servir archivos estáticos/media y un servidor WSGI (Gunicorn) para tu aplicación Django.
5.  Configura un servicio de caché (Redis) y un broker de tareas (Celery).

Para instrucciones más detalladas, consulta la documentación específica de tu proveedor de hosting.

-----

## 🤝Contribuir

¡Las contribuciones son bienvenidas\! Si deseas mejorar este proyecto, sigue estos pasos:

1.  Haz un **"fork"** de este repositorio.
2.  Crea una nueva rama para tu característica o corrección de bug:
    ```bash
    git checkout -b feature/nueva-caracteristica
    # o
    git checkout -b fix/solucion-de-bug
    ```
3.  Realiza tus cambios y asegúrate de que pasen las pruebas (si las hay).
4.  Realiza un "commit" con un mensaje claro y descriptivo:
    ```bash
    git commit -m 'feat: Añade integración con PayPal'
    ```
5.  Haz "push" a tu rama:
    ```bash
    git push origin feature/nueva-caracteristica
    ```
6.  Abre un **Pull Request (PR)** explicando tus cambios.

Por favor, asegúrate de que tu código siga los estándares de calidad (PEP 8) y que tus commits sean atómicos.

-----

## 📄Licencia

Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` en la raíz del repositorio para más detalles.

-----

## 📧Contacto

  * **Tu Nombre/Organización** - [oviedotorreschristian@gmail.com](mailto:oviedotorreschristian@gmail.com)
  * **GitHub:** [https://github.com/plzchristianot](https://github.com/plzchristianot)
  * **LinkedIn:** [https://www.linkedin.com/in/plzchristianot/](https://www.linkedin.com/in/plzchristianot/)

-----

## 🙏Agradecimientos

  * A la comunidad de **Django** por el increíble framework.
  * A todos los contribuidores y testers que han ayudado a mejorar este proyecto.

-----

**Consejos Adicionales:**

  * **Capturas de Pantalla/GIFs:** Si puedes, añade algunas capturas de pantalla de tu tienda funcionando, o un GIF corto mostrando el flujo de compra. Esto es muy atractivo visualmente.
  * **Tests:** Si tienes pruebas, puedes añadir una sección de "Tests" explicando cómo ejecutarlas (`python manage.py test`).
  * **Prerrequisitos específicos:** Si tu proyecto usa algo muy particular (ej. un servicio externo específico), menciónalo claramente.

¡Espero que esta plantilla te sea muy útil para tu proyecto de eCommerce\!
