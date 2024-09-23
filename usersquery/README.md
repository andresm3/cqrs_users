# cqrs-usersquery
Siguiendo el patron CQRS, este Microservicio se encarga de las operaciones de Consulta(Query) sobre la entidad Users. Esta optimizado para consultas usando memoria en cache(Redis), se usa la misma base de datos del microservicio que se encarga de los Comandos, la tabla users esta normalizada y con indices necesarios.
Esta implementacion facilita la escalabilidad y optimizacion de recursos de los microservicios desplegados.

## Stack
Python 3.11
FastAPI
SQLAlchemy
MySQL
Redis

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
        /redis_cache.py           # Implementación del puerto para Cache Redis
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
To start the usersquery:
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
http://localhost:8010/docs
