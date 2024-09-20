from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.adapters.models.user_model import Base

# Configuración de la base de datos
engine = create_engine("mysql+pymysql://root:password@localhost:3306/database")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
