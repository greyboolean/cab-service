from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, type, id):
        self.__type = type
        self.__id = id

    def getType(self):
        return self.__type

    def getId(self):    
        return self.__id

class PassengerVehicle(Vehicle):

    def __init__(self, type, id, passengerCapacity):
        super().__init__(type, id)
        self.__passengerCapacity = passengerCapacity

    def getPassengerCapacity(self):
        return self.__passengerCapacity

class HeavyVehicle(Vehicle):
    pass

class Car(PassengerVehicle):
    pass

class Van(PassengerVehicle):
    pass

class Threewheeler(PassengerVehicle):
    pass

class Truck(HeavyVehicle):

    def __init__(self, type, id, size):
        super().__init__(type, id)
        self.__size = size

    def getSize(self):
        return self.__size

class Lorry(HeavyVehicle):

    def __init__(self, type, id, maxLoad):
        super().__init__(type, id)
        self.__maxLoad = maxLoad

    def getMaxLoad(self):
        return self.__maxLoad

