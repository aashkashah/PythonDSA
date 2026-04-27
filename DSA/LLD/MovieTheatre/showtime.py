import datetime

from DSA.LLD.MovieTheatre.movie import Movie
from DSA.LLD.MovieTheatre.theatre import Theatre


class ShowTime:
    
    def __int__(self, showtime_id: str, 
                movie: "Movie", theatre: "Theatre", 
                dt: datetime, screen_label: str):
        self._movie = ""
        self._theatre = theatre
        self._date = dt
    
    def get_movie(self) -> "Movie":
        return self._movie
    
    def get_theatre(self) -> "Theatre":
        return self._theatre
    
    def get_datetime(self) -> datetime:
        return self._date
    