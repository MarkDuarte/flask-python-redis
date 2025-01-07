# Flask Redis DDD Example

This is a simple example of a Flask application using Redis for session management, following Domain-Driven Design (DDD) principles. The application is built with Python and uses type annotations for better clarity and safety.

---

## Project Structure

```plaintext
flask-redis-ddd
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models.py       # Domain models
│   │   ├── services.py     # Business logic
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── redis_client.py # Redis integration
│   ├── interfaces/
│   │   ├── __init__.py
│   │   ├── routes.py       # Flask API routes
├── main.py                 # Application entry point
├── requirements.txt


## Running the Project

### 1. Start Redis Locally:

```bash
docker run --name redis -p 6379:6379 -d redis

### Install Dependencies:

```bash
pip install -r requirements.txt

### Start the Flask server:
```bash
python main.py

# Testing the Endpoints

### Create a Session:
```bash
curl -X POST http://127.0.0.1:5000/session \
-H "Content-Type: application/json" \
-d '{"user_id": "123", "session_data": {"name": "John Doe"}, "ttl": 3600}'

### Get a Session:
```bash
curl http://127.0.0.1:5000/session/123

### Delete a Session:
```bash
curl -X DELETE http://127.0.0.1:5000/session/123

# Features

- Domain-Driven Design (DDD): Separation of concerns into domain, infrastructure, and interfaces layers.
- Redis Integration: Sessions are stored in Redis with a configurable TTL.
- Type Annotations: Uses Python type hints and pydantic for data validation.

# Dependencies

The project uses the following Python libraries:

- Flask: Web framework.
- redis: Redis client for Python.
- pydantic: Data validation and settings management.


License
This project is open-source and available under the MIT License.



