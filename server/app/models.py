from sqlmodel import SQLModel, Field
from uuid import uuid4, UUID



class User(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    email: str = Field(unique=True)
    age: int | None = None


class UserCreate(SQLModel):
    name: str
    email: str = Field(unique=True)
    age: int | None = None



class UserUpdate(SQLModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None
