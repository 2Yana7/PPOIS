from typing import List

class Laws:
    def __init__(self, title: str, status: str) -> None:
        self.title: str = title
        self.status: str = status

class Citizen:
    def __init__(self, name: str, id: int, incom: int, tax_paid: str, status: str) -> None:
        self.name: str = name
        self.id: int = id
        self.incom: int = incom  # ДОХОД
        self.tax_paid: str = tax_paid  # "уплочено"/"неуплачено"
        self.social_status: str = status  # например, "запрошено", "отправлено"

    def display(self, currency: str) -> None:
        print(f"ИМЯ: {self.name}   ID: {self.id}   ДОХОД: {self.incom} {currency}   НАЛОГИ: {self.tax_paid}   СОЦ. статус: {self.social_status}")

class Infrastructure:
    def __init__(self, id: int, type: str, location: str, condition: str) -> None:
        self.id: int = id
        self.type: str = type  # школа, дороги и т.д.
        self.location: str = location
        self.condition: str = condition  # состояние объекта

class Economy:
    def __init__(self, salary: int, currency: str) -> None:
        self.average_salary: int = salary  # средняя зарплата граждан
        self.currency: str = currency  # валюта

    def calculate_average_salary(self, list_of_citizen: List[Citizen]) -> None:
        n: int = len(list_of_citizen)
        total_income: int = sum(c.incom for c in list_of_citizen)
        if n != 0:
            average: float = total_income / n
            print(f"Средняя зарплата: {average} {self.currency}")
        else:
            print("Граждан нет")

    def salary_up(self, list_of_citizen: List[Citizen]) -> None:
        try:
            up_str: str = input("На сколько повышаем среднюю зарплату (число): ").strip()
            if not up_str:
                raise ValueError("Пустой ввод")
            up: int = int(up_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        for citizen in list_of_citizen:
            citizen.incom += up
        print(f"Зарплата увеличена на {up} {self.currency}\n")
        self.calculate_average_salary(list_of_citizen)

    def salary_down(self, list_of_citizen: List[Citizen]) -> None:
        try:
            down_str: str = input("На сколько понижаем среднюю зарплату (число): ").strip()
            if not down_str:
                raise ValueError("Пустой ввод")
            down: int = int(down_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        for citizen in list_of_citizen:
            citizen.incom -= down
            if citizen.incom < 0:
                citizen.incom = 0
        print(f"Зарплата понижена на {down} {self.currency}\n")
        self.calculate_average_salary(list_of_citizen)

    def currency_change(self) -> None:
        try:
            new_currency: str = input("Введите новую валюту: ").strip()
            if not new_currency:
                raise ValueError("Валютный ввод не может быть пустым")
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        print(f"Теперь валюта {new_currency}")
        self.currency = new_currency

class Foreign_relations:
    def __init__(self, alliances: List[str]) -> None:
        self.list_of_bordering_countries: List[str] = ['Нарния', 'Ваканда', 'Готэм-Сити', 'Спрингфилд']
        self.list_of_alliances: List[str] = alliances
        self.bording_status: List[str] = ["открыта"] * len(self.list_of_bordering_countries)

    def display_bording_status(self) -> None:
        print("Список граничащих стран:")
        for i, country in enumerate(self.list_of_bordering_countries):
            print(f"СТРАНА: {country}  ГРАНИЦА: {self.bording_status[i]}")

    def change_bording_status(self) -> None:
        try:
            name: str = input("Введи название страны, статус границы которой хотите поменять: ").strip()
            if not name:
                raise ValueError("Название страны не может быть пустым")
            name = name.title()
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found: bool = False
        for i, country in enumerate(self.list_of_bordering_countries):
            if name == country:
                found = True
                self.bording_status[i] = "открыта" if self.bording_status[i] == "закрыта" else "закрыта"
                print(f"Статус границы для страны {name} изменён")
                break
        if not found:
            print(f"Страна {name} не является соседом")

    def add_alliances(self) -> None:
        try:
            new_alliance: str = input("Введи новую страну-союзника: ").strip()
            if not new_alliance:
                raise ValueError("Название страны не может быть пустым")
            new_alliance = new_alliance.title()
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        if new_alliance in self.list_of_alliances:
            print(f"Страна {new_alliance} уже союзник")
        else:
            self.list_of_alliances.append(new_alliance)
            print(f"Страна {new_alliance} добавлена в список союзников")

    def del_alliances(self) -> None:
        try:
            alliance: str = input("Введи страну, которую нужно удалить из списка союзников: ").strip()
            if not alliance:
                raise ValueError("Название страны не может быть пустым")
            alliance = alliance.title()
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        if alliance in self.list_of_alliances:
            self.list_of_alliances.remove(alliance)
            print(f"Страна {alliance} удалена из списка союзников")
        else:
            print(f"Страны {alliance} нет в списке союзников")

    def display_alliance(self) -> None:
        print("Список союзников:")
        if not self.list_of_alliances:
            print("Список пуст")
        else:
            for alliance in self.list_of_alliances:
                print(alliance)

    def del_alliance(self) -> None:
        self.del_alliances()

    def display_alliances(self) -> None:
        self.display_alliance()
