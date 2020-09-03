from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__list_of_movies = []
    def add_movie(self, movie):
        if movie not in self.__list_of_movies:
            self.__list_of_movies.append(movie)
    def remove_movie(self, movie):
        if movie in self.__list_of_movies:
            self.__list_of_movies.pop(self.__list_of_movies.index(movie))
    def select_movie_to_watch(self, index):
        if index >= 0 and index <= len(self.__list_of_movies):
            return self.__list_of_movies[index]
        else:
            return None
    def size(self):
        return len(self.__list_of_movies)
    def first_movie_in_watchlist(self):
        if len(self.__list_of_movies) > 0:
            return self.__list_of_movies[0]
        else:
            return None
    def __iter__(self):
        self._Current = -1;
        return self
    def __next__(self):
        if self._Current < len(self.__list_of_movies)-1:
            self._Current += 1
            return self.__list_of_movies[self._Current]
        else:
            raise StopIteration