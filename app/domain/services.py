from typing import Optional
from app.domain.models import UserSession
from app.infrastructure.redis_client import RedisClient

class SessionService:
  def __init__(self, redis_client: RedisClient):
    self.redis_client = redis_client

  def create_session(self, session: UserSession) -> None:
    self.redis_client.set(
      key=f"Session:{session.user_id}",
      value=session.session_data,
      ttl=session.ttl
    )

  def get_session(self, user_id: str) -> Optional[dict]:
    return self.redis_client.get(f"session:{user_id}")
  
  def delete_session(self, user_id: str) -> None:
    self.redis_client.delete(f"session:{user_id}")