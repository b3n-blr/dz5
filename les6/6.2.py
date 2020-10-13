class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.tickness = 0.05
        self.weigth = 25
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'необходимо {intake} тон для постройки')

road_to_village = Road(20, 5000)
road_to_village.intake()