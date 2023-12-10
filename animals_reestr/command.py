# command.py

class Command:
    def __init__(self, name):
        self.name = name

    def execute(self):
        pass


class SitCommand(Command):
    def execute(self):
        print(f"{self.name}: Сел")


class StayCommand(Command):
    def execute(self):
        print(f"{self.name}: Остался на месте")
