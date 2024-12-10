import logging
from abc import ABC, abstractmethod
from typing import Type


logging.INFO
logger = logging.getLogger("vehicle")
logger.setLevel(logging.INFO)

handlr = logging.StreamHandler()
handlr.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handlr.setFormatter(formatter)

logger.addHandler(handlr)

fhandlr = logging.FileHandler("vehicle.log")
fhandlr.setLevel(logging.INFO)
fhandlr.setFormatter(formatter)

logger.addHandler(fhandlr)


class Vehicle(ABC):

    def __init__(self, make: str, model: str, factory: str) -> None:
        self.make = make
        self.model = model
        self.factory = factory

    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.factory}: Engine started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.factory}: Motor started")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US factory")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US factory")


class EUVehicleFactory(VehicleFactory):

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU factory")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU factory")


# Використання
def main() -> None:
    us_factory: Type[VehicleFactory] = USVehicleFactory()
    eu_factory: Type[VehicleFactory] = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")

    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    eu_car = eu_factory.create_car("Volkswagen", "Lamborghini")

    eu_motorcycle = eu_factory.create_motorcycle("Ducati Motor", "Ducati")

    us_car.start_engine()
    us_motorcycle.start_engine()
    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
