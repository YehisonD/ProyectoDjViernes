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

## 📊 Arquitectura y Modelado (PlantUML)

Los planos de la arquitectura del microproyecto (del C1 al C4) se encuentran en la carpeta `docs/arquitectura_uml.puml`.

---
*Desarrollado para la entrega final del módulo.*
