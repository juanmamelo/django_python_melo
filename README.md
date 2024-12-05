Proyecto Django - Pasos Seguidos
A continuación, detallo los pasos que seguí para configurar y desarrollar el proyecto en Django:

1. Creación de la Carpeta del Proyecto
Primero, creé una carpeta para el proyecto y la abrí en VS Code.

2. Configuración del Archivo .gitignore
Generé un archivo .gitignore utilizando gitignore.io, seleccionando las opciones relevantes: VisualStudioCode, Python y Django. Guardé este archivo en la carpeta del proyecto.

3. Creación del Entorno Virtual
Configuré un entorno virtual con el comando:
    python -m venv <venv>
Luego, agregué el nombre del entorno virtual al archivo .gitignore.

4. Inicialización de Git
Inicié un repositorio de Git dentro del proyecto con el comando:
    git init
Hice el primer commit:
    git add .
    git commit -m "Inicio del proyecto"

5. Conexión con Repositorio Remoto
Conecté el repositorio local con un repositorio en la nube (en GitHub, por ejemplo), y realicé el primer push:
    git remote add origin <URL_del_repositorio>
    git branch -M main
    git push -u origin main

6. Activación del Entorno Virtual
Activé el entorno virtual:
    <venv>\Scripts\activate

7. Instalación de Django
Instalé Django con el manejador de paquetes pip:
    pip install django

8. Creación del Archivo requirements.txt
Generé el archivo requirements.txt para registrar las dependencias:
    pip freeze > requirements.txt

9. Creación del Proyecto Django
Inicié el proyecto en la carpeta actual con:
    django-admin startproject <nombre_proyecto>.

10. Prueba del Proyecto
Realicé las migraciones iniciales y ejecuté el servidor para verificar que el proyecto funcionaba:
    python manage.py migrate
    python manage.py runserver

11. Creación de la App Principal
Creé una app con el comando:
    python manage.py startapp <inicio>
La añadí en el archivo settings.py y creé un archivo urls.py dentro de la app. Luego, conecté las rutas con el archivo urls.py del proyecto principal usando:
    path('', include('<nombre_app>.urls')),

12. Configuración de Plantillas
Ajusté el archivo settings.py añadiendo:
    BASE_DIR / 'templates'
a la lista DIRS en la variable TEMPLATES. Después, creé una carpeta templates al nivel de las apps.

13. Creación del Superusuario
Generé un superusuario para acceder al panel de administración:
    python manage.py createsuperuser

14. Creación de Vistas y Rutas
Creé vistas en el archivo views.py, añadí sus rutas en el urls.py de la app correspondiente y diseñé los templates dentro de la carpeta templates. Además, conecté los templates a través de enlaces (<a>).

15. Modelos en Django
Creé modelos en models.py, heredando de models.Model y definiendo atributos con los tipos de campos (CharField, IntegerField, etc.).
Realicé migraciones:
    python manage.py makemigrations
    python manage.py migrate
Registré los modelos en el archivo admin.py.
Importé los modelos en views.py para usarlos en las vistas.

16. Creación de Formularios
Creé un archivo forms.py en la app correspondiente.
Definí formularios heredando de forms.Form, usando atributos como forms.CharField.
Importé los formularios en views.py para utilizarlos en las vistas.