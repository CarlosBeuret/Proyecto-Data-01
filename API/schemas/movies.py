"""
from typing import Optional
from pydantic import BaseModel, Field


class Movies(BaseModel):
    id: Optional[int]
    type: str 
    title: str  
    director: str 
    cast: str 
    country: str
    date_added: str
    release_year: int 
    rating: str
    genre: str
    description: str = Field(default = "La descripción debe contener entre 4 y 150 caracteres", min_length= 4, max_length=150)
    platform: str
    duration: float = Field(ge=1, le=500)
    type_duration: str
    # pordemos reemplazar default
    class Config:
        schema_extra = {
            "example":{
                "title": "Titulo de la película",
                "country": "pais"
            }
        }
        """