from litestar import Litestar
from app.controllers import (
    UserController,
    AccommodationController,
    TransportController,
    ActivityController,
    ExpenseController,
    CityController,
    TravelController
)
from app.database import db_plugin

app = Litestar(
    [UserController, AccommodationController, TransportController, ActivityController, ExpenseController, CityController, TravelController],
    debug=True,
    plugins=[db_plugin],
)
