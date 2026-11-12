# HelpDesk - Sistema de Gestión de Incidencias Técnicas

Proyecto del módulo MF0227_3 (Programación orientada a objetos). Núcleo funcional de un sistema de gestión de incidencias técnicas para una empresa simulada.

## Instalación y despliegue local

1. Crear el entorno virtual:

```
python -m venv venv
```

2. Activarlo (Windows con Git Bash):

```
source venv/Scripts/activate
```

En Windows con CMD o PowerShell: `venv\Scripts\activate`. En Mac o Linux: `source venv/bin/activate`.

3. Instalar las dependencias:

```
pip install -r requirements.txt
```

4. Aplicar las migraciones:

```
python manage.py migrate
```

5. Crear un usuario administrador (opcional, para entrar en `/admin/`):

```
python manage.py createsuperuser
```

6. Levantar el servidor:

```
python manage.py runserver
```

7. Abrir en el navegador:
- Lista de incidencias: http://127.0.0.1:8000/
- Nueva incidencia: http://127.0.0.1:8000/nueva/
- Panel de administración: http://127.0.0.1:8000/admin/

Para ejecutar las pruebas del Bloque 1 (POO):

```
python core_modelos.py
```

## Arquitectura del proyecto

```
helpdesk/
├── core_modelos.py
├── manage.py
├── requirements.txt
├── README.md
├── helpdesk_project/
└── incidencias/
    ├── models.py
    ├── admin.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
```

El proyecto se organiza según las tres unidades formativas:

- **UF2404 - Principios de POO**: `core_modelos.py` es un módulo independiente de Django. Define la clase base `TicketTecnico` (atributos protegidos, estados con transiciones validadas), las clases hijas `TicketHardware` y `TicketSoftware` (herencia), el método `calcular_sla()` sobrescrito (polimorfismo) y la excepción personalizada `EstadoInvalidoError`.
- **UF2405 - Programación web y bases de datos**: la app `incidencias` de Django lleva la misma idea de dominio a la web. Los modelos `Tecnico` e `Incidencia` (relacionados con `ForeignKey`) se guardan con el ORM, se gestionan desde el panel de administración, y se muestran con una `ListView` y una `CreateView` que usan plantillas con herencia (`base.html`) y Bootstrap.
- **UF2406 - Ciclo de vida del desarrollo**: el control de versiones con Git (ramas `main` y `desarrollo`, commits por fases), el archivo `requirements.txt` para reproducir el entorno y este `README.md` con el plan de pruebas.

## Plan de pruebas

| Nº | Caso de prueba | Pasos | Resultado esperado | Resultado obtenido |
|----|----------------|-------|--------------------|--------------------|
| 1 | Validación de campos vacíos en el formulario web | Abrir `/nueva/`, dejar todo vacío y pulsar Guardar | El formulario no se guarda y muestra errores de campo obligatorio | Correcto |
| 2 | Alta de una incidencia desde la web | Abrir `/nueva/`, rellenar todos los campos y pulsar Guardar | Redirección a la lista y la nueva incidencia aparece en ella | Correcto |
| 3 | Transición de estados en POO | Ejecutar `python core_modelos.py` | Pasar de Cerrado a En Proceso lanza `EstadoInvalidoError` controlado | Correcto |