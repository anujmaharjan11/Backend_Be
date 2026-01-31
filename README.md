# Flask Auth API

## Setup

1. **Install dependencies:**
```bash
pip install flask flask-sqlalchemy flask-migrate flask-jwt-extended flask-restful python-dotenv psycopg2-binary
```

2. **Create `.env` file:**
```env
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your-secret-key-here
```

3. **Initialize database (if using PostgreSQL):**
```bash
# Create migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Running the API

```bash
python run.py
```

The API will run on `http://localhost:5000`

## Testing the API

### 1. Create a user
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "password123"}'
```

### 2. Login
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'
```

### 3. Access profile (with JWT token)
```bash
curl -X GET http://localhost:5000/profile \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

### 4. Get all users
```bash
curl -X GET http://localhost:5000/users
```

## Available Endpoints

- `POST /users` - Create new user
- `GET /users` - Get all users
- `POST /login` - User login
- `GET /profile` - Get user profile (requires JWT)