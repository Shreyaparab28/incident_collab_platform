from app.core.database import Base, engine
from app.models import incident  # ✅ Import your models to register them

def init_db():
    Base.metadata.create_all(bind=engine)
