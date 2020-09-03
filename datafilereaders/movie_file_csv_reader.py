import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:
    def __init__(self, filename):
        self.__file_name = filename
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []
    def read_csv_file(self):
        csv_file_contents = csv.DictReader(open(self.__file_name, mode='r', encoding='utf-8-sig'))
        for individual_dictionary in csv_file_contents:
            for key,value in individual_dictionary.items():
                if key == "Title":
                    temptitle = value
                if key == "Actors":
                    tempactorlist = value.split(",")
                    for actor in tempactorlist:
                        actor = Actor(actor.strip())
                        if actor not in self.dataset_of_actors:
                            self.dataset_of_actors.append(actor)
                if key == "Genre":
                    tempgenrelist = value.split(",")
                    for genre in tempgenrelist:
                        genre = Genre(genre.strip())
                        if genre not in self.dataset_of_genres:
                            self.dataset_of_genres.append(genre)
                if key == "Director":
                    tempdirectorlist = value.split(",")
                    for director in tempdirectorlist:
                        director = Director(director.strip())
                        if director not in self.dataset_of_directors:
                            self.dataset_of_directors.append(director)
                if key == "Year":
                    self.dataset_of_movies.append(Movie(temptitle, value))