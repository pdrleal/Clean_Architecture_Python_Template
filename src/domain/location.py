from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.domain.base.base_class import Base


class Location(Base):
    address: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(20))
    country: Mapped[str] = mapped_column(String(20))

    """
        Must add the many side with the list of objects. 
        back_populates must be the name of the attribute on the other side.
    """
    events: Mapped[List["Event"]] = relationship(back_populates="location")
    location: Mapped["Location"] = relationship(back_populates="events")
