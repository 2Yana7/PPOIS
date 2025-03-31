import sys
from government.government import Government
from government.models import Laws, Citizen, Infrastructure, Economy
from utils.persistence import save_data, load_data

def law_state(government: Government):
    law_actions = {
        1: government.new_law,
        2: government.change_status_of_law,
        3: government.display_laws,
        4: lambda: 1
    }
    while True:
        try:
            print("\nДействия с законами:")
            print("1 - Добавить новый закон")
            print("2 - Изменить статус закона")
            print("3 - Показать список законов")
            print("4 - Назад")
            law_choice = int(input("Введите номер действия: ").strip())
            if not law_choice:
                raise ValueError("Пустой ввод")
            if 1 <= law_choice <= 4:
                result = law_actions[law_choice]()
                if result:
                    break
            else:
                print("Ошибка: выберите корректный номер действия.")
        except Exception as e:
            print(f"Ошибка: {e}")
    save_data(government)

def citizen_state(government: Government):
    citizen_actions = {
        1: government.add_citizen,
        2: government.del_citizen,
        3: government.display_citizen,
        4: government.pay_tax,
        5: government.display_debtor,
        6: government.ask_help,
        7: government.help_citizen,
        8: lambda: 1
    }
    while True:
        try:
            print("\nДействия с гражданами:")
            print("1 - Добавить гражданина")
            print("2 - Удалить гражданина")
            print("3 - Показать список граждан")
            print("4 - Оплатить налог")
            print("5 - Вывести должников")
            print("6 - Запросить соц выплату")
            print("7 - Оказать соц выплату")
            print("8 - Назад")
            citizen_choice = int(input("Введите номер действия: ").strip())
            if not citizen_choice:
                raise ValueError("Пустой ввод")
            if 1 <= citizen_choice <= 8:
                result = citizen_actions[citizen_choice]()
                if result:
                    break
            else:
                print("Ошибка: выберите корректный номер действия.")
        except Exception as e:
            print(f"Ошибка: {e}")
    save_data(government)

def infrastructure_state(government: Government):
    infrastructure_actions = {
        1: government.add_object,
        2: government.change_condition,
        3: government.show_infrastructure,
        4: government.del_infrastructure,
        5: lambda: 1
    }
    while True:
        try:
            print("\nДействия с инфраструктурой:")
            print("1 - Добавить объект")
            print("2 - Улучшить состояние объекта")
            print("3 - Список объектов")
            print("4 - Удаление объекта")
            print("5 - Назад")
            infrastructure_choice = int(input("Введите номер действия: ").strip())
            if not infrastructure_choice:
                raise ValueError("Пустой ввод")
            if 1 <= infrastructure_choice <= 5:
                result = infrastructure_actions[infrastructure_choice]()
                if result:
                    break
            else:
                print("Ошибка: выберите корректный номер действия.")
        except Exception as e:
            print(f"Ошибка: {e}")
    save_data(government)

def economy_state(government: Government, economy: Economy):
    def currency_change(_):
        economy.currency_change()
        government.currency = economy.currency
    economy_actions = {
        1: economy.calculate_average_salary,
        2: economy.salary_up,
        3: economy.salary_down,
        4: currency_change,
        5: lambda _: 1
    }
    while True:
        try:
            print("\nДействия с экономикой:")
            print("1 - Средняя зарплата")
            print("2 - Поднять зарплату")
            print("3 - Понизить зарплату")
            print("4 - Изменить валюту")
            print("5 - Назад")
            economy_choice = int(input("Введите номер действия: ").strip())
            if not economy_choice:
                raise ValueError("Пустой ввод")
            if 1 <= economy_choice <= 5:
                result = economy_actions[economy_choice](government.citizen_manager.citizens)
                if result:
                    break
            else:
                print("Ошибка: выберите корректный номер действия.")
        except Exception as e:
            print(f"Ошибка: {e}")
    save_data(government)

def foreign_relations_state(government: Government):
    foreign_relations_actions = {
        1: government.display_borders,
        2: government.change_bording,
        3: government.add_alliances,
        4: government.del_alliance,
        5: government.display_alliances,
    }
    while True:
        try:
            print("\nДействия с внешними отношениями:")
            print("1 - Список стран-соседей")
            print("2 - Поменять статус границы")
            print("3 - Добавить страну-союзника")
            print("4 - Удалить страну из союзников")
            print("5 - Список стран союзников")
            print("6 - Назад")
            foreign_relations_choice = int(input("Введите номер действия: ").strip())
            if not foreign_relations_choice:
                raise ValueError("Пустой ввод")
            if 1 <= foreign_relations_choice <= 5:
                foreign_relations_actions[foreign_relations_choice]()
            elif foreign_relations_choice == 6:
                break
            else:
                print("Ошибка: выберите корректный номер действия.")
        except Exception as e:
            print(f"Ошибка: {e}")
    save_data(government)

def exit_program(government: Government):
    print("Выход из программы.")
    save_data(government)
    sys.exit()

def main():
    # Загрузка данных
    data = load_data()
    laws_list = [Laws(item["title"], item["status"]) for item in data.get("laws", [])]
    citizens_list = [Citizen(item["name"], item["id"], item["incom"], item["tax_paid"], item["social_status"])
                     for item in data.get("citizens", [])]
    infrastructures_list = [Infrastructure(item["id"], item["type"], item["location"], item["condition"])
                            for item in data.get("infrastructures", [])]
    alliances_list = data.get("foreign_alliances", [])
    currency_data = data.get("currency", "Трумэн")
    tax_rate_data = data.get("tax_rate", 20)

    government = Government(
        name="Сихэвэн",
        laws=laws_list,
        currency=currency_data,
        tax_rate=tax_rate_data,
        my_object=infrastructures_list,
        foreign_relations=alliances_list,
        citizen=citizens_list
    )
    economy = Economy(salary=0, currency=currency_data)

    states = {
        1: lambda: government.display_country_info(),  # Пункт 1 - информация о государстве
        2: lambda: law_state(government),
        3: lambda: citizen_state(government),
        4: lambda: infrastructure_state(government),
        5: lambda: economy_state(government, economy),
        6: lambda: foreign_relations_state(government),
        7: lambda: exit_program(government)
    }
    try:
        while True:
            print("\nВыберите действие:")
            print("1 - Показать информацию о государстве")
            print("2 - Действия с законами")
            print("3 - Действия с гражданами")
            print("4 - Действия с инфраструктурой")
            print("5 - Действия с экономикой")
            print("6 - Действия с внешними отношениями")
            print("7 - Выйти")
            try:
                choice = int(input("Введите номер действия: ").strip())
                if not choice:
                    raise ValueError("Пустой ввод")
            except Exception as e:
                print(f"Ошибка ввода: {e}")
                continue
            if 1 <= choice <= 7:
                states[choice]()
            else:
                print("Ошибка: выберите корректный номер действия.")
    except KeyboardInterrupt:
        print("\nПрерывание программы. До свидания!")
        save_data(government)
        sys.exit()
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        save_data(government)
        sys.exit()

if __name__ == "__main__":
    main()