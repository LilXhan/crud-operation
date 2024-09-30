# CRUD en Django con SQL Server

> Atendiendo el reto Code Challenge, se desarrolla una aplicación en Django que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) siguiendo buenas prácticas de diseño y codificación, como los principios SOLID y el uso adecuado de SQL Server.

## Para usar este repositorio

Este proyecto contiene tanto el código fuente como las configuraciones necesarias para ejecutar una aplicación Django con SQL Server. La base de datos utilizada es SQL Server, y se incluye la configuración para conectarse a ella utilizando el paquete `django-mssql-backend`.

Se ha desarrollado un CRUD básico para gestionar una entidad dentro de la aplicación, aplicando buenas prácticas de Django y utilizando SQL Server como base de datos.

Todas las dependencias están descritas en el fichero `requirements.txt`.

El puerto por defecto es el 8000 para evitar posibles conflictos.

### Requisitos previos

- Python 3.8 o superior
- SQL Server (local o remoto)
- Navegador web
- Opcional: git, IDE de desarrollo

### Probar la aplicación mediante la interfaz web

1. Descargar como zip o clonar el repositorio usando git o cualquier asistente gráfico. Una vez descargado, puede optar por ejecutar el entorno virtual o abrir el proyecto en su IDE favorito.

2. Descomprimir el paquete descargado.

3. Crear y activar un entorno virtual con los siguientes comandos:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

4. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

5. Configurar la conexión a la base de datos SQL Server en el archivo `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'mssql',
           'NAME': 'nombre_base_datos',
           'USER': 'usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': '1433',
           'OPTIONS': {
               'driver': 'ODBC Driver 17 for SQL Server',
           },
       }
   }
   ```

6. Ejecutar las migraciones para crear las tablas necesarias en SQL Server:
   ```bash
   python manage.py migrate
   ```

7. Para ejecutar el servidor de desarrollo, usar el siguiente comando:
   ```bash
   python manage.py runserver
   ```

8. Verificar que ha iniciado correctamente. Si tiene problemas, validar que la conexión a SQL Server está configurada correctamente y que las migraciones se ejecutaron sin errores.

9. Para ver y probar el CRUD mediante la interfaz web, navegue a la siguiente URL en su navegador web:
   ```
   http://localhost:8000/payrollapp/employees-list
   ```
   Aquí podrá gestionar las operaciones de crear, leer, actualizar y eliminar datos de la entidad definida en el modelo.

---
