import fastapi
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()

user_db = {}

@app.post("/api/users")
def create_user(request: CreateUserRequest) -> UserResponse:
    user_id = len(user_db) + 1
    user_db[user_id] = {
        "name": request.name,
        "phone_number": request.phone_number,
        "height": request.height,
        "bio": request.bio,
    }
    return {
        "user_id": user_id,
        "name": request.name,
        "phone_number": request.phone_number,
        "height": request.height,
        "bio": request.bio,
    }

@app.get("/api/users/{user_id}")
def get_user(
    user_id: int
) -> UserResponse:

    try:
        data = user_db[user_id]
    except:
        raise ValueError('존재하지 않는 user ID 입니다.')

    return {
        "user_id": user_id,
        "name": data["name"],
        "phone_number": data["phone_number"],
        "height": data["height"],
        "bio": data["bio"],
    }


@app.get("/api/users")
def get_users(
    min_height: float = Query(0), max_height: float = Query(float('inf'))
) -> list[UserResponse]:
    return [
        {
            "user_id": key,
            "name": item['name'],
            "phone_number": item['phone_number'],
            "height": item['height'],
            "bio": item['bio'],
        } for key, item in user_db.items() if item['height'] >= min_height and item['height'] <= max_height
    ]