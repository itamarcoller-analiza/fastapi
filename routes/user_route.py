from fastapi import routing, Body
from models.user_model import User 

router = routing.APIRouter(prefix='/user')

users = []

@router.post("/")
async def create_user(user : User):
    users.append(user)
    return {"message": "User created", "user": user.model_dump()}

@router.get("/")
async def get_users():
    return {"message": "List of users", "users": [user.model_dump() for user in users]}

@router.patch("/{user_id}")
async def update_user(user_id: int, user: User = Body(...)):
    users[user_id] = user
    return {"message": f"User {user_id} updated"}

@router.delete("/{index}")
async def delete_user(index: int):
    users.pop(index)
    return {"message": f"User {index} deleted"}
