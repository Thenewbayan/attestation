# animal.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, birth_date, skills=None):
        self.name = name
        self.birth_date = birth_date
        self.skills = skills or []

    @abstractmethod
    def determine_class(self):
        pass

    def show_commands(self):
        print(f"Команды для {self.name}:")
        for skill in self.skills:
            print(f"- {skill}")

    def train(self, new_command):
        self.skills.append(new_command)
        print(f"{self.name} теперь знает команду: {new_command}")


class Dog(Animal):
    def determine_class(self):
        return "Собака"

class Cat(Animal):
    def determine_class(self):
        return "Кот"

class Camel(Animal):
    def determine_class(self):
        return "Верблюд"

class Hamster(Animal):
    def determine_class(self):
        return "Хомяк"

class Donkey(Animal):
    def determine_class(self):
        return "Осел"

class Horse(Animal):
    def determine_class(self):
        return "Лошадь"
