from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import List

class CreateMovie(BaseModel):
    movie_name: str = Field(example="Интерстеллар")
    year: int = Field(ge=1900, le=3000, example="2014")
    time: int = Field(gt=0, example="169")
    rate: float = Field(ge=0, le=10, example="6")
    description: str | None = Field(example="Научная фантастика")
    poster: str = Field(example="Ссылка на изображение")
    date_add: date = Field(example="2012-12-12")
    
    genres_id:List[int]=Field()


class CreateGenre(BaseModel):
    genre_name: str = Field(example="Научная фантастика")
    description: str | None = Field(example="Фильм-катастрофа")



