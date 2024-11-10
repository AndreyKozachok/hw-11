from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, field_validator


class ContactRequest(BaseModel):
    name: str = Field(max_length=150)
    last_name: str = Field(max_length=150)
    email: EmailStr
    phone: str = Field(max_length=20)
    birthday: Optional[str] = Field(max_length=10)
    info: Optional[str] = Field(max_length=500)

    @field_validator("birthday", mode="after")
    def validate_birthday(cls, value):
        if value:
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Birthday must be in the format dd.mm.yyyy")
        return value


class ContactResponse(ContactRequest):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
