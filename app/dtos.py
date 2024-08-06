from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from app.models import (
    User,
    Accommodation,
    Transport,
    Activity,
    Expense,
    City,
    Travel
)

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travels", "expenses"})

class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"travels", "expenses"})

class UserReadFullDTO(SQLAlchemyDTO[User]):
    pass

class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travels", "expenses"}, partial=True)



class AccommodationReadDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city", "expenses"})

class AccommodationReadFullDTO(SQLAlchemyDTO[Accommodation]):
    pass

class AccommodationCreateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"})

class AccommodationUpdateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "city", "expenses"}, partial=True)


class TransportReadFullDTO(SQLAlchemyDTO[Transport]):
    pass

class TransportReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "start_city", "end_city"})

class TransportCreateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "start_city", "end_city"})

class TransportUpdateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel", "start_city", "end_city"}, partial=True)



class ActivityReadDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "city"})  

class ActivityReadFullDTO(SQLAlchemyDTO[Activity]):
    pass

class ActivityCreateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "travel","city"})

class ActivityUpdateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)



class ExpenseReadFullDTO(SQLAlchemyDTO[Expense]):
    pass

class ExpenseReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"travel", "user"})

class ExpenseCreateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id","travel", "user"})

class ExpenseUpdateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)


class CityReadDTO(SQLAlchemyDTO[City]):
    pass

class CityCreateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"})

class CityUpdateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)


class TravelReadFullDTO(SQLAlchemyDTO[Travel]):
    pass

class TravelReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"users","accommodations","transports","activities","expenses"})

class TravelCreateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id","users","accommodations","transports","activities","expenses"})

class TravelUpdateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id"}, partial=True)
