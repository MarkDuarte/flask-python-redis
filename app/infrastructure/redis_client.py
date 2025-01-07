import redis
from typing import Optional

class RedisClient:
  def __init__(self, host: str, port: int, db: int):
    self.client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

  def set(self, key: str, value: dict, ttl: Optional[int] = None) -> None:
    self.client.set(key, value, ex=ttl)

  def get(self, key: str) -> Optional[dict]:
    result = self.client.get(key)
    return result if result else None
  
  def delete(self, key: str) -> None:
    self.client.delete(key)