from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.domain.base.base_class import Base


class Profile(Base):
    email: Mapped[str] = mapped_column(String(40))
    password: Mapped[str] = mapped_column(String(40))

    people: Mapped["People"] = relationship(back_populates="profile")
