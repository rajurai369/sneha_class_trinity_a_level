
class Vehicle:
    def __init__(self, ID: str, MaxSpeed: int, IncreaseAmount: int):
        # Attributes (private)
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

# ==========================
# 2(a)(ii) Get methods
# ==========================
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

# ==========================
# 2(a)(iii) Set methods
# ==========================
    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed

    def SetHorizontalPosition(self, position):
        self.__HorizontalPosition = position

# ==========================
# 2(a)(iv) IncreaseSpeed method
# ==========================
    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount <= self.__MaxSpeed:
            self.__CurrentSpeed += self.__IncreaseAmount
        else:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed

# ==========================
# 2(b)(i) Helicopter class and constructor
# ==========================
class Helicopter(Vehicle):
    def __init__(self, ID: str, MaxSpeed: int, IncreaseAmount: int, VerticalChange: int, MaxHeight: int):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight

# ==========================
# 2(b)(ii) Helicopter IncreaseSpeed override
# ==========================
    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        # Vertical movement
        if self.__VerticalPosition + self.__VerticalChange <= self.__MaxHeight:
            self.__VerticalPosition += self.__VerticalChange
        else:
            self.__VerticalPosition = self.__MaxHeight

        # Speed
        if self.GetCurrentSpeed() + self.GetIncreaseAmount() <= self.GetMaxSpeed():
            new_speed = self.GetCurrentSpeed() + self.GetIncreaseAmount()
        else:
            new_speed = self.GetMaxSpeed()
        self.SetCurrentSpeed(new_speed)

        # Horizontal movement
        new_position = self.GetHorizontalPosition() + self.GetCurrentSpeed()
        self.SetHorizontalPosition(new_position)

# ==========================
# 2(c) Output Procedure
# ==========================
def OutputVehicleStatus(vehicle):
    print("Current speed:", vehicle.GetCurrentSpeed())
    print("Horizontal position:", vehicle.GetHorizontalPosition())
    if isinstance(vehicle, Helicopter):
        print("Vertical position:", vehicle.GetVerticalPosition())

# ==========================
# 2(d)(i) Main Program
# ==========================
# Instantiate Vehicle ("Tiger")
car = Vehicle("Tiger", 100, 20)
car.IncreaseSpeed()
car.IncreaseSpeed()
OutputVehicleStatus(car)

print("\n---\n")

# Instantiate Helicopter ("Lion")
heli = Helicopter("Lion", 350, 40, 3, 100)
heli.IncreaseSpeed()
heli.IncreaseSpeed()
OutputVehicleStatus(heli)
