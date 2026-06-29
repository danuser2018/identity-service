# Registro de cambios

Todos los cambios notables de este proyecto se documentan en este fichero.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## Guía de uso

Cada versión se documenta bajo su número de versión y fecha de publicación.
Los cambios se agrupan en las siguientes categorías:

- **Añadido** — nuevas funcionalidades.
- **Cambiado** — cambios en funcionalidades existentes.
- **Obsoleto** — funcionalidades que serán eliminadas en versiones futuras.
- **Eliminado** — funcionalidades eliminadas en esta versión.
- **Corregido** — corrección de errores.
- **Seguridad** — correcciones de vulnerabilidades.

---

## Sin publicar

### Corregido

- Corregidas las discrepancias en `README.md` alineando los endpoints de identidad documentados y los ejemplos de comandos `curl` con el prefijo `/v1/` real de la implementación.
- Documentación de las variables de entorno de configuración de red (`PORT` y `HOST`) en la sección correspondiente del `README.md`.

## [1.1.0] - 2026-06-28

### Cambiado

- Versionado de los endpoints de identidad a `/v1/identity`, `/v1/identity/name` y `/v1/identity/email` de acuerdo con ADR-004.

### Añadido


- Nueva carpeta `.agent/skills` con información relevante para la IA.

## [1.0.0] - 2026-06-28

### Añadido

- Integración continua mediante GitHub Actions (`.github/workflows/test.yml`) para ejecutar las pruebas en cada push y pull request al tronco principal.
- Implementación de la versión MVP del microservicio `identity-service` en Python usando FastAPI.
- Configuración externa de la identidad del usuario mediante variables de entorno `USER_NAME` y `USER_EMAIL` utilizando `pydantic-settings`.
- Abstracción de persistencia mediante patrón Repositorio y Servicio desacoplados.
- Endpoints REST de la API: `GET /identity`, `GET /identity/name`, `GET /identity/email` y `GET /health`.
- Dockerización mediante `Dockerfile` y configuración con `docker-compose.yml`.
- Conjunto de pruebas unitarias y de integración bajo la carpeta `tests/`.
- Fichero `CONTRIBUTING.md` con el flujo de trabajo Trunk Based Development,
  convenciones de commits, guía de Pull Requests y buenas prácticas para
  desarrollo asistido con IA.
- Fichero `CHANGELOG.md` con el formato Keep a Changelog v1.1.0 en castellano.
- Fichero `README.md` con la descripción del proyecto.

---

<!-- Plantilla para nuevas versiones:

## [X.Y.Z] - AAAA-MM-DD

### Añadido
-

### Cambiado
-

### Obsoleto
-

### Eliminado
-

### Corregido
-

### Seguridad
-

-->

[Sin publicar]: https://github.com/danuser2018/tts-capability/compare/HEAD...HEAD
