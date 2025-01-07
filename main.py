from flask import Flask
from app.config import Config
from app.infrastructure.redis_client import RedisClient
from app.domain.services import SessionService
from app.interfaces.routes import create_routes

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  redis_client = RedisClient(
    host=app.config["REDIS_HOST"],
    port=app.config["REDIS_PORT"],
    db=app.config["REDIS_DB"]
  )

  session_service = SessionService(redis_client)
  app.register_blueprint(create_routes(session_service))

  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)