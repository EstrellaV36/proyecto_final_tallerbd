from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, String, Float, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    travels: Mapped[list["Travel"]] = relationship(
        back_populates="users", secondary="users_travels"
    )
    expenses: Mapped[list["Expense"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"


class Travel(Base):
    __tablename__ = "travels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=False)

    users: Mapped[list["User"]] = relationship(
        back_populates="travels", secondary="users_travels"
    )
    accommodations: Mapped[list["Accommodation"]] = relationship(back_populates="travel")
    transports: Mapped[list["Transport"]] = relationship(back_populates="travel")
    activities: Mapped[list["Activity"]] = relationship(back_populates="travel")
    expenses: Mapped[list["Expense"]] = relationship(back_populates="travel")

    def __repr__(self):
        return f"Travel(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})"


class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)
    location: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=False)
    observations: Mapped[Optional[str]] = mapped_column(String)

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), nullable=False)

    travel: Mapped["Travel"] = relationship(back_populates="accommodations")
    city: Mapped["City"] = relationship()

    def __repr__(self):
        return f"Accommodation(id={self.id}, name={self.name}, location={self.location}, price={self.price})"

class Transport(Base):
    __tablename__ = "transports"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    company: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    start_datetime: Mapped[datetime] = mapped_column(nullable=False)
    start_location: Mapped[str] = mapped_column(String, nullable=False)
    end_datetime: Mapped[datetime] = mapped_column(nullable=False)
    end_location: Mapped[str] = mapped_column(String, nullable=False)

    start_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    end_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), nullable=False)

    travel: Mapped["Travel"] = relationship(back_populates="transports")
    start_city: Mapped["City"] = relationship(foreign_keys=[start_city_id])
    end_city: Mapped["City"] = relationship(foreign_keys=[end_city_id])

    def __repr__(self):
        return f"Transport(id={self.id}, type={self.type}, company={self.company}, price={self.price})"

class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)
    location: Mapped[str] = mapped_column(String, nullable=False)
    start_datetime: Mapped[datetime] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    duration: Mapped[int] = mapped_column(nullable=False)

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"), nullable=False)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), nullable=False)

    travel: Mapped["Travel"] = relationship(back_populates="activities")
    city: Mapped["City"] = relationship()

    def __repr__(self):
        return f"Activity(id={self.id}, name={self.name}, location={self.location}, start_datetime={self.start_datetime})"

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    datetime: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="expenses")
    travel: Mapped["Travel"] = relationship(back_populates="expenses")

    def __repr__(self):
        return f"Expense(id={self.id}, description={self.description}, amount={self.amount}, datetime={self.datetime})"

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, country={self.country})"

class UsersTravels(Base):
    __tablename__ = "users_travels"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), primary_key=True)

    def __repr__(self):
        return f"UsersTravels(user_id={self.user_id}, travel_id={self.travel_id})"
