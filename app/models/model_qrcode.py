from fastapi import Form
from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import List, Union
from enum import Enum
import inspect

def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(default = arg.default) if arg.default is not inspect._empty else Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

@form_body
class ConfigSchema(BaseModel):
    ngrok_url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "ngrok_url": "http://6edb-202-29-108-66.ngrok.io"
            }
        }


@form_body
class SingleUrlSchema(BaseModel):
    url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "url": "http://codeinsane.wordpress.com"
            }
        }

@form_body
class MultipleUrlSchema(BaseModel):
    url: Union[List[str], None] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "url": "http://codeinsane.wordpress.com, https://github.com/natthasath"
            }
        }

@form_body
class EmailAddressSchema(BaseModel):
    email: str = Field(...)
    subject: str = Field(...)
    body: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "username@example.com",
                "subject": "Hello",
                "body": "This is the body of the email."
            }
        }

@form_body
class MobileMessageSchema(BaseModel):
    phone: str = Field(...)
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "phone": "0123456789",
                "message": "Hello, this is an SMS message."
            }
        }

@form_body
class PhoneSchema(BaseModel):
    phone: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "phone": "0123456789"
            }
        }

@form_body
class ContactSchema(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "username@example.com",
                "phone": "0123456789",
                "address": "Bangkok, Thailand"
            }
        }

@form_body
class EventSchema(BaseModel):
    subject: str = Field(...)
    location: str = Field(...)
    description: str = Field(...)
    start: str = Field(...)
    end: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "subject": "Hello",
                "location": "Bangkok, Thailand",
                "description": "This is the description of the event.",
                "start": "20230315T190000Z",
                "end": "20230315T210000Z"
            }
        }

class AndroidIosUrlSchema(BaseModel):
    android: str = Field(...)
    ios: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "android": "https://play.google.com/store/apps/details?id=com.spotify.music&hl=th&gl=US",
                "ios": "https://apps.apple.com/us/app/spotify-music-and-podcasts/id324684580",
            }
        }

class RedirectSchema(BaseModel):
    url: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "url": "http://codeinsane.wordpress.com"
            }
        }