from domainmodel.user import User
from domainmodel.movie import Movie
from domainmodel.genre import Genre
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
import csv
import random


class recommended:
    def __init__(self, user):
        self.user = user
        self.movies = MovieFileCSVReader('datafiles/Data1000Movies.csv')

    def __repr__(self):
        return "<" + "Recommendations for " + self.user.user_name + ">"

    def suggest_genre(self):
        last_watched = self.user.watched_movies[-1].title
        print(
            "Hi " + self.user.user_name + "! The last movie you watched was " + last_watched + ".\nHere are some movies of the same genre: ")
        movie_title_list = []
        movie_genre_list = []
        csv_file_contents = csv.DictReader(open('datafiles/Data1000Movies.csv', mode='r', encoding='utf-8-sig'))
        for individual_dictionary in csv_file_contents:
            for key, value in individual_dictionary.items():
                if key == "Title":
                    movie_title_list.append(value)
                if key == "Genre":
                    movie_genre_list.append(value.split(","))
        movie_name = self.user.watched_movies[-1].title
        movie_index = movie_title_list.index(movie_name)
        genres = movie_genre_list[movie_index]
        rec_list = []
        for item in movie_genre_list:
            for sub_item in item:
                title = movie_title_list[movie_genre_list.index(item)]
                if sub_item in genres and title not in rec_list and title != last_watched:
                    rec_list.append(title)
        return_list = []
        if len(rec_list) >= 5:
            for i in range(5):
                random_same_genre_movie = random.choice(rec_list)
                return_list.append(random_same_genre_movie)
                rec_list.pop(rec_list.index(random_same_genre_movie))
        else:
            return rec_list
        return return_list

    def suggest_director(self):
        last_watched = self.user.watched_movies[-1].title
        print(
            "Hi " + self.user.user_name + "! The last movie you watched was " + last_watched + ".\nHere are some movies by the same director: ")
        movie_title_list = []
        movie_director_list = []
        csv_file_contents = csv.DictReader(open('datafiles/Data1000Movies.csv', mode='r', encoding='utf-8-sig'))
        for individual_dictionary in csv_file_contents:
            for key, value in individual_dictionary.items():
                if key == "Title":
                    movie_title_list.append(value)
                if key == "Director":
                    movie_director_list.append(value)
        movie_name = self.user.watched_movies[-1].title
        movie_index = movie_title_list.index(movie_name)
        director = movie_director_list[movie_index]
        rec_list = []
        for item in movie_director_list:
            index = movie_director_list.index(item)
            title = movie_title_list[index]
            if item == director and title not in rec_list:
                if title != last_watched:
                    rec_list.append(title)
                movie_director_list.pop(index)
                movie_title_list.pop(index)

        return_list = []
        if len(rec_list) >= 5:
            for i in range(5):
                random_same_director_movie = random.choice(rec_list)
                return_list.append(random_same_director_movie)
                rec_list.pop(rec_list.index(random_same_director_movie))
        else:
            return rec_list
        return return_list

    def suggest_actor(self):
        last_watched = self.user.watched_movies[-1].title
        print(
            "Hi " + self.user.user_name + "! The last movie you watched was " + last_watched + ".\nHere are some movies with the same actors: ")
        movie_title_list = []
        movie_actor_list = []
        csv_file_contents = csv.DictReader(open('datafiles/Data1000Movies.csv', mode='r', encoding='utf-8-sig'))
        for individual_dictionary in csv_file_contents:
            for key, value in individual_dictionary.items():
                if key == "Title":
                    movie_title_list.append(value)
                if key == "Actors":
                    movie_actor_list.append(value.split(","))
        movie_name = self.user.watched_movies[-1].title
        movie_index = movie_title_list.index(movie_name)
        actors = movie_actor_list[movie_index]
        rec_list = []
        for item in movie_actor_list:
            for sub_item in item:
                title = movie_title_list[movie_actor_list.index(item)]
                if sub_item in actors and title not in rec_list and title != last_watched:
                    rec_list.append(title)
        return_list = []
        if len(rec_list) >= 5:
            for i in range(5):
                random_same_actor_movie = random.choice(rec_list)
                return_list.append(random_same_actor_movie)
                rec_list.pop(rec_list.index(random_same_actor_movie))
        else:
            return rec_list
        return return_list