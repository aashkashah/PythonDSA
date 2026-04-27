from DSA.LLD.MovieTheatre.movie import Movie
from DSA.LLD.MovieTheatre.showtime import ShowTime

class Theatre:
    
    def __init__(self, theatre_id: str, name: str):
        self._id = theatre_id
        self._name = name
        self._showtimes = list["ShowTime"] = []
        
    def get_id(self) -> str:
        return self._id
    
    def get_name(self) -> str:
        return self._name
    
    def get_showtimes(self) -> list["ShowTime"]:
        return self._showtimes
    
    def get_showtime_for_move(self, movie: "Movie") -> list["ShowTime"]:
        results = []
        for s in self._showtimes:
            if s.get_movie().get_id() == movie.get_id():
                results.append(s)
        return results