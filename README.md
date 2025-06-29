
# 🌐 Proyecto Django – Aplicación Web Completa

Este repositorio documenta paso a paso el desarrollo de una aplicación web construida con **Django**, abarcando desde la configuración inicial hasta la implementación de funcionalidades avanzadas como mensajería entre usuarios y optimización de la interfaz.

---

## 🛠️ Pasos Seguidos

### 1. Creación del entorno de desarrollo
- Se creó una carpeta del proyecto y se abrió en Visual Studio Code.
- Se generó un archivo `.gitignore` usando [gitignore.io](https://gitignore.io) incluyendo: VisualStudioCode, Python y Django.
- Se configuró un entorno virtual con `python -m venv`, y se añadió al `.gitignore`.

### 2. Inicialización de Git y conexión con GitHub
```bash
git init
git add .
git commit -m "Inicio del proyecto"
git remote add origin <URL_del_repositorio>
git branch -M main
git push -u origin main
```

### 3. Instalación de Django y configuración del proyecto
- Se activó el entorno virtual: `\Scripts\activate`
- Se instaló Django: `pip install django`
- Se generó el archivo de dependencias: `pip freeze > requirements.txt`
- Se inició el proyecto: `django-admin startproject <nombre_proyecto>`
- Se aplicaron migraciones iniciales y se ejecutó el servidor.

### 4. Creación y configuración de apps
- Se creó una app con `python manage.py startapp <nombre_app>`
- Se registró en `settings.py` y se configuró el enrutamiento con `include()`.
- Se creó una carpeta `templates/` y se configuró en TEMPLATES['DIRS'].

### 5. Panel de administración
- Se generó un superusuario: `python manage.py createsuperuser`

### 6. Vistas, URLs y Templates
- Se implementaron vistas en `views.py`
- Se crearon rutas en `urls.py`
- Se diseñaron templates HTML con enlaces dinámicos

### 7. Modelos en Django
- Se definieron modelos en `models.py` con campos como `CharField`, `IntegerField`, etc.
- Se realizaron migraciones y se registraron los modelos en `admin.py`

### 8. Formularios personalizados
- Se creó `forms.py` y se definieron formularios con `forms.Form`
- Se utilizaron en las vistas importando los formularios correspondientes

---

## 👥 Funcionalidades avanzadas

### ✅ App para manejo de usuarios
- Se implementaron vistas basadas en clases (CBV) para gestionar operaciones CRUD.

### ✅ App de chat entre usuarios
- Mensajería privada en tiempo real entre usuarios.

### ✅ UI mejorada con Bootstrap
- Formularios y vistas estilizadas para una mejor experiencia de usuario.

### ✅ Seguridad y variables de entorno
- Se implementó `python-dotenv` para ocultar la `SECRET_KEY` y mejorar la seguridad.

---

## 🧑‍💻 Autor

Juan Manuel Melo  
🔗 [LinkedIn](https://www.linkedin.com/in/juan-manuel-melo95/)  
📧 juanmanuelmelo95@gmail.com

---

## 📄 Licencia

MIT License – ver archivo `LICENSE` para más detalles.
