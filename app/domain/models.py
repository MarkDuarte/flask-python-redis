from typing import Optional
from pydantic import BaseModel, Field

class UserSession(BaseModel):
  user_id: str
  session_data: dict
  ttl: Optional[int] = Field(default=3000, description="Time-to-live in seconds")