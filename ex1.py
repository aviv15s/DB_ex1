import csv
from io import TextIOWrapper
from zipfile import ZipFile

# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
    oscars_outfile = open("oscars.csv", 'w', encoding='UTF8', newline='')
    oscars_outwriter = csv.writer(oscars_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    participants_outfile = open("participants.csv", 'w', encoding='UTF8', newline='')
    participants_outwriter = csv.writer(participants_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    actors_outfile = open("actor_in_movie.csv", 'w', encoding='UTF8', newline='')
    actors_outwriter = csv.writer(actors_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    authors_outfile = open("author_of_movie.csv", 'w', encoding='UTF8', newline='')
    authors_outwriter = csv.writer(authors_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    directors_outfile = open("director_of_movie.csv", 'w', encoding='UTF8', newline='')
    directors_outwriter = csv.writer(directors_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    genre_of_movie_outfile = open("genre_of_movie.csv", 'w', encoding='UTF8', newline='')
    genre_of_movie_outwriter = csv.writer(genre_of_movie_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    with ZipFile('oscars.zip') as zf:
        with zf.open('oscars.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            seen_names = set()

            for row in reader:
                _, film_name, oscar_year, studio, award, release, length, genres, IMDB_rating, IMDB_votes, rating, directors, authors, actors, filmID = row
                # create new movie entry
                oscars_outwriter.writerow([filmID, film_name, oscar_year, studio, award, release, length, IMDB_rating, IMDB_votes, rating])

                authors = split_list_value(authors)
                actors = split_list_value(actors)
                directors = split_list_value(directors)

                # add directors, actors and authors
                # assume film name is not null, only check if actor/director/author name is null
                for name in authors:
                    if name != "" and name not in seen_names:
                        authors_outwriter.writerow([name, filmID])
                        participants_outwriter.writerow([name])
                        seen_names.add(name)
                for name in directors:
                    if name != "" and name not in seen_names:
                        directors_outwriter.writerow([name, filmID])
                        participants_outwriter.writerow([name])
                        seen_names.add(name)
                for name in actors:
                    if name != "" and name not in seen_names:
                        actors_outwriter.writerow([name, filmID])
                        participants_outwriter.writerow([name])
                        seen_names.add(name)

                # add genres
                genres = split_list_value(genres)
                for g in genres:
                    genre_of_movie_outwriter.writerow([g, filmID])

    actors_outfile.close()
    directors_outfile.close()
    authors_outfile.close()
    genre_of_movie_outfile.close()
    participants_outfile.close()
    oscars_outfile.close()

# return the list of all tables
def get_names():
    return ["oscars", "participants", "actor_in_movie", "author_of_movie", "director_of_movie", "genre_of_movie"]


def split_list_value(list_value):
    return list_value.split("&&")


if __name__ == "__main__":
    process_file()

