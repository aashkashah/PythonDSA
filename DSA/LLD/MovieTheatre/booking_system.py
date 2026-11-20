
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr

from DSA.LLD.MovieTheatre.movie import Movie
from DSA.LLD.MovieTheatre.reservation import Reservation
from DSA.LLD.MovieTheatre.theatre import Theatre
from DSA.LLD.MovieTheatre.showtime import ShowTime


class BookingSystem(BaseModel):
    # Movie/Theatre/ShowTime/Reservation are plain classes, not pydantic models
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # public input field: BookingSystem(theatres=[...])
    theatres: list[Theatre] = Field(default_factory=list)

    # internal indexes (not part of the model's fields / validation)
    _movies_by_id: dict[str, Movie] = PrivateAttr(default_factory=dict)
    _showtimes_by_movie_id: dict[str, list[ShowTime]] = PrivateAttr(default_factory=dict)
    _showtimes_by_id: dict[str, ShowTime] = PrivateAttr(default_factory=dict)
    _reservations_by_id: dict[str, Reservation] = PrivateAttr(default_factory=dict)

    def search_movies(self, title: str) -> list[ShowTime]:
        pass

    def get_showtimes_at_theatre(self, theatre: Theatre) -> list[ShowTime]:
        pass

    def book(self, showtime_id: str, seat_ids: list[str]) -> Reservation:
        pass

    def cancel_reservation(self, confirmation_id: str) -> None:
        pass
