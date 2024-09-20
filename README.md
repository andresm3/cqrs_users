# cqrs-challenge
Tarea: Crear el “INIT’ de un Proyecto Backend con Arquitectura Hexagonal
y CQRS

## Stack
Python 3.11
FastAPI
SQLAlchemy
MySQL

## Estructura de carpetas
```bash
/src
    /domain
        /entities               # Entidades de negocio (modelo de dominio)
            /user.py            # Entidad User
        /use_cases
            /create_user.py      # Caso de uso: Crear usuario
    /ports
      /repositories             # Interfaces (puertos de salida) para repositorios
      /services.py              # Interfaces (puertos de salida) para servicios externos
    /adapters
        /models                 # Implementacion de entidades en ORM
        /repositories
            /user_repo.py           # Implementación del puerto para repositorio SQLAlchemy
        /services
            /email_service.py    # Implementación del puerto para enviar emails
    /interfaces
      /api                      # Adaptador para la API REST usando FastAPI
      /config_db.py             # Configuracion BD
```

## Configuration
You will need to recreate docker image container from the root path:
docker-compose up -d

## Installing librariproject dependencieses
poetry install

## Usage
To start the ms-users-command:
uvicorn app:app

## Run tests
To run unit and integration tests:
npm run test
* To run the integration test please run the file individually(index.spec.js) and you will need the server up

## Documentation
Using swaggerUI express, API documentation will be in the following path
http://localhost:8000/docs
