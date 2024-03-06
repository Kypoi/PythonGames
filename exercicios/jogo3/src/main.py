from enum import Enum


class State(Enum):
    ACTIVE = 1
    INACTIVE = 2


class Robot:
    def __init__(self, name):
        self.name = name
        self.state = State.INACTIVE

    def activate(self):
        self.state = State.ACTIVE

    def deactivate(self):
        self.state = State.INACTIVE

    def is_active(self):
        if self.state == State.ACTIVE:
            return True
        else:
            return False


class SuperRobot(Robot):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def increase_speed(self, new_speed):
        if new_speed < self.speed:
            print("Por favor escolher um valor acima da velocidade atual do robot")
        else:
            self.speed = new_speed


def main():
    print("Bem-vindo ao BroBot")
    brobot = Robot("R2D2")
    brobot.activate()
    print(brobot.is_active())
    brobot.deactivate()
    print(brobot.is_active())

    superrobot = SuperRobot("S3P0", 100)
    superrobot.increase_speed(90)
    print(superrobot.speed)


if __name__ == "__main__":
    main()
