from fastapi import APIRouter, HTTPException
from sqlmodel import select
from uuid import UUID

from app.api.deps import SessionDep
from app.models import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/")
async def get_all_users(session: SessionDep):
    return session.exec(select(User)).all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: UUID, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate, session: SessionDep):
    existing_user = session.exec(select(User).where(User.email == user.email)).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return user


@router.put("/{user_id}")
async def update_user_by_id(user_id: UUID, user: UserUpdate, session: SessionDep):
    user_data = user.model_dump(exclude_unset=True)

    db_user = session.get(User, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.sqlmodel_update(user_data)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: UUID, session: SessionDep):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(db_user)
    session.commit()
    return {"message": "Deleted"}
