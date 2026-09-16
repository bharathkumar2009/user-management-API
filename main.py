from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,EmailStr
from database import create_table,get_connection
from crud import get_users,get_user,create_user


app = FastAPI()

class User(BaseModel):
    name:str = Field(min_length = 3 ,max_length = 50)
    email : EmailStr
    age :int= Field(ge=18,le=100)


create_table()
@app.post("/users")
def add_user(user:User):
    try:
        user_id = create_user(
            user.name,
            user.email,
            user.age
        )
        return {
            "message": "user added sucessfully",
            "id" : user_id
        }
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

@app.get("/users")
def get_all_users():
    return get_users()
@app.get("/users/{user_id}")
def read_user(user_id: int):

    user = get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (user.name, user.email, user_id)
    )

    connection.commit()

    connection.close()

    return {"message": "User updated successfully"}
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )

    connection.commit()

    connection.close()

    return {"message": "User deleted successfully"}