# animal_registry.py
from counter import Counter
from animal import Dog, Cat, Camel, Hamster, Donkey, Horse
from command import Command, SitCommand, StayCommand
import sqlite3

class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.conn = sqlite3.connect("animal_registry.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS animals (name TEXT, birth_date TEXT, class TEXT, skills TEXT)"
        )
        self.conn.commit()

    def create_animal(self):
        name = input("Введите имя животного: ")
        birth_date = input("Введите дату рождения животного (в формате DD.MM.YYYY): ")
        
        print("Выберите класс животного:")
        print("1. Собака")
        print("2. Кот")
        print("3. Верблюд")
        print("4. Хомяк")
        print("5. Осел")
        print("6. Лошадь")

        choice = input("Введите номер класса: ")
        animal = None
        if choice == "1":
            animal = Dog(name, birth_date)
        elif choice == "2":
            animal = Cat(name, birth_date)
        elif choice == "3":
            animal = Camel(name, birth_date)
        elif choice == "4":
            animal = Hamster(name, birth_date)
        elif choice == "5":
            animal = Donkey(name, birth_date)
        elif choice == "6":
            animal = Horse(name, birth_date)
        else:
            print("Некорректный выбор. Создание животного отменено.")
        if animal:
            self.animals.append(animal)
            self.save_animal_to_db(animal)
            print(f"{animal.name} успешно зарегистрировано!")

    def determine_animal_class(self):
        name = input("Введите имя животного: ")
        for animal in self.animals:
            if animal.name == name:
                animal_class = animal.determine_class()
                print(f"{animal.name} относится к классу {animal_class}.")
                break
        else:
            print(f"Животное с именем {name} не найдено.")

    def show_animal_commands(self):
        name = input("Введите имя животного: ")
        for animal in self.animals:
            if animal.name == name:
                animal.show_commands()
                break
        else:
            print(f"Животное с именем {name} не найдено.")

    def train_animal(self):
        name = input("Введите имя животного: ")
        for animal in self.animals:
            if animal.name == name:
                new_command = input("Введите новую команду для обучения: ")
                animal.train(new_command)
                self.update_animal_in_db(animal)
                break
        else:
            print(f"Животное с именем {name} не найдено.")

    def save_animal_to_db(self, animal):
        self.cursor.execute(
            "INSERT INTO animals (name, birth_date, class, skills) VALUES (?, ?, ?, ?)",
            (animal.name, animal.birth_date, animal.determine_class(), ",".join(animal.skills))
        )
        self.conn.commit()

    def update_animal_in_db(self, animal):
        self.cursor.execute(
            "UPDATE animals SET skills=? WHERE name=?",
            (",".join(animal.skills), animal.name)
        )
        self.conn.commit()

    def load_animals_from_db(self):
        self.cursor.execute("SELECT * FROM animals")
        rows = self.cursor.fetchall()
        for row in rows:
            name, birth_date, animal_class, skills = row
            skills_list = skills.split(",") if skills else []
            if animal_class == "Собака":
                self.animals.append(Dog(name, birth_date, skills_list))
            elif animal_class == "Кот":
                self.animals.append(Cat(name, birth_date, skills_list))
            elif animal_class == "Верблюд":
                self.animals.append(Camel(name, birth_date, skills_list))
            elif animal_class == "Хомяк":
                self.animals.append(Hamster(name, birth_date, skills_list))
            elif animal_class == "Осел":
                self.animals.append(Donkey(name, birth_date, skills_list))
            elif animal_class == "Лошадь":
                self.animals.append(Horse(name, birth_date, skills_list))

    def show_all_animals(self):
        print("Все зарегистрированные животные:")
        for animal in self.animals:
            print(f"{animal.name} ({animal.determine_class()}), Дата рождения: {animal.birth_date}")

def main():
    animal_registry = AnimalRegistry()
    animal_registry.load_animals_from_db()

    with Counter() as counter:
        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Определить животное в правильный класс")
            print("3. Увидеть список команд животного")
            print("4. Обучить животное новым командам")
            print("5. Вывести всех животных")
            print("6. Выйти из программы")

            choice = input("Выберите действие (введите номер): ")

            if choice == "1":
                animal_registry.create_animal()
                counter.add()
            elif choice == "2":
                animal_registry.determine_animal_class()
            elif choice == "3":
                animal_registry.show_animal_commands()
            elif choice == "4":
                animal_registry.train_animal()
            elif choice == "5":
                animal_registry.show_all_animals()
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
