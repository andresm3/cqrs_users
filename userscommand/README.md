# cqrs-userscommand
Siguiendo el patron CQRS, este Microservicio se encarga de las operaciones de Comandos(Command) sobre la entidad Users. Se utiliza base de datos MySQL, la tabla users esta normalizada y con indices necesarios.
Esta implementacion facilita la escalabilidad y optimizacion de recursos de los microservicios desplegados.

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
/tests
    /domain                     # Tests sobre logica de negocio, entidades
    /adapters                   # Tests sobre adaptadores: repositorios, servicios
```

## Installing library project dependencies
```bash
poetry install
```

## Usage
To start the userscommand:
```bash
python.exe .\main.py
```

## Run tests
To run unit and integration tests:
```bash
python -m unittest discover
```

## Run Coverage tests
To run coverage test:
```bash
coverage run -m unittest discover
coverage report
coverage html
```

## Documentation
Using swaggerUI express, API documentation will be in the following path
http://localhost:8000/docs
