from sqlalchemy.orm import Session
from database import engine
import models as m
from datetime import datetime as dt

m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    movie1 = m.Movie(
        movie_name="Интерстеллар",
        year="2014",
        time="169",
        rate="8.7",
        description="Научная фантастика",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie1)
    
    movie2 = m.Movie(
        movie_name="Титаник",
        year="1997",
        time="194",
        rate="8.4",
        description="Фильм-катастрофа",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie2)
    
    movie3 = m.Movie(
        movie_name="Август",
        year="2025",
        time="138",
        rate="7.4",
        description="Исторический триллер",
        poster="/Ссылка на изображение",
        date_add=dt.strptime("2012-12-12", "%Y-%m-%d").date(),
    )
    session.add(movie3)

    genre1 = m.Genre(genre_name="Фантастика", description="")
    session.add(genre1)
    genre2 = m.Genre(genre_name="Драма", description="")
    session.add(genre2)
    genre3 = m.Genre(genre_name="Военный", description="")
    session.add(genre3)

    movie_genre1 = m.Movie_Genre(movie_id="1", genre_id="1")
    session.add(movie_genre1)
    movie_genre2 = m.Movie_Genre(movie_id="2", genre_id="1")
    session.add(movie_genre2)
    movie_genre3 = m.Movie_Genre(movie_id="2", genre_id="3")
    session.add(movie_genre3)
    movie_genre4 = m.Movie_Genre(movie_id="3", genre_id="2")
    session.add(movie_genre4)
    movie_genre5 = m.Movie_Genre(movie_id="3", genre_id="3")
    session.add(movie_genre5)

    session.commit()