# Identity Service

## Descripción

**Identity Service** es el servicio responsable de almacenar y proporcionar la información privada del usuario dentro de Nova.

Su única responsabilidad es actuar como proveedor de datos personales para el resto de la plataforma. Los consumidores nunca acceden directamente al mecanismo de almacenamiento; toda interacción se realiza mediante una API REST.

En esta primera versión (MVP) los datos se almacenan mediante variables de entorno para simplificar el despliegue y facilitar el desarrollo. En versiones posteriores el backend podrá sustituirse por una base de datos o un gestor de secretos sin modificar la interfaz pública del servicio.

---

# Objetivos

* Centralizar toda la información privada del usuario.
* Exponer una API REST sencilla y estable.
* Desacoplar el almacenamiento de datos del resto de la plataforma.
* Facilitar la evolución futura del sistema.
* Mantener una única fuente de verdad (Single Source of Truth) para la identidad del usuario.

---

# Estado del proyecto

Versión actual: **MVP**

Características implementadas:

* Servicio REST.
* Lectura de datos desde variables de entorno.
* Consulta del nombre del usuario.
* Consulta del correo electrónico.
* Consulta de la identidad completa.
* Dockerización.

Características previstas para versiones futuras:

* Persistencia mediante SQLite.
* Persistencia mediante PostgreSQL.
* Integración con un gestor de secretos.
* Control de acceso mediante tokens.
* Usuarios múltiples.
* Actualización dinámica de datos.

---

# Responsabilidades

Identity Service **debe**:

* almacenar la información del usuario;
* proporcionar dicha información mediante una API REST;
* ocultar el mecanismo de almacenamiento al resto del sistema.

Identity Service **no debe**:

* autenticar usuarios;
* emitir tokens;
* gestionar permisos;
* enviar correos;
* contener lógica de negocio;
* conocer qué plugins consumen la información.

---

# Arquitectura

```
                 +----------------------+
                 |     Plugins          |
                 +----------+-----------+
                            |
                            |
                 REST API
                            |
                            v
                 +----------------------+
                 |  Identity Service    |
                 +----------+-----------+
                            |
                Configuración interna
                            |
                            v
                Variables de entorno
```

En futuras versiones únicamente cambiará la capa inferior:

```
REST API
    |
Identity Service
    |
PostgreSQL / SQLite / Vault / Secrets Manager
```

La API permanecerá inalterada.

---

# Variables de entorno

Actualmente el servicio utiliza las siguientes variables:

```
USER_NAME
USER_EMAIL
PORT
HOST
```

Ejemplo:

```
USER_NAME=David
USER_EMAIL=david@example.com
PORT=8000
HOST=0.0.0.0
```

---

# API REST

## Obtener toda la identidad

```
GET /v1/identity
```

Respuesta:

```json
{
    "name": "David",
    "email": "david@example.com"
}
```

---

## Obtener el nombre

```
GET /v1/identity/name
```

Respuesta:

```json
{
    "name": "David"
}
```

---

## Obtener el correo electrónico

```
GET /v1/identity/email
```

Respuesta:

```json
{
    "email": "david@example.com"
}
```

---

## Estado del servicio

```
GET /health
```

Respuesta:

```json
{
    "status": "UP"
}
```

---

# Estructura del proyecto

```
identity-service/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── config/
│   ├── main.py
│   └── __init__.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

La estructura está preparada para crecer sin reorganizaciones importantes.

---

# Ejecución local

## 1. Clonar el proyecto

```
git clone ...
```

## 2. Crear entorno virtual

```
python -m venv .venv
```

Activar:

Linux

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

---

## 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

## 4. Configurar variables

Crear un archivo `.env`:

```
USER_NAME=David
USER_EMAIL=david@example.com
```

---

## 5. Ejecutar

```
python -m app.main
```

o

```
uvicorn app.main:app --reload
```

---

# Cómo probar el servicio

Ejemplos mediante curl:

```
curl http://localhost:8000/health
```

```
curl http://localhost:8000/v1/identity
```

```
curl http://localhost:8000/v1/identity/name
```

```
curl http://localhost:8000/v1/identity/email
```

La documentación OpenAPI estará disponible en:

```
http://localhost:8000/docs
```

---

# Ejecución mediante Docker

Construcción:

```
docker build -t identity-service .
```

Ejecución:

```
docker run \
    --env-file .env \
    -p 8000:8000 \
    identity-service
```

O utilizando Docker Compose:

```
docker compose up --build
```

---

# Tecnologías

* Python
* FastAPI
* Pydantic
* Uvicorn
* Docker

---

# Filosofía de diseño

Este servicio sigue varios principios arquitectónicos:

* Responsabilidad única.
* API estable.
* Bajo acoplamiento.
* Alta cohesión.
* Sustitución transparente del almacenamiento.
* Configuración mediante variables de entorno.
* Sin estado (stateless).

---

# Convenciones de desarrollo

* Todo el código debe estar tipado.
* Utilizar dataclasses o modelos Pydantic cuando corresponda.
* Evitar lógica de negocio en los controladores REST.
* Toda la lógica debe residir en la capa de servicios.
* Las respuestas deben ser consistentes y tipadas.
* No acceder directamente a variables de entorno fuera del módulo de configuración.
* No duplicar lógica.
* Mantener funciones pequeñas y fácilmente testeables.

---

# Testing

El proyecto deberá incluir pruebas para:

* lectura de configuración;
* capa de servicio;
* endpoints REST;
* respuestas de error.

Las pruebas deben ser independientes del mecanismo de almacenamiento.

---

# Evolución prevista

El diseño está pensado para evolucionar sin modificar la API pública.

```
Variables de entorno
        │
        ▼
SQLite
        │
        ▼
PostgreSQL
        │
        ▼
Secrets Manager
        │
        ▼
Usuarios múltiples
        │
        ▼
Control de acceso mediante tokens
```

---

# Notas para Antigravity

## Principios

Mantener el código lo más simple posible.

No introducir abstracciones innecesarias.

No implementar funcionalidades futuras antes de tiempo (YAGNI).

Seguir principios SOLID cuando aporten claridad.

No romper la API pública existente.

No acceder a variables de entorno fuera del módulo de configuración.

El almacenamiento debe poder sustituirse en el futuro sin modificar los controladores REST.

Las decisiones de implementación deben priorizar la mantenibilidad frente a la optimización prematura.

## Estilo

* Código claro antes que código ingenioso.
* Preferir composición frente a herencia.
* Nombres descriptivos.
* Funciones cortas.
* Comentarios únicamente cuando aporten contexto.
* Evitar dependencias innecesarias.
* Mantener el proyecto preparado para ser desarrollado de forma asistida por IA.

---

# Licencia

The MIT license.
