from datetime import datetime
from datetime import date
from typing import List, Type
from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    username: str
    password: str


class DateModel(BaseModel):
    date: date

    def json_schema(self):
        schema = super().json_schema()
        if "PlainValidatorFunctionSchema" in schema.get("type", ""):
            schema = None
        return schema


class TagModel(BaseModel):
    name: str = Field(max_length=25)


class TagResponse(TagModel):
    id: int

    class Config:
        from_attributes = True


class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150)


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    e_mail: EmailStr
    phone_number: str = Field(max_length=20)
    born_date: DateModel
    description: str = Field(max_length=150)


class NoteModel(NoteBase):
    tags: List[int]


class ContactModel(ContactBase):
    born_date: date


class NoteUpdate(NoteModel):
    done: bool


class ContactUpdate(ContactModel):
    done: bool


class NoteStatusUpdate(BaseModel):
    done: bool


class ContactStatusUpdate(BaseModel):
    done: bool


class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    tags: List[TagResponse]

    class Config:
        from_attributes = True


class ContactResponse(ContactBase):
    id: int
    name: str
    last_name: str
    e_mail: str
    phone_number: str
    born_date: date
    description: str