from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import math


class TicketState(Enum):
    ACTIVE = "active"
    USED = "used"

@dataclass
class Ticket:
    id: int
    spotId: int
    startTime: datetime
    endTime: datetime | None = None
    state: TicketState = TicketState.ACTIVE

class ParkingLot:
    def __init__(self, parkingLotSize: int = 100, hourlyRate: int = 5):
        if parkingLotSize <= 0 or hourlyRate < 0:
            raise ValueError(" invalid parking lot or hourly rate")
    
        self.parkingLotSize = parkingLotSize
        self.hourlyRate = hourlyRate
        self.availablespots = set(range(parkingLotSize))
        self.tickets = dict[int, Ticket] = {}
        self.nextTicketId = 1
    
    def parkCar(self) -> int:
        if not self.availablespots:
            raise ValueError("parking lot is full")
        
        spotId = self.availablespots.pop()
        ticketId = self.nextTicketId
        self.nextTicketId += 1
        
        self.tickets[ticketId] = Ticket(
            id= ticketId,
            startTime=datetime.now(timezone.UTC),
            spotid= spotId
        )
        
        return ticketId
    
    def exitCar(self, ticketId: int) -> int:
        if type(ticketId) is not int or ticketId <= 0:
            raise ValueError("ticket id must be valid")

        ticket = self.tickets(ticketId)
        
        if ticket is None:
            raise ValueError("ticket not found")
    
        if ticket.state == TicketState.USED:
            raise ValueError("ticket already used")
    
        now = datetime.now(timezone.UTC)
        elapsedSeconds = (now - ticket.startTime).total_seconds()
        
        if elapsedSeconds < 0:
            raise ValueError("ticket time is in future")
        
        if(
            not 0 <= ticket.spotId < self.parkingLotSize
            or ticket.spotId in self.availablespots
        ):
            raise ValueError("ticket has an invalid or already free spot")        
        
    
        hours = math.ceil(elapsedSeconds / 3600)
        fee = hours * self.hourlyRate
        
        # change state 
        ticket.state = TicketState.USED
        ticket.endTime = now
        self.availablespots.add(ticket.spotId)
        
        return fee
    