from typing import List
from government.models import Laws, Citizen, Infrastructure

class LawManager:
    def __init__(self, laws: List[Laws]) -> None:
        self.laws = laws

    def new_law(self) -> None:
        try:
            title = input("Введи название закона: ").strip()
            if not title:
                raise ValueError("Название закона не может быть пустым")
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        new_law = Laws(title, status="неактивен")
        self.laws.append(new_law)
        self.display_laws()
        print('Закон добавлен со статусом "неактивен". Чтобы закон вступил в силу, измените его статус.')

    def change_status_of_law(self) -> None:
        try:
            title = input("Введи название закона: ").strip()
            if not title:
                raise ValueError("Название закона не может быть пустым")
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for law in self.laws:
            if law.title == title:
                found = True
                law.status = "активен" if law.status == "неактивен" else "неактивен"
                print("Статус закона изменён!")
                break
        if not found:
            print(f"Закон с названием {title} не найден")

    def display_laws(self) -> None:
        print("\nСписок законов:")
        if not self.laws:
            print("Список пуст")
        else:
            for law in self.laws:
                print(f"- {law.title}: {law.status}")

class CitizenManager:
    def __init__(self, citizens: List[Citizen]) -> None:
        self.citizens = citizens

    def add_citizen(self, currency: str) -> None:
        try:
            id_str = input("Введите ID гражданина: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        for citizen in self.citizens:
            if citizen.id == id:
                print(f"Гражданин с ID {id} уже существует")
                return
        try:
            name = input("Введите имя гражданина: ").strip()
            if not name:
                raise ValueError("Имя не может быть пустым")
            name = name.title()
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        try:
            incom_str = input("Введите доход гражданина: ").strip()
            if not incom_str:
                raise ValueError("Доход не может быть пустым")
            incom = int(incom_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        new_citizen = Citizen(name, id, incom, tax_paid="неуплачено", status="не запрошено")
        self.citizens.append(new_citizen)
        print(f"Гражданин с именем {name} добавлен")
        self.display_citizen(currency)

    def del_citizen(self, currency: str) -> None:
        try:
            id_str = input("Введите ID гражданина: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for citizen in self.citizens:
            if citizen.id == id:
                found = True
                self.citizens.remove(citizen)
                print(f"Гражданин с ID {id} удалён")
                self.display_citizen(currency)
                break
        if not found:
            print("Гражданин с таким ID не найден")

    def display_citizen(self, currency: str) -> None:
        print("\nСписок граждан:")
        if not self.citizens:
            print("Список граждан пуст")
        else:
            for citizen in self.citizens:
                citizen.display(currency)

    def display_debtor(self) -> None:
        print("\nСписок задолжавших граждан:")
        found = False
        for citizen in self.citizens:
            if citizen.tax_paid == "неуплачено":
                found = True
                print(f"ИМЯ: {citizen.name}   ID: {citizen.id}   НАЛОГИ: {citizen.tax_paid}")
        if not found:
            print("Должники отсутствуют")

    def help_citizen(self) -> None:
        try:
            id_str = input("Введите ID гражданина, которому нужна помощь: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for citizen in self.citizens:
            if citizen.id == id:
                found = True
                if citizen.social_status == "запрошено":
                    citizen.social_status = "отправлено"
                    print(f"Гражданину {citizen.name} отправлены социальные выплаты!")
                else:
                    print("Гражданин не запрашивал соц помощь")
                break
        if not found:
            print(f"Гражданин с ID {id} не найден")

    def pay_tax(self) -> None:
        try:
            id_str = input("Введите ID гражданина, который заплатит налог: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for citizen in self.citizens:
            if citizen.id == id:
                citizen.tax_paid = "уплочено"
                print(f"Гражданин {citizen.name} оплатил налог")
                found = True
                break
        if not found:
            print(f"Гражданин с ID {id} не найден")

    def ask_help(self) -> None:
        try:
            id_str = input("Введите ID гражданина, который запрашивает социальную помощь: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for citizen in self.citizens:
            if citizen.id == id:
                citizen.social_status = "запрошено"
                print(f"Гражданин {citizen.name} запросил помощь")
                found = True
                break
        if not found:
            print(f"Гражданин с ID {id} не найден")

class InfrastructureManager:
    def __init__(self, infrastructures: List[Infrastructure]) -> None:
        self.infrastructures = infrastructures

    def add_object(self) -> None:
        try:
            id_str = input("Введи ID объекта: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        for obj in self.infrastructures:
            if obj.id == id:
                print(f"Объект с ID {id} уже существует")
                return
        try:
            type_ = input("Введите тип объекта: ").strip()
            if not type_:
                raise ValueError("Тип объекта не может быть пустым")
            type_ = type_.title()
            location = input("Введите адрес: ").strip()
            if not location:
                raise ValueError("Адрес не может быть пустым")
            condition = input("Введите состояние объекта (хорошее/среднее/плохое): ").strip().lower()
            if condition not in ["хорошее", "среднее", "плохое"]:
                raise ValueError("Неверное состояние объекта")
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        new_object = Infrastructure(id, type_, location, condition)
        self.infrastructures.append(new_object)
        self.show_infrastructure()

    def change_condition(self) -> None:
        try:
            id_str = input("Введите ID объекта для улучшения статуса: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for obj in self.infrastructures:
            if obj.id == id:
                found = True
                if obj.condition == "плохое":
                    obj.condition = "среднее"
                    print(f"Теперь состояние объекта {obj.type} среднее")
                elif obj.condition == "среднее":
                    obj.condition = "хорошее"
                    print(f"Теперь состояние объекта {obj.type} хорошее")
                elif obj.condition == "хорошее":
                    print(f"Состояние объекта {obj.type} и так лучше некуда")
                break
        if not found:
            print(f"Объект с ID {id} не найден")

    def show_infrastructure(self) -> None:
        print("\nСписок объектов:")
        if not self.infrastructures:
            print("Список пуст")
        else:
            for obj in self.infrastructures:
                print(f"ОБЪЕКТ: {obj.type}  АДРЕС: {obj.location}  ID: {obj.id}  СОСТОЯНИЕ: {obj.condition}")

    def del_infrastructure(self) -> None:
        try:
            id_str = input("Введите ID объекта: ").strip()
            if not id_str:
                raise ValueError("ID не может быть пустым")
            id = int(id_str)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
            return
        found = False
        for obj in self.infrastructures:
            if obj.id == id:
                found = True
                self.infrastructures.remove(obj)
                print("Объект удалён")
                self.show_infrastructure()
                break
        if not found:
            print(f"Объект с ID {id} не найден")
