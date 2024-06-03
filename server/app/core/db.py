from sqlmodel import Session, create_engine, SQLModel

from app.core.config import settings
from app.models import User  # noqa: F401 for Ruff

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)

# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly


def init_db(session: Session) -> None:
    SQLModel.metadata.create_all(engine)
