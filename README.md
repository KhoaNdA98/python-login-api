# Python Login API

Basic login API service built with FastAPI.

## Features
- Health/root endpoint
- Basic login endpoint
- Simple hardcoded demo credentials

## Run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API
### GET /
Returns service status.

### POST /login
Request body:
```json
{
  "username": "admin",
  "password": "123456"
}
```

Success response:
```json
{
  "success": true,
  "message": "Login successful",
  "token": "demo-token-123"
}
```

## Note
This is a basic demo service, not suitable for production authentication.
