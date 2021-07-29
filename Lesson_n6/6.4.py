class Cars:
    def __init__(self, name, speed, color, is_police: bool = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} started to go.'

    def stop(self):
        self.speed = 0
        return f'{self.name} stopped.'

    def turn(self, direction: str):
        if direction not in ('left', 'right'):
            return f"'{direction}' is not valid direction"
        else:
            return f"{self.name} turned {direction}"

    def show_speed(self):
        return f'Current speed of {self.name} - {self.speed}'


class TownCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"{self.name}'s speed is higher than allowed range"
        else:
            return f"{self.name}'s speed is in allowed range, which is {self.speed}"


class SportCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(name, speed, color, is_police=False)


class WorkCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(name, speed, color, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name}'s speed is higher than allowed range"
        else:
            return f"{self.name}'s speed is in allowed range, which is {self.speed}"


class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(name, speed, color, is_police=True)


bugatti = SportCar(200, 'Blue', 'Bugatti', False)
print(f"\n{bugatti.go()}\n{bugatti.show_speed()}\n{bugatti.turn('right')}\n{bugatti.stop()}\n{bugatti.speed}")
priora = TownCar(50, 'black', 'Lada Priora', False)
print(f"\n{priora.name}\n{priora.color}\n{priora.show_speed()}")
police = PoliceCar(70, 'White', 'Police', True)
print(f"\n{police.name}\n{police.show_speed()}\n{police.is_police}")
