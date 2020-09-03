class Genre:
    def __init__(self, genreName):
        self.genre = genreName
    def __repr__(self):
        genreReturn = self.genre
        if self.genre == "":
            return "<Genre None>"
        return f'<Genre {self.genre}>'
    def __eq__(self, toCompare):
        return self.genre == toCompare.genre
    def __lt__(self, toCompare):
        return self.genre < toCompare.genre
    def __hash__(self):
        return hash(self.genre)