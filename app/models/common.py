"""
Common Request Models
"""
from datetime import date

from pydantic import BaseModel, root_validator

class Item(BaseModel):
  id: str
  display_name: str
  last_completed: date
  cadence: int
