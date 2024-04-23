from datetime import datetime, time
from typing import Optional, Literal

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from src.domain.base.base_class import Base

EventType = Literal["CUSTOM", "ALL_DAY"]
Recurring = Literal["NO", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]


class Event(Base):
    name: Mapped[str] = mapped_column(String(40))  # only mapped_column() function is used to specify details.
    recurring: Mapped[Optional[str]]  # by defining optional, it creates a nullable attributes in the database
    event_type: Mapped[EventType]  # to define ENUM column create a Literal variable and link to column type
    start_datetime: Mapped[datetime]
    end_datetime: Mapped[datetime]
    """
        To define relationships, an id and object column must be added on the "many" side, where the foreign key is
        the id of the respective connection and the object column must be mapped to the entity class name.
        The back_populates attributes must be with the same name of the property on the other relationship side.
    """
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id"))
    location: Mapped["Location"] = relationship(back_populates="events")

    @validates("event_type", "start_datetime", "end_datetime")
    def validate_event_type(self, key, value):
        """
        Validate only when all values are present:
        https://gist.github.com/matrixise/6417293?permalink_comment_id=1638256#gistcomment-1638256
        """
        if (key == 'event_type' and isinstance(self.start_datetime, datetime)
                and isinstance(self.end_datetime, datetime)):
            self.check_datetimes_constraint()
        elif (key == 'start_datetime' and isinstance(self.end_datetime, datetime)
              and isinstance(self.event_type, str)):
            self.check_datetimes_constraint()
        elif (key == 'end_datetime' and isinstance(self.start_datetime, datetime)
              and isinstance(self.event_type, str)):
            self.check_datetimes_constraint()
        return value

    def check_datetimes_constraint(self):
        if self.end_datetime < self.start_datetime:
            raise AssertionError("The End Datetime must be "
                                 "greater-or-equal than the Start Datetime")
        if self.event_type == 'ALL_DAY':
            if ((self.start_datetime.date() != self.end_datetime.date()) or
                    (self.start_datetime.time() == time(9, 30)) or
                    (self.end_datetime.time() == time(18, 30))):
                raise ValueError("For 'ALL_DAY' events, Start Datetime must be set to 9:30 AM and End Datetime "
                                 "to 6:30 PM of the same day.")
