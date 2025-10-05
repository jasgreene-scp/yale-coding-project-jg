from fastapi import APIRouter, HTTPException

router = APIRouter()
mock_users = ()

@router.post("/mock_register")
def mock_register(username: str, password: str, email: str):
    if username in mock_users:
        raise HTTPException(status_code=400, detail="User already exists")
    mock_users[username] = {
        "password": f"[HASHED]{password}",
        "email": email
    }
    return {
        "user": {
            "username": username,
            "email": email,
            "role": "user",
            "token": "mock-token-123"
        }
    }

@router.post("/mock_login")
def mock_login(username: str, password: str):
    if mock_users.get(username) != f"[HASHED]{password}":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "user": {
            "username": username,
            "role": "user", 
            "token": "mock-token-123"
        }
    }

@router.post("/mock_reset_password")
def mock_reset_password(username: str):
    return {
        "message": f"Password reset link sent to {username}'s email (pretend)"
    }