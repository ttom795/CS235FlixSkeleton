from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def __init__(self, movie, review_text, rating):
        self.__movie = movie
        self.__review_text = review_text.strip()
        self.__timestamp = str(datetime.now())[:19]
        if rating > 10 or rating < 1:
            self.__rating = None
        else:
            self.__rating = rating

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie_in):
        self.__movie = movie_in

    @property
    def review_text(self):
        return self.__review_text

    @review_text.setter
    def review_text(self, review_text_in):
        self.__review_text = review_text_in

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating_in):
        if rating > 10 or rating < 1:
            self.__rating = None
        else:
            self.__rating = rating

    def __repr__(self):
        if len(self.__review_text) > 20:
            return self.__movie.title + " " + self.__timestamp + "\n" + self.__review_text[:20].strip() + "..."
        else:
            return self.__movie.title + " " + self.__timestamp + "\n" + self.__review_text

    def __eq__(self, toCompare):
        return (self.__movie == toCompare.__movie and self.__review_text == toCompare.__review_text
                and self.__rating == toCompare.__rating and self.__timestamp == toCompare.__timestamp)
