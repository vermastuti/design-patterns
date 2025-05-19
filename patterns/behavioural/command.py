from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver
class Light:
    def turn_on(self):
        print("The light is ON")

    def turn_off(self):
        print("The light is OFF")


# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# Client
if __name__ == "__main__":
    # Receiver
    light = Light()

    # Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Invoker
    remote = RemoteControl()

    # Turn the light ON
    remote.set_command(light_on)
    remote.press_button()

    # Turn the light OFF
    remote.set_command(light_off)
    remote.press_button()