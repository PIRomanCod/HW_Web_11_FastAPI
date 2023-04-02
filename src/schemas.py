from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    firstname: str = Field(default='Unknown', min_length=1, max_length=50)
    lastname: str = Field(default='Unknown', min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(default='+380001234567', min_length=10, max_length=15)
    birthday: date
    additional_info: str = Field(default='nothing yet', min_length=1, max_length=150)
    is_favorite: bool = False


class ContactFavoriteModel(BaseModel):
    is_favorite: bool = False


class ContactResponse(BaseModel):
    id: int = 1
    firstname: str = 'Unknown'
    lastname: str = 'Unknown'
    email: EmailStr
    phone: str = '0001234567'
    birthday: date = None
    additional_info: str = 'nothing yet'
    is_favorite: bool = False
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

