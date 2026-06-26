# CRM PRO - Sistema de Gestión Premium ⚡

Sistema CRM (Customer Relationship Management) desarrollado en Django aplicando estrictamente el paradigma de Programación Orientada a Objetos (POO), estructurado con lógica limpia, segura y profesional.

## 🚀 Módulos y Funcionalidades del Sistema

1. **Autenticación y Roles**: Sistema de login y registro que asigna dinámicamente roles ("Administrador" y "Usuario") usando el sistema de Grupos de Django.
2. **CRUD Completo**: Permite crear, leer, actualizar y eliminar registros de clientes de forma segura. La modificación y eliminación están protegidas y exclusivas para Administradores.
3. **Menú SPA (Single Page Application)**: Navegación fluida y dinámica impulsada por Fetch API (Vanilla JS) que evita las recargas completas de página, ofreciendo una experiencia moderna.
4. **Sistema de Alertas**: Mensajes tipo "toast" elegantes e informativos que retroalimentan las acciones del usuario.

## 🎨 Interfaz y Recursos

- **Diseño Premium**: Interfaz moderna "Cosmic Noir" con elementos Glassmorphism, animaciones sutiles y paleta de colores vibrantes.
- **Bootstrap Local**: Integración interna de la librería Bootstrap, sin dependencia de CDNs externas.

## 🛡️ Seguridad (4 Capas Implementadas)

El sistema integra las 4 capas de seguridad solicitadas:
1. **Validación Frontend**: Atributos `pattern` de HTML5 y `required` generados por Django Forms.
2. **Validación Backend (Regex)**: `RegexValidator` de Django para controlar estrictamente nombres, teléfonos y códigos postales.
3. **Restricción de Caracteres**: Limitación rigurosa de caracteres en campos clave (usuario y contraseñas) para prevenir inyecciones.
4. **Autorización Basada en Roles**: Control de acceso a vistas y funciones en las plantillas según los permisos del usuario activo.
*(Adicionalmente, se cuenta con la protección CSRF de Django por defecto contra ataques cross-site).*

## 🧩 Patrones de Diseño Identificados

1. **MVC / MVT (Model-View-Template)**: Patrón estructural nativo de Django para separar los datos (Modelos), la lógica (Vistas) y la presentación (Plantillas).
2. **Active Record**: Implementado a través del ORM de Django (cada objeto de la base de datos es una instancia del Modelo `Record`).
3. **Factory / Builder (a través de ModelForm)**: Se usa `UserRegisterForm` y `RecordForm` que actúan como fábricas construyendo formularios validados y complejos automáticamente basándose en los modelos (Principio DRY).

## 🎨 Patrones de Diseño Implementados

Los patrones listados previamente fueron aplicados en el proyecto:

- **MVC / MVT** – usado por Django para separar modelo, vista y plantilla.
- **Active Record** – mediante el ORM de Django.
- **Factory / Builder** – usando `ModelForm` para crear formularios validados.


## 📊 Arquitectura y Modelado (PlantUML)

Los planos de la arquitectura del microproyecto (del C1 al C4) se encuentran en la carpeta `docs/arquitectura_uml.puml`.

---

## 📋 Implementación según lista de chequeo

A continuación se enlistan los requisitos solicitados y el archivo donde se encuentra la implementación.

| # | Requisito | Archivo(s) | Comentario |
|---|-----------|------------|------------|
| 1 | Login con roles (usuario vs admin) | `dcrm/website/views.py` (login view) y `dcrm/website/templates/home.html` | Autenticación con Django y redirección según grupo |
| 2 | CRUD completo de registros | `dcrm/website/views.py` (add_record, update_record, delete_record) y `dcrm/website/templates/*.html` | Operaciones CRUD |
| 3 | Mostrar solo los componentes del usuario | `dcrm/componentes/views.py` (mis_componentes filter) y `dcrm/componentes/templates/componentes_list.html` | Filtro por usuario |
| 4 | Estrellas de fondo más visibles | `dcrm/website/templates/base.html` (CSS de `.particle`) | Brillo mejorado |
| 5 | Validaciones de formularios (sin números en apellidos, solo números en teléfono, etc.) | `dcrm/website/forms.py` (RegexValidator, patrones) | Mensajes en español |
| 6 | Teléfono exacto 10 dígitos | `dcrm/website/forms.py` (`phone_regex = RegexValidator(r'^\d{10}$', ...)`) | Mensaje: “Solo se permiten números y deben ser exactamente 10 números.” |
| 7 | Notificaciones visuales de errores en registro | `dcrm/website/templates/register.html` (alert‑warning y mensajes inline) | Mensajes claros en rojo |
| 8 | Mensajes de commit en español | `make_commits.py` (lista `commits` traducida) | Historias de git en español |
| 9 | Asignación de roles “Usuario” y “Administrador” | `dcrm/website/models.py` (campo `is_staff`/`is_superuser`) y manejo en vistas | Diferenciación de paneles |
|10| Documentación del proyecto (README actualizado) | `README.md` (esta sección) | Resumen de implementaciones |

*Desarrollado para la entrega final del módulo.*
