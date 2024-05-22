create table oscars(
  filmId varchar(100) PRIMARY KEY,
  film_name varchar(100) NOT NULL,
  oscar_year INTEGER NOT NULL,
  studio varchar(100) NOT NULL,
  award varchar(100) NOT NULL CHECK ( award='Winner' or award='Nominee' ),
  release_year INTEGER NOT NULL ,
  duration INTEGER NOT NULL ,
  imdb_rating FLOAT NOT NULL ,
  imdb_votes INTEGER NOT NULL ,
  content_rating varchar(100)
);

create table participants(
  name varchar(100) PRIMARY KEY
);

create table genre_of_movie(
  genres varchar(100) NOT NULL,
  filmId varchar(100) NOT NULL,
  FOREIGN KEY (filmId) REFERENCES oscars(filmId),
  UNIQUE (genres, filmId)
);

create table director_of_movie(
  name varchar(100) NOT NULL,
  filmId varchar(100) NOT NULL,
  FOREIGN KEY (name) REFERENCES participants(name),
  FOREIGN KEY (filmId) REFERENCES oscars(filmId)
);

create table actor_in_movie(
  name varchar(100) NOT NULL,
  filmId varchar(100) NOT NULL,
  FOREIGN KEY (name) REFERENCES participants(name),
  FOREIGN KEY (filmId) REFERENCES oscars(filmId)
);

create table author_of_movie(
  name varchar(100) NOT NULL,
  filmId varchar(100) NOT NULL,
  FOREIGN KEY (name) REFERENCES participants(name),
  FOREIGN KEY (filmId) REFERENCES oscars(filmId)
);