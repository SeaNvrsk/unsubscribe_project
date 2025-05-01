# Sistema de Cancelación de Suscripción – Recovia

Este es un proyecto Django para gestionar cancelaciones de suscripción vía token único. Incluye:

- Importación de correos desde archivo Excel (.xlsx)
- Enlace de cancelación con token UUID
- Página web personalizada para el usuario
- Notificaciones por correo (Amazon SES)
- Vista de estadísticas en el panel de administración
- Diseño adaptado para dispositivos móviles
- Compatible con `.env` para proteger datos sensibles
- Registro de logs a archivo y vía email

---

## 🚀 Requisitos

- Python 3.11 o superior
- pip
- Virtualenv (opcional, pero recomendado)

---

## ⚙️ Instalación

```bash
git clone https://github.com/tu-usuario/unsubscribe_project.git
cd unsubscribe_project
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Configura variables de entorno

Crea un archivo `.env` en la raíz con este contenido:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-smtp-user
EMAIL_HOST_PASSWORD=tu-smtp-password
DEFAULT_FROM_EMAIL=notificaciones@recovia.solutions
```

Asegúrate de **no subir `.env` a GitHub**. Añade esta línea al `.gitignore`:

```
.env
```

---

## 🗄️ Migraciones y superusuario

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Ejecutar servidor

```bash
python manage.py runserver
```

---

## 📤 Subir Excel con emails

Accede al panel de administración en [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) y usa la opción para cargar correos desde archivo Excel.

---

## 📬 Enlace de cancelación

Los correos exportados contienen una URL de cancelación única como:

```
https://unsubscribe.recovia.solutions/unsubscribe/?token=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

---

## 📈 Estadísticas

Dentro del panel de administración se muestra:

- Número total de suscriptores
- Número de cancelaciones
- Gráfico circular con Chart.js

---

## 📦 Logs y notificaciones

- Todas las acciones se registran en `unsubscribe.log`
- Errores críticos se notifican por correo a `anatoliy.k@recovia.mx`
- Bajas se notifican a `reclamaciones@recovia.mx`

---

## ✅ Recomendaciones para producción

- Usar Gunicorn + Nginx
- Activar HTTPS con Let's Encrypt
- Configurar `DEBUG=False` y `ALLOWED_HOSTS`
- Usar supervisión del servicio (`systemd`)
- Mantener los logs en archivos rotativos

---

## 🧑‍💻 Autor

[Anatoliy Krasnikov] — [Seanvrsk]

© 2025 Recovia, S.A. de C.V.
