# cqrs-users
Se aplico el patron de Arquitectura CQRS para el manejo de la entidad Users, se separa logicamente o parcialmente ya que en la implementacion de userscommand(Microservicio para Command) se implementa un modelo solo para insert y update; y la implementacion de usersquery(Microservicio para Query) implementa un modelo optimizado para consultas usando cache.
Ambos microservicios se conectan a la misma base de datos SQL (MySQL)
Esta implementacion facilita la escalabilidad y optimizacion de recursos de los microservicios desplegados.

Se utilizo Arquitectura Hexagonal para estructurar los proyectos, cada Microservicio tiene la estructura que basicamente separa el dominio(entidades y casos de uso) de la infraestructura o implementacion(adapters e interface). De esa forma no hay dependencia del negocio sobre la tecnologia y cualquier cambio de tecnologia se podra aplicar siguiendo los "contratos" definidos(Ports)


## Estructura de carpetas
```bash
    /userscommand               # Ms Command
    /usersquery                 # Ms Query
    /docker-compose.yml         # Imagen de BD y Cache
```

## Despliegue Docker
Recrear el docker image container desde la raiz:
```bash
docker-compose up -d
```

## Despliegue Microservicios y Tests
Dirigirse a la raiz de cada proyecto y ejecutar los comandos de instalar dependencias y levantar Api Rest especificados aqui:
- [Microservicio userscommand](userscommand/README.md)
- [Microservicio usersquery](usersquery/README.md)

